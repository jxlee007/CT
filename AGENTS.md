# Virtual Round Agent Rules (Oct 31, 8 hours, Solo)

## Event & Evaluator Profile
- **Event:** Odoo x FLUX Lucknow Hackathon '26 | Virtual Round (8 Hours)
- **Team Leader:** Jagmohan Singh Malhi (`JAGMOHAN`)
- **Evaluator:** Piyush Soni (`piso`)
  - **Email:** `piso@odoo.com`
  - **GitHub Usernames:** `piso-odoo`, `hackathon-odoo`
  - **Collaborator Deadline:** **31 Oct, 10:00 AM** (Add both GitHub handles / email)
- **Portal Link:** [Odoo Hackathon Portal](https://hackathon.odoo.com/)

---

## Official Evaluator Briefing: Core Philosophy & Scoring Rubric

> *"This hackathon isn't about coding fast. It's about approaching the chosen problem statement thoughtfully and then designing scalable, well-structured, and clear code... We are looking for someone with solid technical skills, logical thinking, and someone who can work on real-world, dynamic projects."*  
> — **Official Odoo Briefing**

### The 11 Evaluator Scoring Pillars
1. **Database Design (TOP PRIORITY):** Relational modeling, normalization, foreign keys, constraints, and query efficiency.
2. **Modularity & Architecture:** Clean boundaries, domain separation, and unidirectional dependencies.
3. **Logic & Coding Patterns:** Thoughtful solutions, clean algorithms, single responsibility.
4. **Coding Standards & Attention to Detail:** Plain readable code, no dead code, 2-minute comprehension rule.
5. **Front-End Design & UI Consistency:** Consistent design tokens/palette, states (loading, empty, error).
6. **Usability & Navigation Flow:** Intuitive menus, 3-click rule, clean spacing and layout.
7. **Robust Input Validation:** 3-layer validation, graceful error feedback (e.g. invalid email message).
8. **Performance & Scalability:** Zero N+1 queries, fast local queries, indexed lookups.
9. **Security:** Hashed credentials, input sanitization, server-side authorization checks.
10. **Debugging & Resilience:** Zero breaking crashes; edge cases caught gracefully.
11. **Grounded Technology:** Build from scratch; minimal 3rd-party APIs; deep understanding of all code (no blind copy-paste).

### Strictly Forbidden vs. Strictly Required
| Strictly Forbidden (Disqualifiers) | Strictly Required (Winning Patterns) |
|---|---|
| ❌ Firebase, Supabase, MongoDB Atlas, BaaS | ✅ Local PostgreSQL built from scratch |
| ❌ Static JSON for final solution | ✅ Dynamic data from DB via REST API |
| ❌ Heavy / fragile 3rd-party API reliance | ✅ Self-contained, offline-resilient local stack |
| ❌ Unvalidated inputs / raw crashes | ✅ 3-layer validation with friendly error feedback |
| ❌ Blind copy-paste AI / trendy gimmicks | ✅ Code you thoroughly understand and can defend |
| ❌ Mega-commit at hour 7.9 | ✅ Hourly semantic git commits |

---

## Official Schedule (31 Oct 2026)

| Wall Clock | Round Time | Milestone / Action |
|------------|------------|--------------------|
| **08:30 AM** | T - 0.5h | Problem statement selection on portal |
| **09:00 AM** | Hour 0.0 | **Coding starts** & submit GitHub repo URL on portal |
| **10:00 AM** | Hour 1.0 | **CRITICAL:** Add `piso-odoo`, `hackathon-odoo`, `piso@odoo.com` as repo collaborators |
| **02:00 PM** | Hour 5.0 | **STRICT FEATURE FREEZE** (no new features; hardening only) |
| **05:00 PM** | Hour 8.0 | **Coding ends** (final commit and push) |
| **05:30 PM** | Post-code | **Submit public demo video link** on portal |

---

## Core Rules (Non-negotiable)

### 1. Dynamic Data Only & Local Resilience
- No static JSON in frontend
- All data from local PostgreSQL via REST API
- Complete offline/local operation (zero external cloud dependencies)
- Seed script for demo data
- Refresh reflects changes instantly

### 2. Validation (3 Layers)
- **Client:** Required fields, formats, inline errors with friendly feedback (e.g., "Please enter a valid email address")
- **Server:** Pydantic/Zod validation, 400/422 HTTP codes
- **Database:** NOT NULL, UNIQUE, CHECK constraints, FKs

### 3. Clean UI
- Design tokens only (CSS vars)
- Responsive: 375px (phone), 768px (tablet), 1280px (desktop)
- Loading, empty, error states
- Consistent navigation (3-click rule, clean menu placement & spacing)

### 4. Git Discipline
- Commits every 1 hour (requirement)
- Clear messages: `feat(models): add booking`, `fix(validation): slot overlap`
- No mega-dumps at end

### 5. Code Quality & Architectural Discipline
- One job per function (single responsibility)
- Plain, readable code (2-minute rule)
- Comments only for "why", not "what"
- No dead code, debug logs, unused imports
- Understand code thoroughly; zero blind copy-paste
- Strict adherence to the **8-Level Universal Questionnaire** (`notes/questionaire.md`)

---

## Architectural Reasoning: 8-Level Questionnaire Protocol

The agent must reason and validate through the 8 levels of architectural thinking (`notes/questionaire.md`) in order ("4-8-12-16-20-24-28-32"). Never move forward to the next layer if an earlier question fails.

### Level 1: Project Understanding (09:00 - 09:30 AM)
1. **What problem does this solve?** (1 sentence: why does it exist?)
2. **Who uses it?** (User persona + specific operational need)
3. **What are the constraints?** (Time: 8h, PostgreSQL, single developer, responsive targets, offline capable)
4. **How do I measure success?** (3 measurable outcomes: e.g. zero validation leaks, instant refresh, 1 clean working flow)

### Level 2: Architecture Decisions (09:00 - 09:30 AM)
5. **What are my modules/domains?** (Clear domain separation, e.g., Auth, Catalog, Booking)
6. **How do modules communicate?** (Explicit API/interface contracts, NOT raw cross-table monkeypatching)
7. **What data does each module own?** (Strict table ownership per module)
8. **What are the dependencies?** (Unidirectional flow: Domain → UseCase → Adapter/DB)

### Level 3: Feature Implementation (09:30 AM - 02:00 PM)
9. **What is the happy path?** (Step-by-step: User Input → Processing/Validation → Persistent Output)
10. **What can go wrong?** (Identify top 3 edge cases + exact error handling strategy)
11. **Which layer does each piece live in?** (Domain = business rules, UseCase = orchestration, Adapter = DB/API)
12. **Can I test this without the full app?** (YES = decoupled; NO = refactor before proceeding)

### Level 4: Code Design (09:30 AM - 02:00 PM)
13. **What is the ONE job of this function?** (1 sentence; if 2 jobs, split immediately)
14. **What goes in? What comes out?** (Strict typed contracts for inputs and outputs)
15. **Does this function depend on DB/framework?** (YES = Adapter layer; NO = pure Domain/UseCase logic)
16. **Can I test this function alone?** (YES = modular; NO = inject dependencies)

### Level 5: Code Quality & Boundaries (02:00 PM - 04:30 PM)
17. **Is this function pure?** (Predictable: same input → same output without unexpected side effects)
18. **Does this violate module boundaries?** (No cross-module direct table mutation)
19. **If I renamed one module, would this break?** (Enforce loose coupling)
20. **Can someone else understand this in 2 minutes?** (Clear naming, minimal cognitive load)

### Level 6: Database Design (09:30 AM - 11:00 AM) — *EVALUATOR'S #1 PRIORITY*
21. **Is this normalized?** (No data duplication; single source of truth)
22. **Do I have foreign keys?** (Referential integrity enforced with `ON DELETE` policies)
23. **What indexes do I need?** (Index frequently filtered, joined, or sorted columns)
24. **Can I write the query without N+1?** (Eager load with JOINs; batch queries)

### Level 7: API Design (10:00 AM - 01:00 PM)
25. **Is this resource-oriented?** (Nouns not verbs: `/api/bookings`, not `/api/createBooking`)
26. **Am I using the right HTTP method?** (GET = read, POST = create, PATCH/PUT = update, DELETE = remove)
27. **Is my response contract consistent?** (Standard envelope: `{"data": ..., "error": null}`)
28. **What errors can happen?** (Accurate HTTP status codes: 400 Bad Request, 404 Not Found, 422 Validation Error, 500 Server Error)

### Level 8: Communication & Presentation (04:30 PM - 05:30 PM)
29. **Can I draw this in 30 seconds?** (Clean module boxes + data flow arrows)
30. **Can I explain the main decision in 1 sentence?** (E.g. "Used 3-layer validation with Pydantic and PostgreSQL constraints to guarantee zero corrupted records")
31. **What was my alternative? Why didn't I choose it?** (Document trade-off clearly in README)
32. **If I changed this, what breaks?** (Explicit blast radius understanding)

---

## Timeline & Phasing

| Clock Time | Phase | Questionnaire Level | Task |
|------------|-------|---------------------|------|
| **08:30 - 09:00 AM** | Scope Prep | Level 1 (Q1-Q4) | Select problem statement, define 1 core scope |
| **09:00 - 09:30 AM** | Arch Setup | Level 2 (Q5-Q8) | Submit repo URL, map modules, table ownership & models |
| **09:30 - 10:00 AM** | DB & Setup | Level 6 (Q21-Q24) | Schema migrations, seed script, add collaborators |
| **10:00 AM** | **CHECKPOINT** | - | **Verify `piso-odoo` & `hackathon-odoo` added on GitHub** |
| **10:00 - 02:00 PM** | Core Build | Levels 3, 4, 7 (Q9-Q16, Q25-Q28) | Build core feature: REST API → Responsive UI (375/768/1280px) |
| **02:00 PM** | **FREEZE** | - | **Feature freeze: zero new features** |
| **02:00 - 04:30 PM** | Hardening | Levels 4 & 5 (Q13-Q20) | 3-layer validation testing, edge cases, responsive checks, git log |
| **04:30 - 05:00 PM** | Final Polish | Level 8 (Q29-Q32) | README documentation, fresh clone verification, final commit |
| **05:00 - 05:30 PM** | Demo & Video | Level 8 | Record 2-3 min video, upload, submit video link on portal |

---

## Feature Scope Rule

**1 polished feature >> 5 half-baked features**

If behind schedule, cut:
1. Nice features (extras)
2. Beautiful CSS (focus on function)
3. Multiple views (use 1 clean view)

**NEVER cut:**
- Validation (3 layers)
- Git history (hourly commits)
- README & architecture reasoning
- Demo video

---

## Evaluation Checklist

- [ ] Dynamic data (local PostgreSQL, not static JSON)
- [ ] 3-layer validation with clear user error feedback
- [ ] Responsive UI (375px mobile + 768px tablet + 1280px desktop)
- [ ] Navigation: clean layout, intuitive menu spacing, 3-click rule
- [ ] Git: hourly commits, clear semantic messages
- [ ] Offline resilience: completely runnable locally (no BaaS/cloud)
- [ ] Database: normalized, foreign keys, indexes, no N+1
- [ ] API: resource-oriented, consistent responses, accurate HTTP codes
- [ ] Code: single responsibility, no blind copy-paste, no dead code
- [ ] Security: hashed secrets, server-side checks, input sanitization
- [ ] Demo video: 2-3 minutes, covers validation + responsive view

---

## If Stuck

1. **Validation error?** Check 3 layers (client, server, DB)
2. **UI not refreshing?** Fetch data from API, not state
3. **Architecture unclear?** Run the 8-Level Questionnaire from Level 1
4. **Git behind?** Commit hourly regardless
5. **Running out of time?** Cut features, not validation

---

## Demo Script (2-3 min)

1. **Open app (10 sec):** Show running app locally and clean interface
2. **Main flow (60 sec):** Happy path execution (Q9) with dynamic PostgreSQL updates
3. **Validation error (30 sec):** Trigger client, server, and DB error handling (Q10, Q28)
4. **Responsive view (30 sec):** Switch between 375px mobile, 768px tablet, and desktop view
5. **Architecture overview (30 sec):** Explain in 30 seconds using Level 8 (Q29-Q31)

---

## Final Submission Checklist

- [ ] Problem statement selected on portal (08:30 AM)
- [ ] GitHub repo URL submitted on portal (09:00 AM)
- [ ] Evaluators added as GitHub collaborators: `piso-odoo`, `hackathon-odoo` (`piso@odoo.com`) (by 10:00 AM)
- [ ] Repo set to **PUBLIC**
- [ ] Hourly commits visible in git log
- [ ] Fresh clone builds from README steps without cloud dependency
- [ ] README complete (setup, features, tech stack, architecture reasoning)
- [ ] Demo video: PUBLIC (YouTube / Drive accessible to anyone with link)
- [ ] Video link submitted on portal (by 05:30 PM)

---

**Built for:** Oct 31, 2026 | Odoo x FLUX Lucknow Hackathon Virtual Round
