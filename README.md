<div align="center">

<h1>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="40" />
  PlacementGPT
</h1>

<p><strong>AI-Powered Multi-Agent Placement Outreach Automation Platform</strong></p>

<p>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/LangGraph-FF6B35?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

<p>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/LLM-Llama_3.2-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Made%20by-Ritik%20Saini-blue?style=flat-square" />
</p>

<p><em>Parse job portals → Discover recruiter emails → Research companies → Generate personalized outreach → Send — all automated.</em></p>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [LangGraph Workflow](#-langgraph-workflow)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup Guide](#-setup-guide)
- [Usage Workflows](#-usage-workflows)
- [Dashboard Features](#-dashboard-features)
- [Security Notes](#-security-notes)
- [Future Improvements](#-future-improvements)
- [Use Cases](#-use-cases)
- [Author](#-author)
- [License](#-license)

---

## 🧭 Overview

**PlacementGPT** is a full-stack AI workflow automation platform built for placement and internship outreach. It combines multi-agent LangGraph pipelines, local LLMs via Ollama, and Gmail SMTP to automate the entire recruiter outreach process — from HTML parsing to personalized email delivery.

```
Parse Job Portal HTML  →  Discover Recruiter Emails  →  Research Company
         ↓                                                       ↓
  Generate AI Email   ←────────────────────────────────────────←
         ↓
  Human-in-the-Loop Editing  →  Send via Gmail SMTP
```

---

## ✨ Features

### 🌐 Job Portal HTML Parsing
- Supports **Naukri**, **Foundit**, and **Internshala**
- Extracts company names, job titles, and recruiter information from raw HTML

### 🤖 Multi-Agent LangGraph Workflow
Modular AI pipeline with 6 specialized agents:
| Agent | Responsibility |
|---|---|
| Portal Detector | Identifies the source portal |
| HTML Scraper | Extracts structured data from HTML |
| Recruiter Email Search | Discovers HR/recruiter emails via Google |
| Company Research | Fetches company context for personalization |
| Email Filter | Cleans, ranks, and deduplicates emails |
| AI Email Generator | Writes personalized outreach using local LLM |

### 🔍 Recruiter Email Discovery
- Powered by **Serper API** + Google Search
- Finds HR, recruiter, careers, and hiring emails
- Includes email cleaning, spam filtering, and ranking

### 🧠 AI Personalized Outreach
- Uses **Ollama** (Llama 3.2) running locally
- Context-aware email generation using company research
- Generates cold emails, internship applications, and placement outreach

### 📄 CSV Outreach Workflow
Upload a recruiter CSV and bulk-generate personalized emails:

```csv
company_name,hr_name,email,position
Google,Rahul,rahul@google.com,SWE Intern
Microsoft,Priya,priya@microsoft.com,SDE Intern
```

### 📬 Gmail SMTP Integration
- Send emails directly from the dashboard
- Attach resume and portfolio files
- Editable recipient, subject, and body before sending

### 📊 Modern Dashboard
- Live workflow logs with real-time status updates
- Accordion UI, workflow tabs, search & filter
- Copy buttons, send mail buttons, attachment uploads

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│              React Frontend             │
│  Dashboard │ HTML Workflow │ CSV Upload  │
└─────────────────┬───────────────────────┘
                  │ HTTP / REST
┌─────────────────▼───────────────────────┐
│           FastAPI Backend               │
│   Routes │ Services │ Parsers │ Models  │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         LangGraph Workflow Engine       │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  Portal Detection Agent         │    │
│  │  HTML Scraper Agent             │    │
│  │  Recruiter Email Search Agent   │    │
│  │  Company Research Agent         │    │
│  │  Email Filter Agent             │    │
│  │  AI Email Generator Agent       │    │
│  └─────────────────────────────────┘    │
└──────┬──────────────────────┬───────────┘
       │                      │
┌──────▼──────┐        ┌──────▼──────┐
│  Ollama LLM │        │  Serper API │
│ (Llama 3.2) │        │  (Google)   │
└─────────────┘        └─────────────┘
                  │
┌─────────────────▼───────────────────────┐
│           Gmail SMTP                    │
│     Direct email delivery with          │
│     resume/portfolio attachments        │
└─────────────────────────────────────────┘
```

---

## 🧠 LangGraph Workflow

```
[START]
   │
   ▼
[Portal Detection] ──────► Detects: Naukri / Foundit / Internshala
   │
   ▼
[HTML Parsing] ───────────► Extracts: Companies, Job Titles, Info
   │
   ▼
[Recruiter Discovery] ────► Google Search + Serper API → HR Emails
   │
   ▼
[Company Research] ───────► Overview, Activities, Hiring Context
   │
   ▼
[Email Filter] ───────────► Clean, Deduplicate, Rank Emails
   │
   ▼
[AI Email Generation] ────► Personalized Outreach via Ollama LLM
   │
   ▼
[Human-in-the-Loop] ──────► Edit Recipient / Subject / Body
   │
   ▼
[Gmail SMTP Send] ────────► Deliver with Resume Attachment
   │
   ▼
[END]
```

Each step is a discrete, replaceable LangGraph node — making the pipeline fully modular and extensible.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React, React Router, Tailwind CSS |
| **Backend** | FastAPI, Python, Uvicorn |
| **AI Workflow** | LangGraph |
| **Local LLM** | Ollama (Llama 3.2 3B) |
| **Search API** | Serper API |
| **Email** | Gmail SMTP |

---

## 📂 Project Structure

```
PlacementGPT/
│
├── backend/
│   ├── app/
│   │   ├── agents/          # LangGraph agent definitions
│   │   ├── graph/           # Workflow graph construction
│   │   ├── routes/          # FastAPI route handlers
│   │   ├── services/        # Business logic & integrations
│   │   ├── parsers/         # HTML portal parsers
│   │   ├── models/          # Pydantic data models
│   │   └── main.py          # FastAPI app entrypoint
│   │
│   ├── sample.html          # Paste job portal HTML here
│   ├── temp_uploads/        # Temporary file storage
│   ├── requirements.txt
│   └── .env                 # Environment variables (not committed)
│
├── frontend/
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/           # Dashboard, HTML, CSV pages
│   │   └── App.jsx          # Root component & routing
│   │
│   └── package.json
│
└── README.md
```

---

## ⚙️ Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PlacementGPT.git
cd PlacementGPT
```

### 2. Setup Backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. Install Ollama

Download from [https://ollama.com](https://ollama.com) and install for your OS.

### 4. Pull the LLM

```bash
ollama run llama3.2:3b
```

### 5. Configure Environment Variables

Create `backend/.env`:

```env
SERPER_API_KEY=your_serper_api_key
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
```

### 6. Gmail SMTP Setup

1. Enable **2-Step Verification** → [Google Account → Security](https://myaccount.google.com/security)
2. Generate an **App Password** → [Google Account → App Passwords](https://myaccount.google.com/apppasswords)
3. Use the generated 16-character password as `EMAIL_APP_PASSWORD` in `.env`

> ⚠️ Never use your regular Gmail password. App Passwords are required.

### 7. Run the Backend

```bash
uvicorn app.main:app --reload
# Runs at http://localhost:8000
```

### 8. Setup and Run Frontend

```bash
cd frontend
npm install
npm run dev
# Runs at http://localhost:5173
```

---

## 🖥️ Usage Workflows

### 🌐 HTML Workflow (Job Portal Scraping)

```
1. Open Naukri / Foundit / Internshala in your browser
2. Right-click → View Page Source → Copy all HTML
3. Paste into: backend/sample.html
4. Open the dashboard at http://localhost:5173
5. Click "Generate Emails"
6. Review → Edit → Send
```

### 📄 CSV Workflow (Bulk Outreach)

```
1. Prepare a CSV file with columns:
   company_name, hr_name, email, position

2. Upload via the dashboard CSV tab

3. Customize the AI prompt (optional)

4. Click "Generate Emails"

5. Edit individual emails as needed

6. Attach resume → Send
```

---

## 📊 Dashboard Features

| Feature | Description |
|---|---|
| **Live Workflow Logs** | Real-time updates: portal detection → email generation |
| **Accordion UI** | Expandable email cards per recruiter |
| **Human-in-the-Loop** | Edit recipient, subject, body before sending |
| **Attachment Upload** | Attach resume or portfolio per email |
| **Copy Buttons** | One-click copy of any generated email |
| **Send Buttons** | Direct Gmail SMTP sending from the UI |
| **Search & Filter** | Filter results by company or position |

---

## 🔐 Security Notes

- Never commit your `.env` file — add it to `.gitignore`
- Never expose your `SERPER_API_KEY` or `EMAIL_APP_PASSWORD` publicly
- Use Gmail **App Passwords only** — never your personal account password
- `temp_uploads/` should be excluded from version control

```gitignore
# Add to .gitignore
backend/.env
backend/temp_uploads/
```

---

## 🚀 Future Improvements

- [ ] Streaming LLM responses in the UI
- [ ] Auto email campaign scheduling
- [ ] Recruiter CRM with contact history
- [ ] PostgreSQL for persistent storage
- [ ] User authentication & multi-user support
- [ ] Background task queues (Celery / Redis)
- [ ] Analytics dashboard (open rates, responses)
- [ ] Follow-up email agents
- [ ] Vector database memory (RAG for company context)
- [ ] Cloud deployment (Docker + Railway / Render)

---

## 🧪 Use Cases

- 🎓 **Campus Placement Outreach** — bulk personalized emails to recruiters
- 🏢 **Internship Applications** — cold outreach to startup & corporate HRs
- 🤝 **Recruiter Networking** — professional first-touch emails
- 💼 **Freelance Pitching** — customized client outreach at scale
- 🚀 **Startup Outreach** — target hiring managers with company-specific context

---

## 🎯 What This Project Demonstrates

| Skill | Application |
|---|---|
| AI Workflow Orchestration | LangGraph multi-agent pipelines |
| Local LLM Integration | Ollama + Llama 3.2 |
| Backend Engineering | FastAPI, async Python |
| Frontend Engineering | React, Tailwind CSS |
| Prompt Engineering | Context-aware email generation |
| Email Automation | Gmail SMTP with attachments |
| Web Scraping | HTML parsing for job portals |
| API Integration | Serper API for recruiter discovery |

---

## 👨‍💻 Author

<div align="center">

**Ritik Saini**
IIIT Bhubaneswar

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ritik-sa0201/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/ritik-sa0201)

</div>

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If PlacementGPT helped you land an opportunity, star this repo and share it!**

*Built with React · FastAPI · LangGraph · Ollama · Serper API · Gmail SMTP*

</div>
