# Odoo x FLUX Lucknow Hackathon 2026 | Virtual Round

**Team Leader:** Jagmohan Singh Malhi (`JAGMOHAN`)  
**Evaluator:** Piyush Soni (`piso@odoo.com`) | GitHub: `piso-odoo`, `hackathon-odoo`  
**Duration:** 8 Hours (9:00 AM – 5:00 PM, Oct 31, 2026)  

## Demo Video
- **Video Link:** [Public Video Link - Submit by Oct 31, 5:30 PM]

---

# [Project Title]

## Problem Statement
[Selected on 31 Oct, 08:30 AM: 1-2 sentences on what problem this solves]

## Solution & Key Features
- **Core Feature:** [Primary flow]
- **3-Layer Validation:** Client + Server (Pydantic) + Database (PostgreSQL constraints)
- **Responsive UI:** Tested for 375px (mobile), 768px (tablet), and 1280px (desktop)

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React + Vite + Tailwind CSS (Responsive Design Tokens)
- **Database:** PostgreSQL (Local)
- **ORM / Migrations:** SQLAlchemy

##  [_ARCHITECTURE.md](_ARCHITECTURE.md)
 For Detailed architectural design decisions are system data flow diagram visit _ARCHITECTURE.md.

## Folder Structure
```text
OH_SUBMIT/
├── backend/
│   ├── app/
│   │   ├── core/          # DB connection & configuration
│   │   ├── models/        # SQLAlchemy ORM models (constraints, FKs)
│   │   ├── schemas/       # Pydantic v2 validation & response envelopes
│   │   ├── services/      # Business logic (Level 4 single responsibility)
│   │   ├── routes/        # Resource-oriented REST routers (Level 7)
│   │   └── main.py        # FastAPI entrypoint & CORS middleware
│   ├── scripts/           # Demo seed scripts & migrations
│   ├── requirements.txt   # Pinned backend dependencies
│   └── .env.example       # Local environment configuration template
├── frontend/
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Application screens
│   │   ├── services/      # Centralized API service with error interception
│   │   ├── App.jsx        # Root application layout
│   │   └── index.css      # Tailwind CSS tokens (375px, 768px, 1280px)
│   ├── tailwind.config.js # Responsive design tokens
│   ├── vite.config.js     # Dev server & /api reverse proxy
│   └── package.json
├── notes/                 # 8-level questionnaire & reference concepts
├── _ARCHITECTURE.md       # Comprehensive 8-level architectural reasoning
├── AGENTS.md              # 8-hour virtual round agent rules & evaluator rubric
└── README.md
```

## Setup & Local Run Instructions
```bash
# 1. Clone repository
git clone <repo-url>
cd OH_SUBMIT

# 2. Virtual environment setup
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install backend dependencies
pip install -r backend/requirements.txt

# 4. Database setup (PostgreSQL local)
# Update DATABASE_URL in backend/.env if needed
python -m backend.scripts.seed

# 5. Start Backend API
uvicorn backend.app.main:app --reload --port 8000

# 6. Start Frontend (in a separate terminal)
cd frontend
npm install
npm run dev
```

---
**Built by:** Jagmohan Singh Malhi
