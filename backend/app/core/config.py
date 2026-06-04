from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "TRINETRA OSINT API"
    version: str = "1.0.0"
    debug: bool = False

    # Database
    database_url: str = "sqlite+aiosqlite:///./trinetra.db"

    # Redis (optional for dev)
    redis_url: Optional[str] = None

    # CORS
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    # Rate limiting
    trust_proxy_headers: bool = False  # Set true behind a known reverse proxy

    # Cache TTLs (seconds)
    cache_ttl_default: int = 3600  # 1 hour
    cache_ttl_long: int = 86400    # 24 hours

    # Plugin timeouts (seconds)
    plugin_timeout: int = 30

    # API authentication
    # Set API_KEY in .env to enable auth. Leave empty = open access (dev mode).
    # When set, all /api/search and /api/watches endpoints require:
    #   Authorization: Bearer <API_KEY>  OR  X-API-Key: <API_KEY>
    api_key: str = ""

    # External API keys
    hibp_api_key: str = ""  # Have I Been Pwned v3 API key (set via HIBP_API_KEY env var)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
