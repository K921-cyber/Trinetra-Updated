<div align="center">
  <br/>
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/OSINT-Platform-purple.svg" alt="OSINT">
  <br/><br/>
</div>

# 🛡️ TRINETRA — OSINT Intelligence Dashboard

> **An all-in-one Open Source Intelligence (OSINT) Dashboard built specifically for India.**  
> Search any domain, IP, email, phone number, or name — get comprehensive threat intelligence in seconds.

---

## 📋 Table of Contents

- [Why TRINETRA?](#-why-trinetra)
- [What Problem Does It Solve?](#-what-problem-does-it-solve)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Real Data Sources](#-real-data-sources)
- [Plugins (19 OSINT Tools)](#-plugins-19-osint-tools)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [API Endpoints](#-api-endpoints)
- [Performance](#-performance)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Why TRINETRA?

TRINETRA was built because existing OSINT tools have critical gaps for Indian cybersecurity researchers:

| Problem | TRINETRA's Solution |
|---------|-------------------|
| **Global tools ignore India-specific data** — No NCRB crime stats, no Indian breach database | Built-in NCRB 2022 cyber crime data + 70+ curated India-specific breaches (Aadhaar, IRCTC, CoWIN, etc.) |
| **No unified dashboard** — Using 19 separate tools is slow and cumbersome | One search triggers all 19 plugins in parallel — results stream in real-time |
| **Fake/placeholder data** — Many OSINT tools return simulated data when APIs fail | Every plugin returns real data from live sources (WHOIS, DNS, NVD, threat feeds, etc.) |
| **No Indian map visualization** — Attack vectors shown on global maps miss India context | India-focused map with state crime overlay, city risk markers, and animated attack vectors |
| **No automated monitoring** — Manual re-checks waste hours | Watch system automatically re-scans targets at configurable intervals and alerts on changes |

**TRINETRA was designed from the ground up for Indian cybersecurity professionals, researchers, and students.**

---

## 🔥 What Problem Does It Solve?

### The Problem
When investigating a domain like `hackhalt.org`, a security researcher traditionally needs to:

1. Go to a WHOIS lookup site → get registrar info
2. Open a DNS checker → get A, MX, NS records
3. Run `nmap` → scan ports
4. Check SSL certificate manually
5. Search for subdomains via crt.sh
6. Check Have I Been Pwned for data leaks
7. Browse NVD for CVEs
8. Read The Hacker News for recent threats
9. Geo-locate the server IP

**That's 9 different tools, websites, and terminals — taking 15-30 minutes.**

### TRINETRA's Solution
One search box. One click. **All 19 plugins run simultaneously in parallel.** Results stream back in 10-15 seconds.

---

## ⚙️ How It Works

```
                          ┌─────────────────────┐
                          │   User types query   │
                          │  (domain/IP/email/)  │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │   Auto-Detect Type   │
                          │  (domain, ip, email, │
                          │   phone, or name)    │
                          └──────────┬──────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
     ┌────────▼────────┐   ┌────────▼────────┐   ┌────────▼────────┐
     │  Infrastructure  │   │  Threat Intel   │   │  Person Recon   │
     │  9 plugins run   │   │  3 plugins run  │   │  3 plugins run  │
     │  in parallel     │   │  in parallel    │   │  in parallel    │
     └────────┬────────┘   └────────┬────────┘   └────────┬────────┘
              │                      │                      │
     ┌────────▼──────────────────────▼──────────────────────▼────────┐
     │               All results stream back via REST or WebSocket   │
     └─────────────────────────────┬────────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │     Results Displayed On:    │
                    │  ├─ Interactive India Map    │
                    │  ├─ Detailed Report View     │
                    │  ├─ Relationship Graph View  │
                    │  └─ Sidebar Plugin Status     │
                    └─────────────────────────────┘
```

### Real-Time Threat Feed (Separate from Search)

The system also runs a **continuous background loop** independent of user searches:

```
┌─────────────────────────────────────────────────────┐
│              Background Threat Feed Loop             │
│  (Runs every 10 minutes, independent of searches)    │
└─────────────────────────────────────────────────────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
  ┌────────────┐ ┌────────────┐ ┌────────────┐
  │  ThreatFox │ │    Feodo   │ │   IPsum    │
  │ (Malware   │ │ (C2 Botnet │ │ (Blacklist │
  │   IOCs)    │ │   IPs)     │ │   Scores)  │
  └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              ┌─────────────────┐
              │  Geo-locate IPs │
              │  (ip-api.com)   │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  Build Attack   │
              │  Vectors with   │
              │  Real Threat    │
              │  Metadata       │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  Broadcast via  │
              │  WebSocket to   │
              │  Connected      │
              │  Clients        │
              │  (every 8-12s)  │
              └─────────────────┘
```

The attack vectors shown on the map use **real malicious IPs** from threat intelligence feeds. The IPs, their origin countries, malware names, and attack types are all real — only the target city assignment is India-focused for visualization.

---

## ✨ Features

### 🔍 OSINT Search (19 Plugins)
- **One-click intelligence** — Search any domain, IP, email, phone, or name
- **Parallel execution** — All relevant plugins run simultaneously
- **Real-time streaming** — Results appear as each plugin completes
- **Auto-detect** — Automatically identifies the target type

### 🗺️ Interactive India Map
- **Attack vectors** — Animated lines showing real threats from 25+ countries targeting Indian cities
- **City risk markers** — Color-coded circles (green/yellow/red) based on NCRB crime statistics
- **Crime heatmap overlay** — Toggleable state-wise NCRB 2022 cyber crime data
- **Origin intelligence** — Live summary showing which countries are attacking and with what attack types
- **Connection status** — Real-time "LIVE" indicator when WebSocket is streaming

### 📊 Professional Report View
- **Structured GUI view** — Key-value table for each plugin's findings
- **Raw terminal output** — Detailed command-line style output
- **Split view** — See both GUI and terminal simultaneously
- **Export options** — Copy to clipboard, download as .txt, print as PDF
- **Search within results** — Filter findings in real-time

### 🧠 Relationship Graph
- **Dynamic visualization** — Auto-generated graph from search results
- **Color-coded nodes** — Infrastructure (cyan), Threat (red), Person (pink), etc.
- **Interactive** — Pan, zoom, select nodes for details
- **Export to PNG** — Save graphs for reports

### 👁️ Watch & Monitoring
- **Automated re-scanning** — Monitor targets at configurable intervals (5 min to 7 days)
- **Change detection** — Automatically detects and alerts on differences
- **Alert history** — Review all past changes with summaries
- **Plugin selection** — Choose which plugins run for each watch

### 📡 Live Threat Feed
- **Real-time events** — Attack vectors and news stream live via WebSocket
- **Cyber news** — Latest headlines from The Hacker News, BleepingComputer, KrebsOnSecurity, The Record
- **Filterable timeline** — Filter by all, attacks, events, or news
- **Expandable details** — Click any attack for full intelligence

### 🛡️ Data Sources Health Panel
- **Live status** — See health of ThreatFox, Feodo, IPsum, ip-api.com, RSS feeds
- **Metrics** — IP counts, geo-lookups, last fetch times
- **Error reporting** — See exactly which source is failing and why

---

## 🏗️ Architecture

### Docker Architecture (5 Containers)

```
┌─────────────────────────────────────────────────────────┐
│                   User's Browser (:3000)                 │
│                 React App + Leaflet Map                  │
└──────────────────────────┬──────────────────────────────┘
                           │ HTTP / WebSocket
                           ▼
┌─────────────────────────────────────────────────────────┐
│              nginx (Frontend, :80 → :3000)              │
│              Serves static React build                   │
│              Proxies /api/* and /ws/* to backend        │
└──────────────────────────┬──────────────────────────────┘
                           │ Proxy /api/*, /ws/*
                           ▼
┌─────────────────────────────────────────────────────────┐
│          FastAPI (Backend, :8000)                        │
│          ├─ REST API (/api/search, /api/watches, etc.)  │
│          ├─ WebSocket (/ws/search — streaming results)  │
│          ├─ WebSocket (/ws/threats — live threat feed)  │
│          ├─ Plugin Registry (19 OSINT plugins)          │
│          ├─ Orchestrator (parallel plugin execution)    │
│          └─ Background Scheduler (watch checks)         │
└──────────┬──────────────┬──────────────┬───────────────┘
           │              │              │
           ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  PostgreSQL  │ │    Redis     │ │   TaskIQ     │
│  (Database)  │ │   (Cache &   │ │   Worker     │
│  :5432       │ │    Queue)    │ │   (Watch     │
│              │ │   :6380      │ │    Tasks)    │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Container Breakdown

| Container | Technology | Purpose | Port |
|-----------|-----------|---------|------|
| **Frontend** | React 18 + TypeScript + Vite + Leaflet + Cytoscape | UI Dashboard — map, reports, graphs | `3000` |
| **Backend** | Python FastAPI + httpx + aiohttp + dnspython | REST API, WebSocket, plugin execution | `8000` |
| **Worker** | TaskIQ + (Redis InMemory) | Background watch task execution | — |
| **PostgreSQL** | Postgres 15 Alpine | Persistent storage (watches, alerts, scan history) | `5432` |
| **Redis** | Redis 7 Alpine | Task queue broker & result backend | `6380` |

### Data Flow

```
Search Flow:
  Browser → POST /api/search → Orchestrator → 19 plugins (parallel asyncio.gather) → Response

Streaming Search Flow:
  Browser → WebSocket /ws/search → Orchestrator → asyncio.as_completed → Stream results

Live Threat Feed:
  Background loop → Fetch ThreatFox/Feodo/IPsum CSVs (every 10 min) → Geo-locate IPs → 
  Build attack vectors → Broadcast via WebSocket /ws/threats (every 8-12s)

Watch Monitoring:
  Scheduler (every 60s) → Check due watches → Run scan → Compare with previous → 
  Create alert if changed
```

---

## 💻 Tech Stack

### Backend
| Technology | Purpose |
|-----------|---------|
| **Python 3.11+** | Core language |
| **FastAPI** | REST API + WebSocket framework |
| **Uvicorn** | ASGI server |
| **SQLAlchemy (async)** | Database ORM |
| **PostgreSQL** | Primary database |
| **SQLite (aiosqlite)** | Local development fallback |
| **Redis** | Task queue broker (production) |
| **TaskIQ** | Background task processing |
| **httpx** | Async HTTP client |
| **aiohttp** | Async HTTP (threat feed fetches) |
| **dnspython** | DNS record resolution |
| **feedparser** | RSS/Atom feed parsing |
| **Pydantic** | Data validation & settings |

### Frontend
| Technology | Purpose |
|-----------|---------|
| **React 18** | UI framework |
| **TypeScript** | Type safety |
| **Vite** | Build tool |
| **Leaflet** | Interactive map |
| **react-leaflet** | React bindings for Leaflet |
| **Cytoscape.js** | Relationship graph visualization |
| **CSS3** | Dark theme with CSS variables |

### Infrastructure
| Technology | Purpose |
|-----------|---------|
| **Docker Compose** | Orchestration |
| **Nginx** | Static file serving + reverse proxy |
| **PostgreSQL 15 Alpine** | Database |
| **Redis 7 Alpine** | Caching + queue |

---

## 📡 Real Data Sources

All data in TRINETRA is **real** — no simulated or placeholder data. Here's every source:

### 🔬 OSINT Search (19 Plugins)

| Data | Source | API Key? |
|------|--------|----------|
| **Domain WHOIS** | Direct TCP to `whois.verisign-grs.com`, `whois.pir.org`, `whois.nixiregistry.in`, etc. | ❌ Free |
| **Geo Location** | [ip-api.com](https://ip-api.com) | ❌ Free (45 req/min) |
| **DNS Records** | `dnspython` library — direct DNS resolution | ❌ Free |
| **Port Scan** | Direct TCP socket connections | ❌ Free |
| **SSL Certificate** | TLS handshake via Python `ssl` module | ❌ Free |
| **HTTP Headers** | HTTP GET via `httpx` | ❌ Free |
| **Tech Fingerprint** | Parsed from HTTP response headers | ❌ Free |
| **Subdomains** | [crt.sh](https://crt.sh) + [HackerTarget](https://hackertarget.com) API + DNS brute-force | ❌ Free |
| **Reverse DNS** | DNS PTR lookup | ❌ Free |
| **CVE Alerts** | [NVD API](https://nvd.nist.gov) | ❌ Free |
| **Data Leaks** | [XposedOrNot](https://xposedornot.com) + [LeakCheck](https://leakcheck.io) + [LeakIX](https://leakix.net) + Curated breach DB | ❌ Free |
| **Document Vault** | HTTP GET common paths (robots.txt, .env, etc.) | ❌ Free |
| **Live News** | RSS feeds: The Hacker News, BleepingComputer, KrebsOnSecurity, The Record | ❌ Free |
| **Social Radar** | HEAD requests to 8 social media platforms | ❌ Free |
| **Username Tracker** | HEAD requests to 9 platforms | ❌ Free |
| **Email Intelligence** | [EmailRep.io](https://emailrep.io) + Gravatar + 20 platform checks | ❌ Free |
| **Phone Intel** | Number pattern analysis + [NumLookup API](https://numlookupapi.com) (demo key) | ❌ Free |

### 🌐 Live Threat Feed (Map)

| Data | Source | How It Works |
|------|--------|-------------|
| **Malicious IPs** | [Abuse.ch ThreatFox](https://threatfox.abuse.ch) | CSV export, parsed every 10 min |
| **Botnet C2 IPs** | [Feodo Tracker](https://feodotracker.abuse.ch) | CSV export, parsed every 10 min |
| **Blacklisted IPs** | [IPsum](https://github.com/stamparm/ipsum) | TXT list, parsed every 10 min |
| **Geo-location** | [ip-api.com](https://ip-api.com) | Free API, 45 req/min |
| **Malware Names** | From threat feed metadata (Dridex, Emotet, QakBot, etc.) | Real names from CSVs |
| **Cyber News** | RSS: The Hacker News, BleepingComputer, KrebsOnSecurity, The Record | Fetched every 5 min |

### 🇮🇳 Reference Data

| Data | Source | Format |
|------|--------|--------|
| **NCRB Cyber Crime 2022** | [NCRB Crime in India Report](https://ncrb.gov.in) | 23 states/UTs with incident counts |
| **Indian Breach Database** | Curated from public sources | 70+ India-specific breaches |

---

## 🔌 Plugins (19 OSINT Tools)

### 🖥️ Infrastructure (9 plugins)

| Plugin | What It Does | Input Types |
|--------|-------------|-------------|
| **Domain Record** | WHOIS lookup — registrar, creation/expiry dates, name servers | domain |
| **Geo Locator** | Server location, ISP, ASN via ip-api.com | domain, ip |
| **Name Servers** | DNS records — A, AAAA, MX, NS, TXT, CNAME, SOA | domain |
| **Port Scanner** | TCP port scan — 24 common ports (21, 22, 80, 443, 3306, etc.) | domain, ip |
| **SSL Health** | Certificate validity, issuer, expiry, grade, cipher suite | domain |
| **HTTP Headers** | Security headers analysis — HSTS, CSP, X-Frame-Options, etc. | domain |
| **Tech Fingerprint** | Web server detection — Nginx, Apache, LiteSpeed, Cloudflare, PHP, ASP.NET | domain |
| **Subdomain Finder** | 3 sources: crt.sh + HackerTarget + DNS brute-force (150+ prefixes) | domain |
| **Reverse DNS** | PTR record lookup for IP addresses | ip |

### 🚨 Threat Intel (3 plugins)

| Plugin | What It Does | Input Types |
|--------|-------------|-------------|
| **CVE Alerts** | NVD vulnerability search matching target keywords | domain, ip |
| **Data Leaks** | 3 live APIs + 70+ curated India breaches (Aadhaar, IRCTC, CoWIN, etc.) | domain, email, username |
| **Document Vault** | Exposed document scan — robots.txt, .env, .git, backups, admin panels | domain |

### 👤 Person Recon (3 plugins)

| Plugin | What It Does | Input Types |
|--------|-------------|-------------|
| **Email Finder** | EmailRep.io + Gravatar + 20 platform registration checks (GitHub, Twitter, Spotify, Reddit, etc.) | email |
| **Phone Intel** | Carrier detection (Jio, Airtel, Vi, BSNL) + location inference + NumLookup API | phone |
| **Username Tracker** | 9 platform presence check (GitHub, Twitter, Instagram, Reddit, Medium, etc.) | username |

### 🔬 Advanced Scan (4 plugins)

| Plugin | What It Does | Input Types |
|--------|-------------|-------------|
| **Live Feed** | Real-time RSS news from The Hacker News | domain, ip, name |
| **Deep Search** | Google dork query generation (6 dork patterns) | domain, name |
| **Social Radar** | Social media presence check — 8 platforms | username, name, email |
| **Surface Scan** | Risk assessment + port analysis | domain, ip |

---

## 🚀 Quick Start

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac) or Docker Engine (Linux)
- [Git](https://git-scm.com/)

### Setup (2 Minutes)

```bash
# 1. Clone the repo
git clone https://github.com/K921-cyber/trinetra.git
cd trinetra

# 2. Create .env file (copy from template)
cp .env.example .env
# Edit .env — set POSTGRES_PASSWORD to a strong password

# 3. Start everything
docker compose up --build
```

### Access
- **Dashboard**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Quick Commands

```bash
# Start in background
docker compose up -d

# View logs
docker compose logs -f backend

# Rebuild backend (after code changes)
docker compose up -d --build backend

# Stop everything
docker compose down

# Reset database
docker compose down -v
```

### Local Development (Without Docker)

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

> **Note**: For local dev, set `DATABASE_URL=sqlite+aiosqlite:///./trinetra.db` in `.env` to use SQLite instead of PostgreSQL.

---

## 📖 Usage Guide

### Searching a Target

1. Open http://localhost:3000
2. Type a target in the search bar — domain, IP, email, phone, or name
3. The system auto-detects the target type and shows a badge
4. Press Enter or click "Scan"
5. Results stream in as each plugin completes (10-15 seconds)

**Examples:**
- `google.com` — Domain intelligence
- `8.8.8.8` — IP intelligence
- `security@gmail.com` — Email intelligence
- `+919876543210` — Phone intelligence
- `john_doe` — Username tracking

### Reading Results

| Feature | Location | How To |
|---------|----------|--------|
| **Plugin list** | Left sidebar | Shows all plugins with status dots (green=done, yellow=running, red=failed) |
| **Detailed report** | Click any plugin | Opens professional report with GUI/terminal/split views |
| **Relationship graph** | Map overlay button | Shows all findings as an interactive node graph |
| **Search within results** | In report view | Type to filter findings |

### Map Controls

| Button | Action |
|--------|--------|
| **Show/Hide Attacks** | Toggle animated attack vectors on the map |
| **Crime Data** | Toggle NCRB 2022 cyber crime state heatmap |
| **Data Sources** | Open live health panel for all intelligence feeds |
| **Graph View** | Open relationship graph overlay |
| **Reset View** | Zoom back to center of India |
| **Search [City]** | Run a search on the selected city |

---

## 🔌 API Endpoints

### REST API

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/search` | Run all OSINT plugins against a target | Optional |
| `GET` | `/api/search/{target}` | GET version of search | Optional |
| `GET` | `/api/detect` | Auto-detect target type | Optional |
| `GET` | `/api/plugins` | List all available plugins | Optional |
| `POST` | `/api/watches` | Create a new watch | Optional |
| `GET` | `/api/watches` | List all watches | Optional |
| `GET` | `/api/watches/{id}` | Get watch details | Optional |
| `DELETE` | `/api/watches/{id}` | Delete a watch | Optional |
| `POST` | `/api/watches/{id}/toggle` | Pause/resume a watch | Optional |
| `GET` | `/api/watches/alerts` | List recent alerts | Optional |
| `GET` | `/api/watches/{id}/alerts` | Alerts for a specific watch | Optional |
| `GET` | `/api/crime-data` | NCRB 2022 cyber crime data | ❌ Public |
| `GET` | `/api/health/sources` | Health of all data sources | ❌ Public |
| `GET` | `/health` | Backend health check | ❌ Public |

### WebSocket Endpoints

| Path | Purpose | Protocol |
|------|---------|----------|
| `/ws/search` | Stream scan results in real-time | Client sends `{"target": "..."}`, server streams `start → result → complete` |
| `/ws/threats` | Live threat feed for the map | Server sends `initial_state → attack_vector → news_event` continuously |

---

## ⚡ Performance

### Resource Usage

| Container | Typical CPU | Typical Memory | Memory Limit |
|-----------|-----------|---------------|-------------|
| Backend | ~12% | 180 MB | 1 GB |
| Frontend (Nginx) | ~0.03% | 16 MB | 256 MB |
| Worker | ~0.2% | 178 MB | 1 GB |
| Redis | ~0.8% | 7 MB | 256 MB |
| Postgres | ~2% | 37 MB | 512 MB |

### Optimizations Applied

| Optimization | Before | After |
|-------------|--------|-------|
| Map animation frame rate | 30 fps | 10 fps |
| SVG elements per attack vector | 5 (path, dot, ghost, pulse, source) | 3 (path, dot, source) |
| Background grid animation | Animated CSS (continuous GPU cycle) | Static |
| Threat broadcast frequency | Every 2-5 seconds | Every 8-12 seconds |
| Uptime counter updates | Every 1 second | Every 10 seconds |

### Scan Times (Typical)

| Target Type | Avg Time | Notes |
|-------------|----------|-------|
| Domain | 10-15s | 14 plugins |
| IP | 5-6s | 6 plugins |
| Email | 15-18s | 3 plugins (breach API latency) |
| Phone | ~5s | 1 plugin |

---

## 📁 Project Structure

```
trinetra/
├── backend/
│   ├── app/
│   │   ├── api/              # REST & WebSocket routes
│   │   │   ├── routes.py           # /api/search, /api/detect, /api/plugins
│   │   │   ├── websocket_routes.py # /ws/search, /ws/threats
│   │   │   ├── watch_routes.py     # /api/watches CRUD
│   │   │   ├── threat_routes.py    # /ws/threats (alt)
│   │   │   └── data_routes.py      # /api/crime-data, /api/health/sources
│   │   ├── core/              # Core services
│   │   │   ├── config.py           # Settings & env vars
│   │   │   ├── detector.py         # Target type auto-detection
│   │   │   ├── sanitizer.py        # Input validation & sanitization
│   │   │   ├── rate_limiter.py     # Per-IP rate limiting middleware
│   │   │   └── api_key_auth.py     # API key authentication
│   │   ├── data/              # Static data
│   │   │   └── ncrb_crime_data.py  # NCRB 2022 cyber crime stats
│   │   ├── models/
│   │   │   └── schemas.py          # Pydantic request/response models
│   │   ├── plugins/           # 19 OSINT plugins (auto-discovered)
│   │   │   ├── base.py             # OSINTPlugin abstract base class
│   │   │   ├── registry.py         # Plugin auto-discovery & registry
│   │   │   ├── infrastructure/     # 8 plugins (WHOIS, DNS, ports, SSL, etc.)
│   │   │   ├── threat/             # 4 plugins (CVEs, data leaks, docs, surface)
│   │   │   ├── person/             # 3 plugins (email, phone, username)
│   │   │   └── advanced/           # 4 plugins (deep search, social, live feed)
│   │   ├── services/          # Business logic
│   │   │   ├── orchestrator.py     # Parallel plugin execution
│   │   │   ├── database.py         # Async DB queries (PostgreSQL + SQLite)
│   │   │   ├── threat_feed.py      # Real-time threat event generator
│   │   │   ├── real_threat_service.py  # Threat feed fetcher (ThreatFox, Feodo, IPsum)
│   │   │   ├── real_news_service.py    # RSS news fetcher
│   │   │   └── watch_service.py    # Watch CRUD operations
│   │   └── tasks/             # Background tasks
│   │       ├── broker.py           # TaskIQ broker setup
│   │       ├── scheduler.py        # Periodic watch scheduler
│   │       └── watch_tasks.py      # Watch scan & alert tasks
│   ├── main.py                # FastAPI app entry point
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── init.sql               # Database schema
│   └── tests/                 # Test suite
├── frontend/
│   ├── src/
│   │   ├── App.tsx                 # Main app component
│   │   ├── main.tsx                # React entry point
│   │   ├── styles.css              # Global styles (dark theme)
│   │   ├── types/index.ts          # TypeScript type definitions
│   │   ├── store/                  # State management
│   │   │   ├── AppContext.tsx       # App state (search, results, UI)
│   │   │   └── ThreatContext.tsx    # Live threat feed state
│   │   ├── components/
│   │   │   ├── SearchBar/          # Search input with auto-detect
│   │   │   ├── Sidebar/            # Plugin status sidebar
│   │   │   ├── Map/IndiaMap.tsx    # India map with Leaflet
│   │   │   ├── ReportView/         # Professional report overlay
│   │   │   ├── GraphView/          # Cytoscape relationship graph
│   │   │   ├── LiveFeed/           # Real-time threat feed page
│   │   │   ├── WatchPanel/         # Watch & monitoring UI
│   │   │   ├── DashboardStats/     # Stats bar
│   │   │   ├── ScanProgress/       # Scan progress bar
│   │   │   ├── ToastNotification/  # Toast messages
│   │   │   ├── DataSourcesPanel/   # Health panel
│   │   │   ├── VectorDetailModal/  # Attack vector details
│   │   │   └── Icons/              # SVG icon components
│   │   └── utils/
│   │       ├── api.ts              # REST API client
│   │       ├── useWebSocket.ts     # Scan WebSocket hook
│   │       ├── useThreatFeed.ts    # Threat feed WebSocket hook
│   │       ├── pluginMapper.ts     # API→frontend data mapper
│   │       ├── mockData.ts         # Target type detection utility
│   │       ├── indiaStatesGeoJSON.ts  # India state boundaries
│   │       └── india-states.geojson   # GeoJSON data
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml
├── docker-compose.override.yml     # Dev hot-reload
├── .env.example                    # Environment template
├── .gitignore
└── CHANGELOG.md
```

---

## 🧪 Running Tests

```bash
# Run backend tests (inside container)
docker exec trinetra-backend python -m pytest tests/ -v

# Or from host (if local Python setup)
cd backend
python -m pytest tests/ -v
```

### Test Coverage

| Test File | What It Tests |
|-----------|--------------|
| `test_api_key_auth.py` | API key validation, header extraction, timing attack prevention |
| `test_data_leaks.py` | Data leak plugin — breach matching, API responses, edge cases |
| `test_watch_routes.py` | Watch CRUD endpoints, validation, error handling |
| `test_watch_service.py` | Database operations for watches & alerts |
| `test_watch_alerts.py` | Change detection diff logic, alert creation |
| `test_watch_retry.py` | SQLite lock contention retry logic |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run tests: `python -m pytest tests/ -v`
5. Commit: `git commit -m "Add my feature"`
6. Push: `git push origin feature/my-feature`
7. Open a Pull Request

### Adding a New Plugin

Creating a new OSINT plugin takes just one file:

```python
# backend/app/plugins/infrastructure/my_plugin.py
from app.plugins.base import OSINTPlugin, PluginResult

class MyPlugin(OSINTPlugin):
    plugin_id = "my-plugin"
    name = "My Plugin"
    category = "infrastructure"  # infrastructure, threat, person, or advanced
    description = "What this plugin does"
    input_types = ["domain"]  # domain, ip, email, phone, username, name
    icon = "🔌"

    async def run(self, target: str) -> PluginResult:
        # Your OSINT logic here
        return PluginResult(
            plugin_id=self.plugin_id,
            plugin_name=self.name,
            category=self.category,
            target=target,
            gui_data={"Finding": "Value"},
            terminal_data="Raw output",
        )
```

The plugin system auto-discovers new files — no registration needed.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

<div align="center">
  <strong>Made with ❤️ for Indian Cybersecurity Community</strong>
  <br/><br/>
  <sub>TRINETRA — त्रिनेत्र: The Third Eye for Cyber Intelligence</sub>
</div>
