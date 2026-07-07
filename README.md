<br/>

<div align="center">
  <br/>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/TRINETRA-v1.0.0-8b5cf6?style=for-the-badge&logo=appveyor&labelColor=0b0f1a">
    <img src="https://img.shields.io/badge/TRINETRA-v1.0.0-8b5cf6?style=for-the-badge&logo=appveyor&labelColor=0b0f1a" alt="TRINETRA">
  </picture>
  <br/>
  <h3>India-Focused OSINT Intelligence Dashboard</h3>
  <p>
    <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+"/>
    <img src="https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react&logoColor=white" alt="React 18"/>
    <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
    <img src="https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
    <img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose"/>
    <img src="https://img.shields.io/badge/TypeScript-5.6-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript 5.6"/>
    <img src="https://img.shields.io/badge/Leaflet-1.9-199900?style=flat-square&logo=leaflet&logoColor=white" alt="Leaflet 1.9"/>
    <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License"/>
    <img src="https://img.shields.io/badge/tests-138%20passed-brightgreen?style=flat-square" alt="138 Tests Passing"/>
  </p>
  <br/>
</div>

> **Search any domain, IP, email, phone, or name — get 360° threat intelligence in seconds.**
>
> TRINETRA is an all-in-one OSINT platform built for India. It combines 20 parallel OSINT plugins, a live threat feed powered by real malicious IP data, automated watch monitoring, and a Telegram OSINT bot — all wrapped in a dark-themed interactive map dashboard.

<br/>

<p align="center">
  <b>🔍 OSINT Search</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>🗺️ Live Threat Map</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>📡 Real-Time Feed</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>👁️ Watch Monitoring</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>📊 Professional Reports</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>🧠 Relationship Graphs</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>🤖 Telegram OSINT Bot</b>
</p>

<br/>

---

## 📋 Table of Contents

- [📸 Dashboard Preview](#-dashboard-preview)
- [⚡ Quick Start (Docker)](#-quick-start-docker)
- [🛠️ Manual Installation](#️-manual-installation)
- [🎯 What TRINETRA Does](#-what-trinetra-does)
- [🏗️ Architecture & Workflow](#️-architecture--workflow)
- [🔍 OSINT Search — How It Works](#-osint-search--how-it-works)
- [📡 Live Threat Feed — How It Works](#-live-threat-feed--how-it-works)
- [👁️ Watch Monitoring — How It Works](#️-watch-monitoring--how-it-works)
- [🤖 Telegram OSINT Bot — How It Works](#-telegram-osint-bot--how-it-works)
- [🗺️ Interactive Map — How It Works](#️-interactive-map--how-it-works)
- [📡 Real Data Sources](#-real-data-sources)
- [✨ Features](#-features)
- [📡 API Reference](#-api-reference)
- [🧪 Running Tests](#-running-tests)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Configuration Reference](#️-configuration-reference)
- [🔐 Authentication & Rate Limiting](#-authentication--rate-limiting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

<br/>

---

## 📸 Dashboard Preview

<p align="center">
  <i>🚀 The dashboard features an interactive India threat map, live attack vectors from real threat intelligence feeds, city risk analysis, and comprehensive search results — all in one unified dark-themed interface.</i>
</p>

### Main Dashboard Views

| View | Description |
|------|-------------|
| **Search** | Search any domain, IP, email, phone, or name. Results stream live via WebSocket across 20 OSINT plugins. |
| **Live Feed** | Real-time timeline of attack vectors, threat events, and cyber news from RSS feeds. |
| **Watches** | Create and manage automated monitoring targets with change detection alerts. |

### Map Overlays

| Overlay | Description |
|---------|-------------|
| **Attack Vectors** | Animated dashed lines with traveling dots showing real malicious IPs targeting Indian cities. |
| **Crime Heatmap** | State-wise NCRB 2022 cyber crime data with color-coded GeoJSON boundaries. |
| **City Markers** | Color-coded circles (green/yellow/red) based on NCRB statistics at major Indian cities. |
| **Destination Pins** | Aggregated attack destination markers showing vector counts, origins, and attack types. |

<br/>

---

## ⚡ Quick Start (Docker)

Get TRINETRA running in under 2 minutes with Docker.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac) or Docker Engine (Linux)
- [Git](https://git-scm.com/)

### Step-by-Step Installation

```bash
# Step 1: Clone the repository
git clone https://github.com/K921-cyber/trinetra.git
cd trinetra

# Step 2: Create and configure environment variables
cp .env.example .env
# ⚠️ Edit .env — set POSTGRES_PASSWORD (required), API keys are optional

# Step 3: Launch the full stack (5 services)
docker compose up --build -d

# Step 4: Verify all services are running
docker compose ps

# Step 5: Open the dashboard
# → http://localhost:3000
```

### What Gets Deployed

When you run `docker compose up`, these 5 containers start:

| Container | Service | Port | Purpose |
|-----------|---------|------|---------|
| `trinetra-frontend` | Nginx + React SPA | `3000` | Serves the dashboard UI, proxies API/WS to backend |
| `trinetra-backend` | FastAPI (Python 3.11) | `8000` | REST API + WebSocket server |
| `trinetra-worker` | TaskIQ Worker | — | Background watch task execution |
| `trinetra-db` | PostgreSQL 15 | `5432` | Persistent storage for watches, alerts, scan results |
| `trinetra-cache` | Redis 7 | `6380` | Task queue backend, caching |

### Access the Dashboard

| Service | URL | Description |
|---------|-----|-------------|
| **Dashboard** | [http://localhost:3000](http://localhost:3000) | Full OSINT intelligence dashboard |
| **API Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) | Swagger UI for all REST endpoints |
| **Health Check** | [http://localhost:8000/health](http://localhost:8000/health) | Backend health + plugin status |
| **Data Source Health** | [http://localhost:8000/api/health/sources](http://localhost:8000/api/health/sources) | Live status of all threat feeds and RSS sources |

### Docker Management Commands

```bash
# Start all services (in background)
docker compose up -d

# Rebuild and start (after code changes)
docker compose up --build -d

# Stop all services
docker compose down

# Stop and clear volumes (deletes database data)
docker compose down -v

# Watch backend logs (real-time)
docker compose logs -f backend

# Watch frontend logs
docker compose logs -f frontend

# Check container health
docker compose ps

# Run one-time command in backend container
docker compose exec backend python -c "print('hello')"

# Access PostgreSQL
docker compose exec postgres psql -U trinetra -d trinetra
```

<br/>

---

## 🛠️ Manual Installation

Run TRINETRA locally without Docker for development purposes.

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15 (optional — SQLite works for development)
- Redis 7 (optional — in-memory task queue works for development)

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows (CMD):
venv\Scripts\activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Install test dependencies (optional)
pip install pytest pytest-asyncio pytest-cov

# Create .env file (copy from project root)
cp ../.env.example ../.env
# Edit .env — set DATABASE_URL for PostgreSQL or leave default for SQLite

# Run database migrations (SQLite — auto-creates tables)
# Tables are created automatically on first startup

# Start the backend server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Or build for production
npm run build
npm run preview
```

### Redis Setup (Optional — for production task queue)

```bash
# Using Docker (recommended for local dev)
docker run -d -p 6379:6379 --name trinetra-redis redis:7-alpine

# Set REDIS_URL in .env:
# REDIS_URL=redis://localhost:6379/0
```

### Environment Variables (.env)

```bash
# Copy the example file first
cp .env.example .env
```

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `POSTGRES_PASSWORD` | **Yes** (Docker) | — | PostgreSQL password (must be set for Docker) |
| `POSTGRES_USER` | No | `trinetra` | PostgreSQL username |
| `POSTGRES_DB` | No | `trinetra` | PostgreSQL database name |
| `APP_NAME` | No | `TRINETRA OSINT API` | Application display name |
| `DEBUG` | No | `true` | Enable debug mode and verbose logging |
| `DATABASE_URL` | No | SQLite (`sqlite+aiosqlite:///./trinetra.db`) | Database connection string |
| `REDIS_URL` | No | In-memory (dev) | Redis connection for task queue |
| `API_KEY` | No | Empty (open access) | API key for endpoint authentication |
| `HIBP_API_KEY` | No | Empty | Have I Been Pwned v3 API key |
| `TELEGRAM_BOT_TOKEN` | No | Empty | Telegram Bot token from @BotFather |
| `TELEGRAM_OSINT_API_URL` | No | Empty | OSINT Leak API base URL |
| `TELEGRAM_OSINT_API_KEY` | No | Empty | API key for OSINT API |

### Running Without Docker (Full Development Setup)

Open **3 terminal windows**:

```bash
# Terminal 1: Backend
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
# Opens at http://localhost:5173

# Terminal 3: TaskIQ Worker (optional — for watch monitoring)
cd backend
source venv/bin/activate
taskiq worker app.tasks.broker:broker app.tasks.watch_tasks
```

> **Note:** In development mode (no Redis), TaskIQ uses an in-memory broker and tasks run inline, so the worker process is not required for basic functionality.

<br/>

---

## 🎯 What TRINETRA Does

### The Problem

Investigating a single domain typically means juggling **9+ separate tools**:

| Task | Tool | Time |
|------|------|------|
| WHOIS lookup | Separate website | ~2 min |
| DNS records | Another site | ~2 min |
| Port scan | nmap / Shodan | ~5 min |
| SSL check | Yet another tool | ~1 min |
| Subdomain discovery | crt.sh | ~2 min |
| Data breach check | Have I Been Pwned | ~1 min |
| CVE lookup | NVD | ~2 min |
| Tech fingerprint | Wappalyzer | ~1 min |
| Geo-location | ip-api.com | ~1 min |

**Total: 15–30 minutes** of context switching between tabs.

### TRINETRA's Solution

```
┌─────────────────────────────────────────────────────────────┐
│                    One Search. 20 Plugins.                   │
│                    Results in 10–15 seconds.                 │
└─────────────────────────────────────────────────────────────┘
```

**Four independent systems running simultaneously:**

1. **🔍 On-Demand OSINT Search** — Run 20 parallel plugins against any target
2. **📡 Live Threat Feed** — Background loop fetching real malicious IPs and cyber news
3. **👁️ Watch Monitoring** — Automated re-scanning with change detection alerts
4. **🤖 Telegram OSINT Bot** — Search data leaks via Telegram commands

<br/>

---

## 🏗️ Architecture & Workflow

```
                    ┌──────────────────────────────────────┐
                    │   User's Browser (port 3000)          │
                    │   React 18 + TypeScript + Vite        │
                    │   Leaflet Map + Cytoscape Graphs      │
                    └──────────────┬──────────┬─────────────┘
                                  HTTP       WebSocket
                                    │            │
                    ┌───────────────▼────────────▼─────────────┐
                    │           Nginx (port 80)                 │
                    │   Serves static build /api/* → backend   │
                    │              /ws/* → backend             │
                    └──────────────────────┬───────────────────┘
                                           │
                    ┌──────────────────────▼───────────────────┐
                    │    FastAPI Backend (port 8000)            │
                    │                                          │
                    │  ┌──────────┐  ┌──────────────────────┐  │
                    │  │ REST API │  │  WebSocket Streaming  │  │
                    │  │ /search  │  │  /ws/search           │  │
                    │  │ /watch   │  │  /ws/threats          │  │
                    │  │ /plugins │  └──────────────────────┘  │
                    │  └────┬─────┘                            │
                    │        │                                 │
                    │  ┌────▼─────────────────────────────┐    │
                    │  │    Plugin Orchestrator            │    │
                    │  │   ┌──────────┐ ┌──────────┐      │    │
                    │  │   │ 20 OSINT │ │ Watch    │      │    │
                    │  │   │ Plugins  │ │ Scheduler│      │    │
                    │  │   └──────────┘ └──────────┘      │    │
                    │  └──────────────────────────────────┘    │
                    │                                          │
                    │  ┌──────────────────────┐  ┌──────────┐ │
                    │  │ Threat Feed Service  │  │ TaskIQ   │ │
                    │  │ (background loop)    │  │ Worker   │ │
                    │  └──────────────────────┘  └──────────┘ │
                    │                                          │
                    │  ┌──────────────────┐                    │
                    │  │ Telegram Bot     │                    │
                    │  │ (optional)       │                    │
                    │  └──────────────────┘                    │
                    └────────────┬────────┬────────┬──────────┘
                                │        │        │
                    ┌───────────▼──┐ ┌───▼───┐ ┌─▼──────────────┐
                    │  PostgreSQL  │ │ Redis │ │  External       │
                    │  (watches,   │ │(queue)│ │  APIs &         │
                    │   alerts)    │ │       │ │  Feeds          │
                    └──────────────┘ └───────┘ └─────────────────┘
```

### Data Flow

```
User Input → Auto-Detect → Parallel Plugins (asyncio.gather) → WebSocket Stream → React UI
                                                                    │
                                                            ┌───────▼───────┐
                                                            │  Live Results │
                                                            │  as they       │
                                                            │  complete      │
                                                            └───────────────┘
```

### Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React 18 + TypeScript + Vite | UI — map, reports, graphs, live feed, watch panel |
| **Mapping** | Leaflet + react-leaflet | India threat map with SVG animated attack vectors |
| **Graphs** | Cytoscape + cytoscape-dagre | Relationship visualization from scan results |
| **Backend** | FastAPI + Python 3.11 | REST API + WebSocket server |
| **Database** | PostgreSQL 15 / SQLite | Persistent storage (watches, alerts, scan results) |
| **Cache** | Redis | Task queue backend + optional caching |
| **Worker** | TaskIQ | Background watch task execution |
| **Data** | httpx + aiohttp + feedparser | External API calls + RSS parsing |
| **Bot** | python-telegram-bot | Telegram OSINT leak search |
| **Container** | Docker + Docker Compose | Production deployment |

<br/>

---

## 🔍 OSINT Search — How It Works

### Workflow

```
  Target Query ──→ Input Sanitizer ──→ Auto-Detect Type ──→ 20 Parallel Plugins ──→ Stream Results
                           │                    │
                     Control chars,        domain / IP /
                     injection checks      email / phone / name
```

### Step-by-Step

1. **Input Sanitization** — The target string is validated against:
   - Maximum length (253 characters — DNS hostname limit)
   - No control characters, null bytes, or shell metacharacters
   - Strict regex patterns per type (domain, IP, email, phone, name)

2. **Auto-Detect Type** — The `AutoDetect` class determines the target type:
   - `re.match` for IP addresses, emails, domains, and phone numbers
   - Falls back to "name" for unrecognized inputs
   - Returns confidence scores (1.0 for IP/email, 0.95 for domain, 0.85 for phone, 0.6 for name)

3. **Plugin Registry** — The `PluginRegistry` scans all plugin subdirectories at startup and auto-registers every `OSINTPlugin` subclass. Plugins are organized by:
   - **Category**: infrastructure, threat, person, advanced
   - **Input type**: domain, ip, email, phone, username, name

4. **Plugin Orchestration** — The `OrchestratorService`:
   - Queries the registry for plugins matching the target type
   - Fires all matching plugins concurrently via `asyncio.gather`
   - Each plugin has a 30-second timeout (configurable)
   - Results stream back via WebSocket using `asyncio.as_completed`

5. **WebSocket Streaming** — The `/ws/search` endpoint:
   - Accepts client connection
   - Sends `{"type": "start", "total": N, "plugins": [...]}`
   - Sends `{"type": "result", "result": {...}, "completed": X, "total": N}` for each plugin
   - Sends `{"type": "complete", "total": N, "completed": N}` when done

### REST API Alternative

For non-streaming scenarios, use `POST /api/search` which returns all results in a single JSON response after all plugins complete.

### The 20 OSINT Plugins

| Category | Plugin ID | Name | What It Finds | Input Types |
|----------|-----------|------|---------------|-------------|
| **Infrastructure** | `domain-record` | Domain Record | WHOIS registration, registrar info, creation/expiry dates | domain |
| | `name-servers` | Name Servers | DNS records: A, AAAA, MX, NS, CNAME, TXT, SOA | domain |
| | `port-scanner` | Port Scanner | Open TCP ports (24 common ports), service identification | domain, ip |
| | `ssl-health` | SSL Health | Certificate validity, cipher suites, protocol support, grade | domain |
| | `subdomain-finder` | Subdomain Finder | Subdomains via crt.sh, HackerTarget API, DNS brute-force (185+ prefixes) | domain |
| | `geo-locator` | Geo Locator | Server location, country, city, ISP, ASN, coordinates | domain, ip |
| | `http-headers` | HTTP Headers | Security headers (HSTS, CSP, XFO, etc.), server info, cookies | domain |
| | `name-servers` | Name Servers | DNS records resolution | domain |
| | `tech-fingerprint` | Tech Fingerprint | Web server, frameworks, CMS, Cloudflare detection | domain |
| **Threat Intel** | `cve-alerts` | CVE Alerts | Known vulnerabilities from NVD API matching target | domain, ip |
| | `data-leaks` | Data Leaks | Breach data from XposedOrNot, LeakCheck, LeakIX + curated breach DB (70+ India-specific breaches) | domain, email, username |
| | `document-vault` | Document Vault | Exposed documents, .env, .git/config, backup files on common paths | domain |
| | `osint-leak` | OSINT Leak | Deep breach search via Leakosint API (email, phone, name, IP, username) | email, phone, username, name, ip |
| **Advanced** | `deep-search` | Deep Search | Google dorking queries for sensitive files, admin panels, backups | domain, name |
| | `live-feed` | Live Feed | Real-time cyber news from RSS feeds (The Hacker News) | domain, ip, name |
| | `social-radar` | Social Radar | Social media footprint across LinkedIn, Twitter, Facebook, Instagram, GitHub, etc. | username, name, email |
| | `surface-scan` | Surface Scan | Aggregated risk score, attack surface analysis, key port scanning | domain, ip |

### Performance

| Metric | Value |
|--------|-------|
| **Full scan (all matching plugins)** | 10–15 seconds |
| **Plugins run per search** | Up to 20 (depending on target type) |
| **API rate limit (search)** | 10 req/min per IP |
| **API rate limit (general)** | 60 req/min per IP |
| **Plugin timeout** | 30 seconds (configurable) |

<br/>

---

## 📡 Live Threat Feed — How It Works

### Workflow

```
ThreatFox ──┐
Feodo     ──┼──→ Fetch Real Malicious IPs (every 10 min)
IPsum    ───┘         │
                      ▼
              Geo-locate via ip-api.com
                      │
                      ▼
              Build Attack Vectors ──→ Broadcast via WebSocket (every 8-12 sec)
                      │
                      ▼
    ┌─────────────────┼─────────────────┐
    │                 │                 │
    ▼                 ▼                 ▼
Animated Map   Threat Ticker      Data Source
Lines + Dots   Events + News      Health Panel
```

### Background Services

The threat feed consists of **three independent background loops**:

#### 1. RealThreatService (Malicious IP Fetcher)

- **Interval**: Every 10 minutes
- **Sources**: Three free threat intelligence feeds in parallel
- **Processing**:
  1. Fetch CSV/dumps from ThreatFox, Feodo Tracker, and IPsum
  2. Parse IPs with real threat types (ransomware, phishing, botnet C2, etc.)
  3. Geo-locate IPs via ip-api.com (free, 45 req/min, no key required)
  4. Build attack vectors with real source IPs, malware family names, and feed attribution
  5. Cache geo-location results in-memory to minimize API calls
  6. Keep rolling buffer of 50 vectors
- **Attack Classification**:
  - Real attack types from feed metadata: Ransomware, Phishing, DDoS, Botnet C2, Malware
  - Severity from IPsum blacklist scores (≥5 = critical, ≥2 = medium)
  - Feodo C2 servers always classified as critical
  - Fallback classification when no keywords match (with disclosure note)
- **Target City Assignment**: Weighted random selection based on NCRB 2022 cyber crime statistics (higher crime = more attack targeting)

#### 2. RealNewsService (RSS News Fetcher)

- **Interval**: Every 5 minutes
- **Sources**: 4 RSS feeds fetched sequentially with 1-second politeness delay
  - The Hacker News
  - BleepingComputer
  - KrebsOnSecurity
  - The Record
- **Deduplication**: Up to 2,000 seen URLs tracked to prevent duplicates
- **Rolling buffer**: Max 200 headlines kept in memory
- **Categorization**: News automatically categorized into attack types (ransomware, phishing, malware, APT, etc.) and severity (critical/medium)

#### 3. ThreatFeedService (Broadcast Loop)

- **Interval**: Every 8–12 seconds per event
- **On connect**: Sends initial state with 20 recent vectors + 10 recent news headlines + city data
- **Broadcast**: 1 attack vector + 1 news headline per cycle
- **Subscriber model**: Each WebSocket connection gets a dedicated `asyncio.Queue`
- **City data**: Built from real NCRB 2022 crime statistics for 10 major Indian cities

### Data Transparency

All data includes disclosure notes about which parts are real vs. estimated:

| Data Point | Real? | Source |
|-----------|-------|--------|
| Source IP | ✅ Real | ThreatFox, Feodo, IPsum feeds |
| Geo-location | ✅ Real | ip-api.com |
| Attack Type | ✅ Real | Feed metadata keywords |
| Malware Family | ✅ Real | Feodo (Dridex, Emotet, QakBot) / ThreatFox |
| Severity | ✅ Real | IPsum blacklist score / source credibility |
| Target City | ⚠️ Statistical | NCRB 2022 crime-weighted distribution |

<br/>

---

## 👁️ Watch Monitoring — How It Works

### Workflow

```
Step 1: Create Watch
┌─────────────────────────────────────────────┐
│ Target: example.com | Interval: 1 hour       │
│ Plugins: [domain-record, ssl-health, ...]    │
└─────────────────────────────────────────────┘
                    │
                    ▼
Step 2: Scheduler Loop (every 60 seconds)
┌─────────────────────────────────────────────┐
│ Query `watches` table for due targets        │
│ WHERE is_active = TRUE                       │
│   AND (last_checked IS NULL                  │
│        OR NOW - last_checked >= interval)    │
└─────────────────────────────────────────────┘
                    │
                    ▼
Step 3: Scan Watch (via TaskIQ)
┌─────────────────────────────────────────────┐
│ Run specified plugins (or all matching)      │
│ against the target                           │
└──────────────┬──────────────────────────────┘
               │
               ▼
Step 4: Save & Compare
┌─────────────────────────────────────────────┐
│ Save new scan results to `scan_results`      │
│ Compare gui_data with previous scan          │
│ If changed → Create Alert                    │
│ Update last_checked_at                       │
└─────────────────────────────────────────────┘
```

### Key Features

- **Configurable Intervals**: 5 minutes to 7 days
- **Plugin Selection**: Choose exactly which plugins run per watch (or run all matching)
- **Smart Change Detection**: Compares `gui_data` JSON across scans — generates human-readable diffs
- **Alert History**: Full timeline of changes per watch target with old/new data
- **Pause/Resume**: Toggle watches on/off without deleting them
- **Database Backend**: PostgreSQL (production) or SQLite (development) with dual SQL query sets

### Alert Format

Each alert captures:
- `watch_id`: Which watch triggered
- `target`: The monitored target
- `plugin_id`: Which plugin detected changes
- `old_data`: Previous scan gui_data (JSON)
- `new_data`: New scan gui_data (JSON)
- `summary`: Human-readable diff (e.g., "SSL Health: 2 change(s) — Days Remaining: 45 → 44; Grade: A → A+")

### Retry Logic

On SQLite lock contention (common in concurrent dev scenarios), watch tasks retry up to 3 times with exponential backoff (1s, 2s, 4s).

<br/>

---

## 🤖 Telegram OSINT Bot — How It Works

### Workflow

```
Telegram User → Message → @YourBot
                            │
                    Auto-Detect Input Type
                      (email/phone/IP/domain/name)
                            │
                            ▼
                    OSINT Leak API (leakosintapi.com)
                            │
                            ▼
                    Format Results with Emojis
                            │
                            ▼
                    Send Rich Response to User
```

### Setup

```bash
# In .env, add:
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_OSINT_API_URL=https://leakosintapi.com/
TELEGRAM_OSINT_API_KEY=your_api_key_here
```

### Supported Commands

- `/start` — Welcome message with usage examples
- `/help` — Detailed command reference

### Query Types

| Type | Example | Detection Method |
|------|---------|-----------------|
| Email | `user@domain.com` | Regex with @ and valid domain |
| Phone | `+919876543210` | Starts with + or 7+ digits |
| IP | `192.168.1.1` | IPv4 pattern |
| Domain | `example.com` | Domain pattern (no spaces) |
| Name | `John Doe` | Default fallback |

### Response Format

Results are formatted with:
- Emoji-coded source names (🛥 Boat, 🧃 BigBasket, 🇮🇳 Truecaller, etc.)
- Field-specific emojis (📩 email, 📞 phone, 🔑 password, 👤 name, etc.)
- MarkdownV2 formatted for Telegram
- Auto-chunking for long responses (>4000 characters)
- Pagination indicator for multi-page results
- Disclosure of cached/censored results

### Auto-start/stop

The bot integrates into FastAPI's lifespan — starts with the server, stops on shutdown.

<br/>

---

## 🗺️ Interactive Map — How It Works

### Map Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    IndiaMap (React Component)                 │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  MapContainer (Leaflet)                                  │ │
│  │                                                          │ │
│  │  ├── TileLayer (CartoDB dark basemap)                   │ │
│  │  ├── MapController (programmatic center/zoom)           │ │
│  │  ├── AnimatedAttackOverlay (SVG lines + traveling dots) │ │
│  │  ├── CrimeHeatmap (GeoJSON state boundaries + NCRB)     │ │
│  │  ├── CityMarkers (10 major Indian cities, NCRB-risk)    │ │
│  │  └── DestinationPins (aggregated attack targets)        │ │
│  │                                                          │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                              │
│  ├── AttackCounter (live badge: critical/medium count)       │
│  ├── AttackInfoPanel (severity bars, origin intel, table)    │
│  ├── VectorDetailModal (full IP intel + report actions)      │
│  ├── DataSourcesPanel (feed health status)                   │
│  ├── Map Controls (show/hide attacks, crime, data sources)   │
│  └── Legend (threat levels, data source colors)              │
└──────────────────────────────────────────────────────────────┘
```

### Animation System

Attack vectors are rendered as an **SVG overlay** using Leaflet's `L.svgOverlay`:

- **Dashed lines** from origin country coordinates to Indian city coordinates
- **Traveling dots** (animated circles) moving along the line with easing
- **Glow filter** (feGaussianBlur) for visual emphasis
- **10 FPS throttle** to optimize performance
- **Pauses animation when tab is hidden** (visibility API)
- **Critical severity** vectors have faster cycle times (5s vs 7s)
- **Reuses SVG elements** across animation frames (no DOM re-creation)
- **Shallow comparison** on vector IDs to avoid unnecessary rebuilds

### City Risk Markers

10 major Indian cities are plotted with:
- **Risk level** derived from NCRB 2022 cyber crime statistics
- **Color-coded circles**: Safe (green), Medium (yellow), Critical (red)
- **Radius proportional** to risk level (7/10/14px)
- **Pulsing animation** for critical destinations
- **Asset count** proportional to NCRB incident count (500–3,500)
- **Active threats** derived from risk level (0–15)

### Origin Intelligence Panel

The Threat Intelligence panel (bottom-right of map) shows:
- **Severity distribution bars** (critical/medium/safe counts)
- **Origin intelligence** (country flags, attack counts, attack types)
- **Detailed attack routes table** (source IP, origin→target, attack type, malware, feed, severity)

### Vector Detail Modal

Clicking any attack vector opens a full intelligence modal with:
- **Source IP** with copy button
- **Geo-location** (ISP, organization)
- **Attack classification** (type, severity, malware, source feed)
- **Data transparency disclosure** (which fields are real vs. estimated)
- **Report actions**: AbuseIPDB, AlienVault OTX, CERT-In email, copy JSON

<br/>

---

## 📡 Real Data Sources

All data in TRINETRA is **real** — no simulated or placeholder data.

### Threat Intelligence Feeds

| Source | Type | Data Provided | Key Required? | Fetch Interval |
|--------|------|---------------|---------------|----------------|
| [Abuse.ch ThreatFox](https://threatfox.abuse.ch/) | Malware IOCs | Malicious IPs, malware families, attack types | ❌ Free | 10 min |
| [Feodo Tracker](https://feodotracker.abuse.ch/) | C2 Tracker | C2 server IPs, botnet malware (Dridex, Emotet, QakBot) | ❌ Free | 10 min |
| [IPsum](https://github.com/stamparm/ipsum) | IP Blacklist | Blacklisted IPs with detection scores (1-7) | ❌ Free | 10 min |
| [ip-api.com](https://ip-api.com/) | Geo-location | Country, city, lat/lon, ISP, org (45 req/min free tier) | ❌ Free | On-demand |

### OSINT Plugins Data Sources

| Plugin | Source(s) | Key Required? |
|--------|-----------|---------------|
| Domain Record | WHOIS servers (direct TCP on port 43, 25+ TLDs) | ❌ Free |
| Name Servers | dnspython (direct DNS resolution) | ❌ Free |
| Port Scanner | Built-in async TCP scanner (24 common ports) | ❌ Free |
| SSL Health | OpenSSL via socket (certificate chain, cipher, protocols) | ❌ Free |
| Subdomain Finder | crt.sh + HackerTarget API + DNS brute-force (185+ prefixes) | ❌ Free |
| Geo Locator | ip-api.com | ❌ Free |
| HTTP Headers | httpx (security headers analysis, 8 key headers tracked) | ❌ Free |
| Tech Fingerprint | httpx (server header, x-powered-by, cookie analysis) | ❌ Free |
| CVE Alerts | NVD API v2.0 | ❌ Free |
| Data Leaks | XposedOrNot + LeakCheck + LeakIX + curated breach DB (70+ India-specific) | ❌ Free |
| Document Vault | httpx (12 common sensitive paths checked) | ❌ Free |
| OSINT Leak | leakosintapi.com | 🔑 API Key |
| Deep Search | Google dork query generation (manual execution) | ❌ Free |
| Live Feed | RSS (The Hacker News) via feedparser | ❌ Free |
| Social Radar | HTTP HEAD requests to 8 social platforms | ❌ Free |
| Surface Scan | Built-in async port scanner + risk analyzer | ❌ Free |

### RSS News Feeds

| Feed | Topic | Icon |
|------|-------|------|
| [The Hacker News](https://thehackernews.com/) | General cybersecurity | 📰 |
| [BleepingComputer](https://www.bleepingcomputer.com/) | Tech news + malware | 💻 |
| [KrebsOnSecurity](https://krebsonsecurity.com/) | In-depth security reporting | 🔒 |
| [The Record](https://therecord.media/) | Cyber crime + policy | 📝 |

### India-Specific Data

| Source | Description |
|--------|-------------|
| **NCRB 2022** | Official cyber crime statistics for 23 Indian states/UTs (from "Crime in India 2022" report) |
| **Curated Breach DB** | 70+ India-specific breaches (Aadhaar, IRCTC, BigBasket, CoWIN, Truecaller, Jio, etc.) embedded in the Data Leaks plugin |
| **India Map** | India-specific GeoJSON boundaries for all states/UTs |
| **City Targeting** | 10 major Indian cities with NCRB-weighted attack distribution |

<br/>

---

## ✨ Features

### 🔍 OSINT Search (20 Plugins)

| Category | Plugins | What They Find |
|----------|---------|----------------|
| **Infrastructure** | WHOIS, DNS Lookup, Port Scanner, SSL Health, Subdomain Finder, Geo Locator, HTTP Headers, Name Servers, Tech Fingerprint | Registrar info, A/MX/NS records, open ports, certificate validity, subdomains, geo-location, security headers, tech stack |
| **Threat Intel** | CVE Alerts, Data Leaks, Document Vault, OSINT Leak | Known vulnerabilities (NVD), breach data (LeakIX, XposedOrNot, LeakCheck), exposed documents, deep leak search |
| **Advanced** | Deep Search, Surface Scan, Social Radar, Live Feed | Google dork queries, risk scoring, social media footprint, real-time cyber news |

**Every plugin queries live, free data sources** — no simulated or placeholder results.

### 🗺️ Interactive India Threat Map

- **Animated attack vectors** — Dashed lines with traveling dots from 25+ origin countries to Indian cities
- **City risk markers** — Color-coded circles (green/yellow/red) based on NCRB 2022 cyber crime statistics
- **Crime heatmap overlay** — State-wise NCRB cyber crime data with hover tooltips and click popups
- **Destination threat pins** — Aggregated attack destination markers showing live vector count, origin countries, attack types, and feed sources
- **Threat Intelligence panel** — Severity distribution bars, origin intelligence summary (flags + counts), detailed attack routes table
- **Live attack counter** — Real-time badge with critical/medium breakdown and LIVE indicator
- **Data Sources Health panel** — Live status of ThreatFox, Feodo, IPsum, ip-api.com, RSS feeds
- **10 FPS optimized animation** — Tab-aware: pauses when hidden to save CPU
- **Vector Detail Modal** — Full IP intelligence with AbuseIPDB, AlienVault, and CERT-In report actions

### 📡 Real-Time Threat Feed

- **Live events timeline** — Filterable by All, Attacks, Events, or News
- **Attack vector cards** — Color-coded by severity with origin→target route, type, and timestamp
- **Cyber news** — Latest headlines from The Hacker News, BleepingComputer, KrebsOnSecurity, The Record
- **Vector detail modal** — Full intelligence with copy IP, ISP, organization, report actions

### 📊 Professional Report View

- **Three view modes** — GUI (structured table), Terminal (raw output), Split (both side-by-side)
- **Export options** — Copy to clipboard, download as `.txt`, print/save as PDF
- **Full system report** — Executive summary, threat landscape, watches & alerts, intelligence events, recent scans
- **Search within results** — Filter through structured data in real-time

### 🧠 Relationship Graph

- **Dynamic Cytoscape visualization** — Auto-generated graph connecting search results by relationships
- **Color-coded node types** — Target (blue), Infrastructure (cyan), Threat (red), Person (pink), Advanced (purple), Domain (orange), Geo (green)
- **Layout** — Directed breadthfirst layout with animation
- **Export to PNG** — Save graphs at 2x resolution for reports
- **Click interaction** — Select nodes to highlight connections

### 👁️ Watch & Monitoring

- **Automated re-scanning** — Every 5 minutes to 7 days
- **Smart change detection** — Compares `gui_data` across scans, generates human-readable diffs
- **Alert history** — Full timeline of changes per watch target
- **Plugin-level control** — Select exactly which plugins to run per watch
- **Pause/Resume** — Toggle watches without data loss
- **Full Intelligence Report** — Generate comprehensive PDF-ready reports combining all watch data, threat intelligence, and scan results

### 🛡️ India-Specific Intelligence

- **NCRB 2022 cyber crime data** embedded for all 23 states/UTs
- **70+ curated India-specific data breaches** (Aadhaar, IRCTC, BigBasket, CoWIN, Truecaller, Jio, etc.)
- **India-focused map** with state boundaries, city markers, crime heatmap
- **Target city modeling** — Attack destinations statistically assigned from NCRB data
- **CERT-In incident reporting** — Pre-filled email template for reporting threats

### 🤖 Telegram OSINT Bot

- **Auto-detect query type** — email, phone, IP, domain, or name
- **Deep breach search** — Via Leakosint API
- **Rich formatting** — Emoji-coded sources and data fields
- **Multi-source aggregation** — Searches across multiple breach databases

<br/>

---

## 📡 API Reference

### REST Endpoints

| Method | Endpoint | Description | Auth | Rate Limit |
|--------|----------|-------------|------|------------|
| `GET` | `/` | API overview with available endpoints | ❌ Public | 60/min |
| `GET` | `/health` | Backend health + plugin counts | ❌ Public | — |
| `POST` | `/api/search` | Run OSINT scan on a target (all plugins) | Optional | 10/min |
| `GET` | `/api/search/{target}` | GET variant of search | Optional | 10/min |
| `GET` | `/api/detect?target=` | Auto-detect target type with confidence | Optional | 60/min |
| `GET` | `/api/plugins` | List all 20 OSINT plugins with metadata | Optional | 60/min |
| `GET` | `/api/target-intel?target=` | Web intelligence (DuckDuckGo + RSS news) | Optional | 60/min |
| `GET` | `/api/crime-data` | NCRB 2022 cyber crime data by state | ❌ Public | 60/min |
| `GET` | `/api/health/sources` | Health of all data sources | ❌ Public | 60/min |
| `GET` | `/api/watches` | List all watches | Optional | 60/min |
| `POST` | `/api/watches` | Create a watch | Optional | 60/min |
| `GET` | `/api/watches/{id}` | Get watch details | Optional | 60/min |
| `DELETE` | `/api/watches/{id}` | Delete a watch | Optional | 60/min |
| `POST` | `/api/watches/{id}/toggle` | Pause/resume a watch | Optional | 60/min |
| `GET` | `/api/watches/alerts` | Recent alerts across all watches | Optional | 60/min |
| `GET` | `/api/watches/alerts?limit=N` | Recent alerts (configurable limit) | Optional | 60/min |
| `GET` | `/api/watches/{id}/alerts` | Alerts for a specific watch | Optional | 60/min |

### WebSocket Endpoints

| Endpoint | Description | Protocol |
|----------|-------------|----------|
| `/ws/search` | Streaming OSINT search results | Send `{"target": "...", "type": "..."}` → receive `start`/`result`/`complete` messages |
| `/ws/threats` | Live threat feed for map | Receive `initial_state` → continuous `attack_vector`/`threat_event`/`news_event` messages. Client can send `pause`/`resume`/`stop`. |

### WebSocket /ws/search Protocol

```
Client → Server:  {"target": "example.com", "type": "domain"}  (type is optional)
Server → Client:  {"type": "start", "total": 14, "plugins": [{"plugin_id": "...", "plugin_name": "...", "category": "..."}]}
Server → Client:  {"type": "result", "result": {...}, "completed": 1, "total": 14}  × N times
Server → Client:  {"type": "complete", "total": 14, "completed": 14}
Server → Client:  {"type": "error", "message": "..."}  (on failure)
```

### WebSocket /ws/threats Protocol

```
Server → Client:  {
                    "type": "initial_state",
                    "events": [attack_vector | news_event, ...],
                    "cities": [{name, lat, lng, risk, assetCount, activeThreats}, ...],
                    "timestamp": "..."
                  }
Server → Client:  {"type": "attack_vector", "id": "...", "from": "China", "fromLat": 35.86, "fromLng": 104.19, "to": "Mumbai", "toLat": 19.07, "toLng": 72.87, "attackType": "Phishing", "severity": "critical", "sourceIp": "1.2.3.4", ...}
Server → Client:  {"type": "news_event", "id": "...", "text": "...", "url": "...", "severity": "medium", ...}
Client → Server:  {"action": "pause"}  or  {"action": "resume"}  or  {"action": "stop"}
```

### API Request/Response Examples

**POST /api/search**

```bash
curl -X POST http://localhost:8000/api/search \
  -H "Content-Type: application/json" \
  -d '{"target": "example.com"}'
```

Response:
```json
{
  "target": "example.com",
  "type": "domain",
  "timestamp": "2025-01-15T10:30:00Z",
  "total_plugins": 14,
  "completed_plugins": 12,
  "results": [
    {
      "plugin_id": "domain-record",
      "plugin_name": "Domain Record",
      "category": "infrastructure",
      "target": "example.com",
      "status": "completed",
      "freshness": "moments",
      "gui_data": {
        "Domain": "example.com",
        "Registrar": "Example Registrar Inc",
        "Created": "2000-01-01T00:00:00Z",
        "Expires": "2030-01-01T00:00:00Z"
      },
      "terminal_data": "..."
    }
  ]
}
```

**GET /api/detect**

```bash
curl "http://localhost:8000/api/detect?target=user@example.com"
```

```json
{
  "target": "user@example.com",
  "detected_type": "email",
  "confidence": 1.0
}
```

### Authentication

When `API_KEY` is set in `.env`, all `/api/search`, `/api/watch*`, and `/api/detect` endpoints require authentication. Provide the key via:

```
Authorization: Bearer <your_api_key>
# or
X-API-Key: <your_api_key>
# or (WebSocket only)
?api_key=<your_api_key>  (as query parameter)
```

Uses constant-time comparison (hmac.compare_digest) to prevent timing attacks.

### Rate Limiting

| Path | Limit | Window |
|------|-------|--------|
| `/api/search` | 10 requests | 60 seconds |
| `/ws/*` | 20 connections | 60 seconds |
| Everything else | 60 requests | 60 seconds |

Rate limit headers are returned on every response:
```
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1705314000
```

Rate-limited requests return HTTP 429 with a `Retry-After` header and error details.

<br/>

---

## 🧪 Running Tests

```bash
cd backend

# Run all 138+ tests
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov

# Run specific test file
pytest tests/test_watch_routes.py -v

# Run with verbose output
pytest tests/ -v --tb=long
```

### Test Coverage

| Test File | What It Tests |
|-----------|---------------|
| `test_api_key_auth.py` | API key validation, constant-time comparison, header extraction |
| `test_data_leaks.py` | Data Leaks plugin breach matching, XposedOrNot, LeakCheck parsing |
| `test_watch_routes.py` | Watch CRUD endpoints, validation, toggle |
| `test_watch_service.py` | Watch service CRUD operations, alert generation |
| `test_watch_alerts.py` | Alert creation, diff detection, summary generation |
| `test_watch_retry.py` | Watch task retry logic, SQLite lock handling |

<br/>

---

## 🗂️ Project Structure

```
trinetra/
├── backend/
│   ├── app/
│   │   ├── api/                        # REST + WebSocket routes
│   │   │   ├── routes.py               # Search, detect, plugins, target-intel
│   │   │   ├── websocket_routes.py     # /ws/search streaming
│   │   │   ├── threat_routes.py        # /ws/threats live feed
│   │   │   ├── watch_routes.py         # Watch CRUD + alerts
│   │   │   └── data_routes.py          # NCRB crime data, data source health
│   │   ├── core/                       # App core
│   │   │   ├── config.py               # Settings via pydantic-settings + .env
│   │   │   ├── detector.py             # Auto-detect target type (domain/IP/email/phone/name)
│   │   │   ├── sanitizer.py            # Input validation & sanitization
│   │   │   ├── rate_limiter.py         # In-memory sliding window rate limiter
│   │   │   └── api_key_auth.py         # API key authentication (constant-time)
│   │   ├── data/                       # Static data
│   │   │   └── ncrb_crime_data.py      # NCRB 2022 cyber crime statistics (23 states)
│   │   ├── models/
│   │   │   └── schemas.py              # Pydantic request/response models
│   │   ├── plugins/                    # 20 OSINT plugins (auto-discovered)
│   │   │   ├── base.py                 # Abstract base class (OSINTPlugin, PluginResult)
│   │   │   ├── registry.py             # Auto-discovery plugin registry
│   │   │   ├── infrastructure/         # 9 plugins: WHOIS, DNS, Port Scan, SSL, Subdomain,
│   │   │   │                           #   Geo IP, HTTP Headers, Name Servers, Tech Fingerprint
│   │   │   ├── threat/                 # 4 plugins: CVE Alerts, Data Leaks, Document Vault, OSINT Leak
│   │   │   └── advanced/               # 4 plugins: Deep Search, Live Feed, Social Radar, Surface Scan
│   │   ├── services/                   # Business logic services
│   │   │   ├── orchestrator.py         # Plugin orchestrator (parallel execution)
│   │   │   ├── threat_feed.py          # Live threat feed generator + broadcaster
│   │   │   ├── real_threat_service.py  # Real malicious IP fetcher (ThreatFox, Feodo, IPsum)
│   │   │   ├── real_news_service.py    # Real RSS news fetcher (4 feeds)
│   │   │   ├── watch_service.py        # Watch CRUD + alert service
│   │   │   ├── database.py             # Async SQLAlchemy + dual SQL backend (PG/SQLite)
│   │   │   └── telegram_bot.py         # Telegram OSINT bot service
│   │   ├── tasks/                      # Background task processing
│   │   │   ├── broker.py               # TaskIQ broker (Redis or in-memory)
│   │   │   ├── scheduler.py            # Watch scheduler (60-second loop)
│   │   │   └── watch_tasks.py          # Watch scan + change detection tasks
│   │   └── main.py                     # FastAPI app factory + lifespan
│   ├── tests/                          # 138+ unit tests
│   ├── Dockerfile                      # Multi-stage build (Python 3.11)
│   ├── init.sql                        # PostgreSQL schema initialization
│   └── requirements.txt                # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Map/IndiaMap.tsx        # Interactive India threat map with SVG animations
│   │   │   ├── SearchBar/SearchBar.tsx # Auto-detect search input
│   │   │   ├── ReportView/ReportView.tsx   # Plugin detail report
│   │   │   ├── FullReportView/FullReportView.tsx  # Full system intelligence report
│   │   │   ├── LiveFeed/LiveFeed.tsx       # Real-time events page
│   │   │   ├── WatchPanel/WatchPanel.tsx   # Watch management
│   │   │   ├── GraphView/GraphView.tsx     # Cytoscape relationship graph
│   │   │   ├── VectorDetailModal/VectorDetailModal.tsx # Attack vector details + report
│   │   │   ├── Sidebar/Sidebar.tsx         # Plugin status sidebar
│   │   │   ├── TargetIntelPanel/TargetIntelPanel.tsx  # Web + news intelligence
│   │   │   ├── DataSourcesPanel/DataSourcesPanel.tsx  # Data source health
│   │   │   ├── DashboardStats/DashboardStats.tsx  # Stats bar
│   │   │   ├── ScanProgress/ScanProgress.tsx  # Scan progress indicator
│   │   │   └── ToastNotification/ToastNotification.tsx  # Toast notifications
│   │   ├── store/
│   │   │   ├── AppContext.tsx           # Global app state (useReducer)
│   │   │   └── ThreatContext.tsx        # Live threat feed state
│   │   ├── types/index.ts               # TypeScript type definitions
│   │   ├── utils/
│   │   │   ├── api.ts                   # REST API client
│   │   │   ├── detectSearchType.ts      # Client-side type detection
│   │   │   ├── useWebSocket.ts          # WebSocket scan hook
│   │   │   ├── useThreatFeed.ts         # WebSocket threat feed hook
│   │   │   ├── wsUtils.ts              # WebSocket URL builder
│   │   │   ├── pluginMapper.ts          # API response → frontend types
│   │   │   ├── indiaStatesGeoJSON.ts    # India GeoJSON boundaries
│   │   │   └── india-states.geojson     # Raw GeoJSON data
│   │   ├── App.tsx                      # Root app component
│   │   ├── main.tsx                     # React entry point
│   │   └── styles.css                   # Complete dark-themed design system
│   ├── Dockerfile                       # Multi-stage build (Node → Nginx)
│   ├── nginx.conf                       # Nginx config (API proxy, SPA routing)
│   └── package.json
├── docker-compose.yml                   # Production compose (5 services)
├── docker-compose.override.yml          # Dev overrides (hot-reload mounts)
├── .env.example                         # Environment template
└── README.md
```

<br/>

---

## ⚙️ Configuration Reference

### Backend Configuration (.env)

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `TRINETRA OSINT API` | Application display name |
| `VERSION` | `1.0.0` | Application version |
| `DEBUG` | `false` | Enable debug mode (verbose logging, SSL warnings) |
| `DATABASE_URL` | `sqlite+aiosqlite:///./trinetra.db` | Database connection (SQLite for dev, PostgreSQL for prod) |
| `REDIS_URL` | `None` | Redis connection (e.g., `redis://redis:6379/0`) |
| `CORS_ORIGINS` | `["http://localhost:3000","http://localhost:5173"]` | Allowed CORS origins |
| `PLUGIN_TIMEOUT` | `30` | Per-plugin timeout in seconds |
| `TRUST_PROXY_HEADERS` | `false` | Enable when behind reverse proxy |
| `API_KEY` | `""` | Enable API key auth when set |
| `CACHE_TTL_DEFAULT` | `3600` | Default cache TTL in seconds |
| `CACHE_TTL_LONG` | `86400` | Long cache TTL in seconds |

### Database Backend Selection

The database backend is auto-selected based on `DATABASE_URL`:

| URL Pattern | Backend | Best For |
|-------------|---------|----------|
| `sqlite+aiosqlite:///./trinetra.db` | SQLite | Development, single-user |
| `postgresql+asyncpg://user:pass@host:5432/db` | PostgreSQL | Production, multi-user, Docker |

SQLite optimization: WAL journal mode + busy_timeout=30s + NullPool for concurrent access.

### PostgreSQL Production URL Format

```
DATABASE_URL=postgresql+asyncpg://trinetra:your_password@postgres:5432/trinetra
```

### Rate Limiting Tuning

The rate limiter is in-memory and configurable via the `RateLimitMiddleware` class:
- `/api/search`: 10 requests per 60 seconds
- `/ws/*`: 20 connections per 60 seconds
- Default: 60 requests per 60 seconds

<br/>

---

## 🔐 Authentication & Rate Limiting

### Authentication Modes

| API_KEY Setting | Behavior |
|-----------------|----------|
| Empty (`""`) | **Open access** — no authentication required (development mode) |
| Set (e.g., `API_KEY=my-secret-key`) | **Protected** — all search, watch, and detect endpoints require the key |

### Accepted Authentication Methods

1. **HTTP Header**: `Authorization: Bearer <key>`
2. **HTTP Header**: `X-API-Key: <key>`
3. **Query Parameter** (WebSocket only): `?api_key=<key>`
4. **WebSocket JSON** (/ws/search): `{"api_key": "<key>", "target": "..."}`

### Security Features

- **Constant-time comparison** (hmac.compare_digest) — prevents timing attacks
- **Input sanitization** — shell metacharacters and control characters are rejected
- **Security headers** — X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy, HSTS
- **Non-root Docker user** — backend runs as `appuser` with dropped capabilities
- **No-new-privileges** — container security option enabled
- **Rate limiting** — per-IP sliding window with transparent headers

<br/>

---

## 🚀 Performance

| Metric | Value |
|--------|-------|
| **OSINT Search (20 plugins)** | 10–15 seconds (parallel execution) |
| **Threat feed fetch interval** | Every 10 minutes |
| **Map animation refresh** | Every 8–12 seconds |
| **Watch scheduler check** | Every 60 seconds |
| **RSS news fetch interval** | Every 5 minutes |
| **API rate limit (search)** | 10 req/min per IP |
| **API rate limit (general)** | 60 req/min per IP |
| **Geo-location limit** | ~40 req/min (ip-api.com free tier) |
| **Max attack vectors stored** | 50 (rolling buffer) |
| **Max headlines stored** | 200 (rolling buffer) |
| **Unit tests** | **138+ passing** |

<br/>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- **Report bugs** — Open an issue with reproduction steps
- **Suggest features** — Open an issue with your idea
- **Add plugins** — New OSINT plugins welcome! See the base class in `backend/app/plugins/base.py`
- **Improve the map** — Better visualizations, new overlays, performance optimizations
- **Add data sources** — Integrate new threat intelligence feeds or APIs

### How to Add a New Plugin

1. Create a new `.py` file in the appropriate category directory under `backend/app/plugins/`
2. Subclass `OSINTPlugin` and implement the `run()` method
3. Set `plugin_id`, `name`, `category`, `description`, `input_types`, and `icon`
4. The plugin is **auto-discovered** and available instantly — no registration needed

```python
from app.plugins.base import OSINTPlugin, PluginResult

class MyNewPlugin(OSINTPlugin):
    plugin_id = "my-plugin"
    name = "My Plugin"
    category = "threat"  # infrastructure, threat, person, advanced
    description = "What this plugin finds"
    input_types = ["domain", "ip"]
    icon = "🔌"

    async def run(self, target: str) -> PluginResult:
        # Your OSINT logic here
        gui_data = {"key": "value"}
        terminal_data = "key: value"
        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data=gui_data,
            terminal_data=terminal_data,
        )
```

### Development Setup

```bash
# Backend (local)
cd backend
pip install -r requirements.txt
pip install pytest pytest-asyncio pytest-cov  # For testing
uvicorn app.main:app --reload

# Frontend (local)
cd frontend
npm install
npm run dev
```

<br/>

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

<br/>

---

<div align="center">
  <p>
    <b>Built with 🛡️ for India's cybersecurity community</b>
  </p>
  <p>
    <sub>TRINETRA — Open Source Intelligence for a safer digital India</sub>
  </p>
  <br/>
  <p>
    <a href="https://github.com/K921-cyber/trinetra/issues">Report Bug</a> ·
    <a href="https://github.com/K921-cyber/trinetra/issues">Request Feature</a> ·
    <a href="https://github.com/K921-cyber/trinetra">GitHub</a>
  </p>
</div>
