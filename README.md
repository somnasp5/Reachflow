
🚀 PlacementGPT

AI Powered Multi-Agent Placement Outreach Automation Platform

PlacementGPT is a full-stack AI workflow automation platform that:

parses job portal HTML
discovers recruiter emails
researches companies using Google Search
generates personalized outreach emails using local LLMs
supports CSV recruiter workflows
enables human-in-the-loop editing
sends emails directly using Gmail SMTP

Built using:

React
FastAPI
LangGraph
Ollama
Serper API
Gmail SMTP
✨ Features
🌐 Job Portal HTML Parsing

Supports:

Naukri
Foundit
Internshala

Extracts:

company names
job titles
recruiter information
🤖 Multi-Agent LangGraph Workflow

PlacementGPT uses a modular AI workflow architecture.

Agents:

Portal Detector Agent
HTML Scraper Agent
Recruiter Email Search Agent
Company Research Agent
Email Filtering Agent
AI Email Generator Agent
🔍 Recruiter Email Discovery

Uses:

Serper API
Google Search

Discovers:

HR emails
recruiter emails
careers emails
hiring emails

Includes:

email cleaning
spam filtering
email ranking
🧠 AI Personalized Outreach

Uses:

Ollama local LLMs
prompt engineering
company research

Generates:

personalized recruiter outreach
internship applications
placement outreach
cold emails
📄 CSV Outreach Workflow

Upload recruiter/company CSV files.

Supported columns:

company_name,hr_name,email,position
Google,Rahul,rahul@google.com,SWE Intern
Microsoft,Priya,priya@microsoft.com,SDE Intern

Features:

editable prompts
AI personalization
recruiter outreach generation
direct email sending
📬 Gmail SMTP Integration

Supports:

direct email sending
attachments
resume upload
portfolio upload

Frontend supports:

editable recruiter email
editable subject
editable AI-generated email body
📊 Modern Dashboard

Includes:

live workflow logs
accordion UI
workflow tabs
search/filter
copy buttons
send mail buttons
attachment uploads
real-time status updates
🏗️ Architecture
Frontend (React)
        ↓
FastAPI Backend
        ↓
LangGraph Workflow
        ↓
+-----------------------------+
| Portal Detection Agent      |
| HTML Scraper Agent          |
| Recruiter Search Agent      |
| Company Research Agent      |
| Email Filter Agent          |
| Email Generator Agent       |
+-----------------------------+
        ↓
Frontend Dashboard
        ↓
Gmail SMTP Email Sending
🧠 LangGraph Workflow
Workflow Steps
1. Portal Detection

Detects:

Naukri
Foundit
Internshala
2. HTML Parsing

Extracts:

company names
job titles
hiring information
3. Recruiter Discovery

Uses Google Search + Serper API to:

find HR emails
find recruiter emails
rank best emails
4. Company Research

Researches:

company overview
company activities
hiring context
5. AI Email Generation

Generates:

personalized outreach emails
context-aware recruiter messages
editable professional emails
6. Email Sending

Users can:

edit recruiter email
edit subject
edit email body
upload resume
send directly via Gmail
🛠️ Tech Stack
Frontend
React
React Router
Tailwind CSS
Backend
FastAPI
LangGraph
Python
AI/LLM
Ollama
Llama 3.2
Prompt Engineering
APIs
Serper API
Gmail SMTP
📂 Project Structure
PlacementGPT/
│
├── backend/
│   │
│   ├── app/
│   │   ├── agents/
│   │   ├── graph/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── parsers/
│   │   ├── models/
│   │   └── main.py
│   │
│   ├── sample.html
│   ├── temp_uploads/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   │
│   └── package.json
│
└── README.md
⚙️ Setup Guide
1. Clone Repository
git clone https://github.com/yourusername/PlacementGPT.git

cd PlacementGPT
2. Setup Backend
cd backend

Install dependencies:

pip install -r requirements.txt
3. Install Ollama

Download:

https://ollama.com
4. Download LLM
ollama run llama3.2:3b
5. Configure Environment Variables

Create:

backend/.env

Add:

SERPER_API_KEY=your_serper_key

EMAIL_ADDRESS=yourgmail@gmail.com

EMAIL_APP_PASSWORD=your_app_password
6. Gmail SMTP Setup
Enable 2FA

Google Account → Security → 2-Step Verification

Generate App Password

Google Account → App Passwords

Use generated password inside .env

7. Run Backend
uvicorn app.main:app --reload

Backend runs on:

http://localhost:8000
8. Setup Frontend
cd frontend

npm install
9. Run Frontend
npm run dev

Frontend runs on:

http://localhost:5173
🌐 HTML Workflow
Step 1

Open:

Naukri
Foundit
Internshala
Step 2

Inspect page source.

Copy complete HTML.

Step 3

Paste into:

backend/sample.html
Step 4

Open dashboard.

Click:

Generate Emails
📄 CSV Workflow

Upload recruiter CSV file.

Example:

company_name,hr_name,email,position
Google,Rahul,rahul@google.com,SWE Intern
Microsoft,Priya,priya@microsoft.com,SDE Intern

Then:

customize prompt
generate emails
edit emails
attach resume
send emails
📬 Email Sending

PlacementGPT supports:

direct Gmail SMTP sending
resume attachments
portfolio attachments

Features:

editable recipient email
editable subject
editable AI-generated content
📸 Dashboard Features
Live Workflow Logs

Real-time logs:

portal detection
recruiter discovery
email generation
workflow progress
Human-in-the-Loop Editing

Users can manually:

edit recruiter emails
edit AI output
change subject
add attachments
🔐 Security Notes
Never expose .env
Never commit API keys
Use Gmail App Passwords only
Do not use personal password directly
🚀 Future Improvements

Possible future upgrades:

streaming LLM responses
auto-email campaigns
recruiter CRM
PostgreSQL integration
authentication
background queues
analytics dashboard
follow-up email agents
vector database memory
RAG company memory
cloud deployment
🧪 Example Use Cases
placement outreach
internship applications
recruiter networking
startup outreach
cold emailing
freelance pitching
🎯 Resume Value

This project demonstrates:

AI workflow orchestration
LangGraph multi-agent systems
FastAPI backend engineering
React frontend engineering
local LLM integration
recruiter automation workflows
Gmail SMTP automation
prompt engineering
async frontend/backend communication
👨‍💻 Author
Ritik Saini

IIIT Bhubaneswar

Built using:

React
FastAPI
LangGraph
Ollama
Serper API
Gmail SMTP
📜 License

MIT License

⭐ If You Like This Project

Star the repository and share it with others 🚀
