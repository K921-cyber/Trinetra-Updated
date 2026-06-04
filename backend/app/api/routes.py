from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timezone
from app.models.schemas import SearchRequest, SearchResponse, PluginResultData
from app.services.orchestrator import OrchestratorService
from app.core.detector import AutoDetect
from app.core.sanitizer import sanitize_target, validate_target, InputValidationError
from app.core.api_key_auth import require_api_key

router = APIRouter(prefix="/api", tags=["search"])
orchestrator = OrchestratorService()


@router.post("/search")
async def search(request: SearchRequest, _key: str = Depends(require_api_key)):
    """Run all applicable OSINT plugins against a target."""
    # Sanitize input
    try:
        target = sanitize_target(request.target)
    except InputValidationError as e:
        raise HTTPException(400, detail={"error": e.message, "detail": e.detail})

    # Validate target type
    is_valid, detected_type, validation_error = validate_target(target)
    if not is_valid and not request.type:
        raise HTTPException(400, detail={"error": validation_error})

    # Auto-detect type
    target_type = request.type or detected_type
    if target_type == "unknown":
        target_type = "domain"  # default fallback

    # Run all matching plugins in parallel
    results = await orchestrator.run_all(target, target_type)

    return SearchResponse(
        target=target,
        type=target_type,
        timestamp=datetime.now(timezone.utc),
        total_plugins=len(results),
        completed_plugins=sum(1 for r in results if r.get("status") == "completed"),
        results=results,
    )


@router.get("/search/{target}")
async def search_get(target: str, _key: str = Depends(require_api_key)):
    """GET version of search for simple lookups."""
    # Sanitize input
    try:
        target = sanitize_target(target)
    except InputValidationError as e:
        raise HTTPException(400, detail={"error": e.message, "detail": e.detail})

    target_type = AutoDetect.detect(target)
    if target_type == "unknown":
        target_type = "domain"

    results = await orchestrator.run_all(target, target_type)

    return SearchResponse(
        target=target,
        type=target_type,
        timestamp=datetime.now(timezone.utc),
        total_plugins=len(results),
        completed_plugins=sum(1 for r in results if r.get("status") == "completed"),
        results=results,
    )


@router.get("/detect")
async def detect_target(target: str, _key: str = Depends(require_api_key)):
    """Auto-detect what type of target this is."""
    try:
        target = sanitize_target(target)
    except InputValidationError as e:
        raise HTTPException(400, detail={"error": e.message, "detail": e.detail})
    return AutoDetect.detect_full(target)


@router.get("/plugins")
async def list_plugins(_key: str = Depends(require_api_key)):
    """List all available OSINT plugins."""
    from app.plugins.registry import plugin_registry
    return {
        "total": len(plugin_registry.plugins),
        "plugins": [
            {
                "id": p.plugin_id,
                "name": p.name,
                "category": p.category,
                "description": p.description,
                "input_types": p.input_types,
            }
            for p in plugin_registry.plugins
        ],
    }
