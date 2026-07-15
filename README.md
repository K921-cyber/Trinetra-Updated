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
    <img src="https://img.shields.io/badge/TypeScript-5.6-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript 5.6"/>
    <img src="https://img.shields.io/badge/Leaflet-1.9-199900?style=flat-square&logo=leaflet&logoColor=white" alt="Leaflet 1.9"/>
    <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"/>
    <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License"/>
  </p>
  <br/>
</div>

> **Search any domain, IP, email, phone, or name — get 360° threat intelligence in seconds.**
>
> TRINETRA is an all-in-one OSINT platform built for India. It combines **15 parallel OSINT plugins**, a **live threat feed** powered by real malicious IP data, **automated watch monitoring**, and an **interactive threat map dashboard**.

<br/>

<p align="center">
  <b>🔍 OSINT Search</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>🗺️ Live Threat Map</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>📡 Real-Time Feed</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>👁️ Watch Monitoring</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>📊 Professional Reports</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>🧠 Relationship Graphs</b>&nbsp;&nbsp;·&nbsp;&nbsp;
  <b>🔐 User Registration</b>
</p>

<br/>

---

## 📋 Table of Contents

- [⚡ Quick Start](#-quick-start)
- [🛠️ Manual Installation](#️-manual-installation)
- [🎯 What TRINETRA Does](#-what-trinetra-does)
- [🏗️ Architecture & Workflow](#️-architecture--workflow)
- [🔍 OSINT Search — How It Works](#-osint-search--how-it-works)
- [📡 Live Threat Feed](#-live-threat-feed)
- [👁️ Watch Monitoring](#️-watch-monitoring)
- [🗺️ Interactive Map](#️-interactive-map)
- [🔐 Authentication & User System](#-authentication--user-system)
- [📡 Real Data Sources](#-real-data-sources)
- [✨ Features](#-features)
- [📡 API Reference](#-api-reference)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Configuration Reference](#️-configuration-reference)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

<br/>

---

## ⚡ Quick Start

### Without Docker (Development)

**Terminal 1 — Backend:**
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8003 --reload
```

**Terminal 2 — Frontend:**
```bash
cd frontend
npm install
npx vite --host 0.0.0.0 --port 3000
```

**Terminal 3 — TaskIQ Worker (optional, for watch monitoring):**
```bash
cd backend
source venv/bin/activate
taskiq worker app.tasks.broker:broker app.tasks.watch_tasks
```

Then open **http://localhost:3000** — register a new account and start searching.

<br/>

---

## 🛠️ Manual Installation

### Prerequisites

- Python 3.11+
- Node.js 18+
- SQLite (included with Python) or PostgreSQL 15 (optional)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8003 --reload
```

The database (`trinetra.db`) and users table are created automatically on first startup. No `.env` file is required — the first user to register becomes an admin.

### Frontend Setup

```bash
cd frontend
npm install
npx vite --host 0.0.0.0 --port 3000
```

### Environment Variables (Optional)

All configuration can be done via environment variables or a `.env` file in the `backend/` directory:

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `TRINETRA OSINT API` | Application display name |
| `DEBUG` | `false` | Enable debug mode |
| `DATABASE_URL` | `sqlite+aiosqlite:///./trinetra.db` | Database connection string |
| `CORS_ORIGINS` | `["http://localhost:3000","http://localhost:5173"]` | Allowed CORS origins |
| `PLUGIN_TIMEOUT` | `30` | Per-plugin timeout in seconds |
| `HIBP_API_KEY` | `""` | Have I Been Pwned API key |
| `TELEGRAM_BOT_TOKEN` | `""` | Telegram Bot token |
| `TELEGRAM_OSINT_API_URL` | `""` | OSINT Leak API base URL |
| `TELEGRAM_OSINT_API_KEY` | `""` | API key for OSINT API |

<br/>

---

## 🎯 What TRINETRA Does

### The Problem

Investigating a single domain typically means juggling **multiple separate tools**:

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
┌─────────────────────────────────────────────────────────┐
│              One Search. 15 Plugins.                      │
│              Results in 10–15 seconds.                    │
└─────────────────────────────────────────────────────────┘
```

**Four independent systems running simultaneously:**

1. **🔍 On-Demand OSINT Search** — Run 15 parallel plugins against any target
2. **📡 Live Threat Feed** — Background loop fetching real malicious IPs and cyber news
3. **👁️ Watch Monitoring** — Automated re-scanning with change detection alerts
4. **🗺️ Interactive Threat Map** — Real-time India-focused attack visualization

<br/>

---

## 🏗️ Architecture & Workflow

```
                    ┌──────────────────────────────────────────┐
                    │   User's Browser (port 3000)              │
                    │   React 18 + TypeScript + Vite            │
                    │   Leaflet Map + Cytoscape Graphs          │
                    └──────────────┬──────────┬─────────────────┘
                                  HTTP       WebSocket
                                    │            │
                    ┌───────────────▼────────────▼─────────────┐
                    │         FastAPI Backend (port 8003)       │
                    │                                          │
                    │  ┌──────────┐  ┌────────────────────┐    │
                    │  │ REST API │  │ WebSocket Streaming│    │
                    │  │ /search  │  │ /ws/search         │    │
                    │  │ /auth/*  │  │ /ws/threats        │    │
                    │  │ /watch   │  └────────────────────┘    │
                    │  │ /plugins │                            │
                    │  └────┬─────┘                            │
                    │        │                                 │
                    │  ┌────▼─────────────────────────────┐    │
                    │  │    Plugin Orchestrator            │    │
                    │  │   ┌──────────┐ ┌──────────┐      │    │
                    │  │   │ 15 OSINT │ │ Watch    │      │    │
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
                    └──────────────────────────────────────────┘
```

### Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React 18 + TypeScript + Vite | Dashboard UI, map, reports, graphs, live feed, watch panel |
| **Mapping** | Leaflet + react-leaflet | India threat map with animated attack vectors |
| **Graphs** | Cytoscape + cytoscape-dagre | Relationship visualization from scan results |
| **Backend** | FastAPI + Python 3.11 | REST API + WebSocket server |
| **Database** | SQLite / PostgreSQL | Persistent storage (users, watches, alerts, scan results) |
| **Worker** | TaskIQ | Background watch task execution |
| **Data** | httpx + feedparser | External API calls + RSS parsing |
| **Bot** | python-telegram-bot | Telegram OSINT leak search (optional) |

<br/>

---

## 🔍 OSINT Search — How It Works

### Workflow

```
Target Query → Input Sanitizer → Auto-Detect Type → 15 Parallel Plugins → Stream Results
                      │                    │
                Control chars,        domain / IP /
                injection checks      email / phone / name
```

### Step-by-Step

1. **Input Sanitization** — Validated against maximum length, no control characters, null bytes, or shell metacharacters
2. **Auto-Detect Type** — Regex matching for IP, email, domain, phone; falls back to "name"
3. **Plugin Registry** — Auto-discovers all `OSINTPlugin` subclasses at startup
4. **Plugin Orchestration** — Fires matching plugins concurrently via `asyncio.gather` with 30s timeout
5. **WebSocket Streaming** — Results stream back in real-time as they complete

### The 15 OSINT Plugins

| Category | Plugin ID | Name | What It Finds | Input Types |
|----------|-----------|------|---------------|-------------|
| **Infrastructure** | `domain-record` | Domain Record | WHOIS registration, registrar info, creation/expiry dates | domain |
| | `name-servers` | Name Servers | DNS records: A, AAAA, MX, NS, CNAME, TXT, SOA | domain |
| | `port-scanner` | Port Scanner | Open TCP ports (24 common ports), service identification | domain, ip |
| | `ssl-health` | SSL Health | Certificate validity, cipher suites, protocol support, grade | domain |
| | `subdomain-finder` | Subdomain Finder | Subdomains via crt.sh, HackerTarget API, DNS brute-force (185+ prefixes) | domain |
| | `geo-locator` | Geo Locator | Server location, country, city, ISP, ASN, coordinates | domain, ip |
| | `http-headers` | HTTP Headers | Security headers (HSTS, CSP, XFO, etc.), server info, cookies | domain |
| | `tech-fingerprint` | Tech Fingerprint | Web server, frameworks, CMS, Cloudflare detection | domain |
| **Threat Intel** | `cve-alerts` | CVE Alerts | Known vulnerabilities from NVD API matching target | domain, ip |
| | `data-leaks` | Data Leaks | Breach data from XposedOrNot, LeakCheck, LeakIX + curated breach DB (70+ India-specific breaches) | domain, email, username |
| | `document-vault` | Document Vault | Exposed documents, .env, .git/config, backup files on common paths | domain |
| | `osint-leak` | OSINT Leak | Deep breach search via Leakosint API (email, phone, name, IP, username) | email, phone, username, name, ip |
| **Advanced** | `deep-search` | Deep Search | Google dorking queries for sensitive files, admin panels, backups | domain, name |
| | `live-feed` | Live Feed | Real-time cyber news from RSS feeds (The Hacker News) | domain, ip, name |
| | `surface-scan` | Surface Scan | Aggregated risk score, attack surface analysis, key port scanning | domain, ip |

### Performance

| Metric | Value |
|--------|-------|
| **Full scan (all matching plugins)** | 10–15 seconds |
| **Plugins run per search** | Up to 15 (depending on target type) |
| **API rate limit (search)** | 10 req/min per IP |
| **Plugin timeout** | 30 seconds (configurable) |

<br/>

---

## 📡 Live Threat Feed

### Background Services

#### 1. RealThreatService (Malicious IP Fetcher)

- **Interval**: Every 10 minutes
- **Sources**: Three free threat intelligence feeds in parallel
  - **ThreatFox** (Abuse.ch) — Malware IOCs
  - **Feodo Tracker** — C2 server IPs (Dridex, Emotet, QakBot)
  - **IPsum** — Blacklisted IPs with detection scores
- **Processing**: Parse IPs, geo-locate via ip-api.com, build attack vectors, cache results

#### 2. RealNewsService (RSS News Fetcher)

- **Interval**: Every 5 minutes
- **Sources**: The Hacker News, BleepingComputer, KrebsOnSecurity, The Record
- **Deduplication**: Up to 2,000 seen URLs tracked
- **Rolling buffer**: Max 200 headlines kept in memory

#### 3. ThreatFeedService (Broadcast Loop)

- **Interval**: Every 8–12 seconds per event
- **On connect**: Sends initial state with 20 recent vectors + 10 recent news headlines + city data
- **Subscriber model**: Each WebSocket connection gets a dedicated `asyncio.Queue`

### Data Transparency

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

## 👁️ Watch Monitoring

Create watches to automatically re-scan targets at configurable intervals and get alerts when data changes.

### Key Features

- **Configurable Intervals**: 5 minutes to 7 days
- **Plugin Selection**: Choose exactly which plugins run per watch
- **Smart Change Detection**: Compares `gui_data` JSON across scans — generates human-readable diffs
- **Alert History**: Full timeline of changes per watch target
- **Pause/Resume**: Toggle watches on/off without deleting them

### Retry Logic

On SQLite lock contention, watch tasks retry up to 3 times with exponential backoff (1s, 2s, 4s).

<br/>

---

## 🗺️ Interactive Map

### Map Architecture

```
IndiaMap (React Component)
├── MapContainer (Leaflet)
│   ├── TileLayer (CartoDB dark basemap)
│   ├── MapController (programmatic center/zoom)
│   ├── AnimatedAttackOverlay (SVG lines + traveling dots)
│   ├── CrimeHeatmap (GeoJSON state boundaries + NCRB)
│   ├── CityMarkers (10 major Indian cities, NCRB-risk)
│   └── DestinationPins (aggregated attack targets)
├── AttackCounter (live badge: critical/medium count)
├── AttackInfoPanel (severity bars, origin intel, table)
├── VectorDetailModal (full IP intel + report actions)
├── DataSourcesPanel (feed health status)
├── Map Controls (show/hide attacks, crime, data sources)
└── Legend (threat levels, data source colors)
```

### Animation System

Attack vectors are rendered as an **SVG overlay** using Leaflet's `L.svgOverlay`:

- **Dashed lines** from origin country coordinates to Indian city coordinates
- **Traveling dots** moving along the line with easing
- **Glow filter** for visual emphasis
- **10 FPS throttle** to optimize performance
- **Pauses animation when tab is hidden** (visibility API)
- **Shallow comparison** on vector IDs to avoid unnecessary rebuilds

### City Risk Markers

10 major Indian cities plotted with NCRB 2022 cyber crime statistics:
- **Color-coded circles**: Safe (green), Medium (yellow), Critical (red)
- **Pulsing animation** for critical destinations
- **Radius proportional** to risk level (7/10/14px)

<br/>

---

## 🔐 Authentication & User System

TRINETRA uses a **username/password registration system** with session tokens.

### How It Works

1. **First visit** — Login page appears with **Sign In** and **Register** tabs
2. **Register** — Create an account with username, email, and password
3. **First user becomes admin** — Subsequent users get the "user" role
4. **Auto-login** — After registration, you're automatically logged in
5. **Session tokens** — Stored in `localStorage`, verified on page reload
6. **Token expiry** — Tokens are valid until server restart or logout

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/auth/status` | Check if auth is enabled and registration is open |
| `POST` | `/api/auth/register` | Create a new account `{username, email, password}` |
| `POST` | `/api/auth/login` | Log in with credentials `{username, password}` |
| `POST` | `/api/auth/verify` | Check if a session token is still valid `{token}` |
| `POST` | `/api/auth/logout` | Invalidate the current session token |

### Authentication Methods

Once logged in, all API endpoints require the session token via:

```
X-API-Key: <your_session_token>
# or
Authorization: Bearer <your_session_token>
# or (WebSocket only)
?api_key=<your_session_token>  (as query parameter)
```

### Security Features

- **Password hashing** — SHA-256 with random 16-byte salt
- **Session tokens** — 32-byte cryptographically random hex strings
- **In-memory token store** — Tokens are cleared on server restart
- **Input validation** — Username regex, email format, minimum password length
- **Rate limiting** — Per-IP sliding window for all endpoints

<br/>

---

## 📡 Real Data Sources

All data in TRINETRA is **real** — no simulated or placeholder data.

### Threat Intelligence Feeds

| Source | Type | Data Provided | Key Required? |
|--------|------|---------------|---------------|
| [Abuse.ch ThreatFox](https://threatfox.abuse.ch/) | Malware IOCs | Malicious IPs, malware families, attack types | ❌ Free |
| [Feodo Tracker](https://feodotracker.abuse.ch/) | C2 Tracker | C2 server IPs, botnet malware (Dridex, Emotet, QakBot) | ❌ Free |
| [IPsum](https://github.com/stamparm/ipsum) | IP Blacklist | Blacklisted IPs with detection scores (1-7) | ❌ Free |
| [ip-api.com](https://ip-api.com/) | Geo-location | Country, city, lat/lon, ISP, org | ❌ Free |

### OSINT Plugins Data Sources

| Plugin | Source(s) | Key Required? |
|--------|-----------|---------------|
| Domain Record | WHOIS servers (direct TCP on port 43) | ❌ Free |
| Name Servers | dnspython (direct DNS resolution) | ❌ Free |
| Port Scanner | Built-in async TCP scanner (24 common ports) | ❌ Free |
| SSL Health | OpenSSL via socket (certificate chain, cipher, protocols) | ❌ Free |
| Subdomain Finder | crt.sh + HackerTarget API + DNS brute-force (185+ prefixes) | ❌ Free |
| Geo Locator | ip-api.com | ❌ Free |
| HTTP Headers | httpx (security headers analysis) | ❌ Free |
| Tech Fingerprint | httpx (server header, x-powered-by, cookie analysis) | ❌ Free |
| CVE Alerts | NVD API v2.0 | ❌ Free |
| Data Leaks | XposedOrNot + LeakCheck + LeakIX + curated breach DB | ❌ Free |
| Document Vault | httpx (12 common sensitive paths checked) | ❌ Free |
| OSINT Leak | leakosintapi.com | 🔑 API Key |
| Deep Search | Google dork query generation (manual execution) | ❌ Free |
| Live Feed | RSS (The Hacker News) via feedparser | ❌ Free |
| Surface Scan | Built-in async port scanner + risk analyzer | ❌ Free |

### RSS News Feeds

| Feed | Topic | Icon |
|------|-------|------|
| [The Hacker News](https://thehackernews.com/) | General cybersecurity | 📰 |
| [BleepingComputer](https://www.bleepingcomputer.com/) | Tech news + malware | 💻 |
| [KrebsOnSecurity](https://krebsonsecurity.com/) | In-depth security reporting | 🔒 |
| [The Record](https://therecord.media/) | Cyber crime + policy | 📝 |

### India-Specific Data

- **NCRB 2022** — Official cyber crime statistics for 23 Indian states/UTs
- **70+ curated India-specific data breaches** (Aadhaar, IRCTC, BigBasket, CoWIN, Truecaller, Jio, etc.)
- **India GeoJSON** — State boundaries for all states/UTs
- **City targeting** — 10 major Indian cities with NCRB-weighted attack distribution

<br/>

---

## ✨ Features

### 🔍 OSINT Search (15 Plugins)

| Category | Plugins | What They Find |
|----------|---------|----------------|
| **Infrastructure** | WHOIS, DNS Lookup, Port Scanner, SSL Health, Subdomain Finder, Geo Locator, HTTP Headers, Tech Fingerprint | Registrar info, A/MX/NS records, open ports, certificate validity, subdomains, geo-location, security headers, tech stack |
| **Threat Intel** | CVE Alerts, Data Leaks, Document Vault, OSINT Leak | Known vulnerabilities (NVD), breach data (LeakIX, XposedOrNot, LeakCheck), exposed documents, deep leak search |
| **Advanced** | Deep Search, Live Feed, Surface Scan | Google dork queries, risk scoring, real-time cyber news |

### 🗺️ Interactive India Threat Map

- Animated attack vectors with traveling dots from 25+ origin countries
- City risk markers based on NCRB 2022 cyber crime statistics
- Crime heatmap overlay with hover tooltips
- Threat intelligence panel with severity distribution
- Vector detail modal with AbuseIPDB, AlienVault, CERT-In report actions
- 10 FPS optimized animation (pauses when tab is hidden)

### 📡 Real-Time Threat Feed

- Live events timeline — filterable by All, Attacks, Events, or News
- Attack vector cards color-coded by severity
- Cyber news from 4 RSS feeds
- Vector detail modal with full IP intelligence

### 📊 Report & Graph Views

- **Report View** — Three modes: GUI (structured table), Terminal (raw output), Split (both)
- **Full Report** — Executive summary, threat landscape, watches & alerts, intelligence events
- **Relationship Graph** — Dynamic Cytoscape visualization with color-coded nodes
- **Export** — Save graphs to PNG, copy to clipboard

### 👁️ Watch & Monitoring

- Automated re-scanning from 5 minutes to 7 days
- Smart change detection with human-readable diffs
- Alert history with full timeline
- Plugin-level control per watch
- Pause/resume without data loss

### 🔐 User Authentication

- Username/password registration and login
- First user becomes admin
- Session tokens stored in localStorage
- All API endpoints require authentication

### 🛡️ India-Specific Intelligence

- NCRB 2022 cyber crime data for 23 states/UTs
- 70+ curated India-specific data breaches
- India GeoJSON map with state boundaries
- CERT-In incident reporting

<br/>

---

## 📡 API Reference

### Authentication Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/auth/status` | Check auth status + registration open | ❌ Public |
| `POST` | `/api/auth/register` | Register new user `{username, email, password}` | ❌ Public |
| `POST` | `/api/auth/login` | Log in `{username, password}` → session token | ❌ Public |
| `POST` | `/api/auth/verify` | Verify session token `{token}` | ❌ Public |
| `POST` | `/api/auth/logout` | Invalidate session token | ✅ Required |

### OSINT Search Endpoints

| Method | Endpoint | Description | Rate Limit |
|--------|----------|-------------|------------|
| `POST` | `/api/search` | Run OSINT scan on a target | 10/min |
| `GET` | `/api/search/{target}` | GET variant of search | 10/min |
| `GET` | `/api/detect?target=` | Auto-detect target type | 60/min |
| `GET` | `/api/plugins` | List all 15 OSINT plugins | 60/min |
| `GET` | `/api/target-intel?target=` | Web intelligence (DuckDuckGo + RSS) | 60/min |

### Watch Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/watches` | List all watches |
| `POST` | `/api/watches` | Create a watch |
| `GET` | `/api/watches/{id}` | Get watch details |
| `DELETE` | `/api/watches/{id}` | Delete a watch |
| `POST` | `/api/watches/{id}/toggle` | Pause/resume a watch |
| `GET` | `/api/watches/alerts` | Recent alerts (configurable limit) |
| `GET` | `/api/watches/{id}/alerts` | Alerts for a specific watch |

### Data Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/crime-data` | NCRB 2022 cyber crime data | ❌ Public |
| `GET` | `/api/health/sources` | Data source health status | ❌ Public |
| `GET` | `/health` | Backend health + plugin counts | ❌ Public |

### WebSocket Endpoints

| Endpoint | Description |
|----------|-------------|
| `/ws/search` | Streaming OSINT search results |
| `/ws/threats` | Live threat feed for map |

### WebSocket /ws/search Protocol

```
Client → Server:  {"target": "example.com", "type": "domain"}
Server → Client:  {"type": "start", "total": N, "plugins": [...]}
Server → Client:  {"type": "result", "result": {...}, "completed": X, "total": N}  × N times
Server → Client:  {"type": "complete", "total": N, "completed": N}
```

### WebSocket /ws/threats Protocol

```
Server → Client:  {"type": "initial_state", "events": [...], "cities": [...], "timestamp": "..."}
Server → Client:  {"type": "attack_vector", "id": "...", "from": "China", ...}
Server → Client:  {"type": "news_event", "id": "...", "text": "...", ...}
Client → Server:  {"action": "pause"} | {"action": "resume"} | {"action": "stop"}
```

### API Examples

**Register a user:**
```bash
curl -X POST http://localhost:8003/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "email": "admin@example.com", "password": "securepass123"}'
```

**Login:**
```bash
curl -X POST http://localhost:8003/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "securepass123"}'
```

**Run a search (with auth token):**
```bash
curl -X POST http://localhost:8003/api/search \
  -H "Content-Type: application/json" \
  -H "X-API-Key: <your_session_token>" \
  -d '{"target": "example.com"}'
```

**List plugins:**
```bash
curl -H "X-API-Key: <token>" http://localhost:8003/api/plugins
```

<br/>

---

## 🗂️ Project Structure

```
trinetra/
├── backend/
│   ├── app/
│   │   ├── api/                        # REST + WebSocket routes
│   │   │   ├── routes.py               # Auth (login/register), search, detect, plugins
│   │   │   ├── websocket_routes.py     # /ws/search streaming
│   │   │   ├── threat_routes.py        # /ws/threats live feed
│   │   │   ├── watch_routes.py         # Watch CRUD + alerts
│   │   │   └── data_routes.py          # NCRB crime data, source health
│   │   ├── core/                       # App core
│   │   │   ├── config.py               # Settings via pydantic-settings + .env
│   │   │   ├── detector.py             # Auto-detect target type
│   │   │   ├── sanitizer.py            # Input validation & sanitization
│   │   │   ├── rate_limiter.py         # In-memory sliding window rate limiter
│   │   │   └── api_key_auth.py         # User auth (register, login, tokens)
│   │   ├── data/
│   │   │   └── ncrb_crime_data.py      # NCRB 2022 cyber crime statistics
│   │   ├── models/
│   │   │   └── schemas.py              # Pydantic request/response models
│   │   ├── plugins/                    # 15 OSINT plugins (auto-discovered)
│   │   │   ├── base.py                 # Abstract base class (OSINTPlugin)
│   │   │   ├── registry.py             # Auto-discovery plugin registry
│   │   │   ├── infrastructure/         # 8 plugins
│   │   │   ├── threat/                 # 4 plugins
│   │   │   └── advanced/               # 3 plugins
│   │   ├── services/
│   │   │   ├── orchestrator.py         # Plugin orchestrator (parallel execution)
│   │   │   ├── threat_feed.py          # Live threat feed broadcaster
│   │   │   ├── real_threat_service.py  # Real malicious IP fetcher
│   │   │   ├── real_news_service.py    # Real RSS news fetcher
│   │   │   ├── watch_service.py        # Watch CRUD + alert service
│   │   │   ├── database.py             # Async SQLAlchemy (SQLite/PostgreSQL)
│   │   │   └── telegram_bot.py         # Telegram OSINT bot (optional)
│   │   ├── tasks/
│   │   │   ├── broker.py               # TaskIQ broker
│   │   │   ├── scheduler.py            # Watch scheduler
│   │   │   └── watch_tasks.py          # Watch scan + change detection
│   │   └── main.py                     # FastAPI app factory + lifespan
│   ├── tests/
│   ├── Dockerfile
│   ├── init.sql
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── LoginPage/              # Auth login + register form
│   │   │   ├── Map/IndiaMap.tsx        # Interactive India threat map
│   │   │   ├── SearchBar/SearchBar.tsx # Auto-detect search input
│   │   │   ├── ReportView/             # Plugin detail report
│   │   │   ├── FullReportView/         # Full system intelligence report
│   │   │   ├── LiveFeed/LiveFeed.tsx   # Real-time events page
│   │   │   ├── WatchPanel/             # Watch management
│   │   │   ├── GraphView/              # Cytoscape relationship graph
│   │   │   ├── VectorDetailModal/      # Attack vector details
│   │   │   ├── Sidebar/                # Plugin status sidebar
│   │   │   ├── DataSourcesPanel/       # Data source health
│   │   │   ├── DashboardStats/         # Stats bar
│   │   │   ├── ScanProgress/           # Scan progress indicator
│   │   │   └── ToastNotification/      # Toast notifications
│   │   ├── store/
│   │   │   ├── AppContext.tsx           # Global app state
│   │   │   ├── AuthContext.tsx          # Auth state + login/register/logout
│   │   │   └── ThreatContext.tsx        # Live threat feed state
│   │   ├── types/index.ts               # TypeScript type definitions
│   │   ├── utils/
│   │   │   ├── api.ts                   # REST API client
│   │   │   ├── detectSearchType.ts      # Client-side type detection
│   │   │   ├── useWebSocket.ts          # WebSocket scan hook
│   │   │   ├── useThreatFeed.ts         # WebSocket threat feed hook
│   │   │   ├── wsUtils.ts              # WebSocket URL builder
│   │   │   ├── pluginMapper.ts          # API response → frontend types
│   │   │   └── indiaStatesGeoJSON.ts    # India GeoJSON boundaries
│   │   ├── App.tsx                      # Root app component
│   │   ├── main.tsx                     # React entry point
│   │   └── styles.css                   # Complete dark-themed design system
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
├── docker-compose.yml
├── docker-compose.override.yml
└── README.md
```

<br/>

---

## ⚙️ Configuration Reference

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `TRINETRA OSINT API` | Application display name |
| `DEBUG` | `false` | Enable debug mode |
| `DATABASE_URL` | `sqlite+aiosqlite:///./trinetra.db` | Database connection |
| `CORS_ORIGINS` | `["http://localhost:3000","http://localhost:5173"]` | Allowed CORS origins |
| `PLUGIN_TIMEOUT` | `30` | Per-plugin timeout in seconds |
| `HIBP_API_KEY` | `""` | Have I Been Pwned API key |
| `TELEGRAM_BOT_TOKEN` | `""` | Telegram Bot token |
| `TELEGRAM_OSINT_API_URL` | `""` | OSINT Leak API base URL |
| `TELEGRAM_OSINT_API_KEY` | `""` | API key for OSINT API |

### Database Backend Selection

| URL Pattern | Backend | Best For |
|-------------|---------|----------|
| `sqlite+aiosqlite:///./trinetra.db` | SQLite | Development, single-user |
| `postgresql+asyncpg://user:pass@host:5432/db` | PostgreSQL | Production, multi-user |

<br/>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- **Report bugs** — Open an issue with reproduction steps
- **Suggest features** — Open an issue with your idea
- **Add plugins** — New OSINT plugins welcome! See the base class in `backend/app/plugins/base.py`
- **Improve the map** — Better visualizations, new overlays, performance optimizations

### How to Add a New Plugin

1. Create a new `.py` file in the appropriate category directory under `backend/app/plugins/`
2. Subclass `OSINTPlugin` and implement the `run()` method
3. Set `plugin_id`, `name`, `category`, `description`, `input_types`
4. The plugin is **auto-discovered** — no registration needed

```python
from app.plugins.base import OSINTPlugin, PluginResult

class MyNewPlugin(OSINTPlugin):
    plugin_id = "my-plugin"
    name = "My Plugin"
    category = "threat"  # infrastructure, threat, advanced
    description = "What this plugin finds"
    input_types = ["domain", "ip"]

    async def run(self, target: str) -> PluginResult:
        # Your OSINT logic here
        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data={"key": "value"},
            terminal_data="key: value",
        )
```

### Development Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8003

# Frontend
cd frontend
npm install
npx vite --host 0.0.0.0 --port 3000
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
