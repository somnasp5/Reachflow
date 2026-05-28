import { Link } from "react-router-dom";

const steps = [
  {
    num: 1,
    accent: "#22d3ee",
    bg: "#0e1a2b",
    title: "Install Ollama",
    desc: "Install Ollama locally for AI email generation",
    content: (
      <div style={{ background: "#080a0e", border: "1px solid #151c28", borderRadius: 12, padding: "18px 22px" }}>
        <p style={{ fontSize: 13, color: "#64748b", marginBottom: 12 }}>Download Ollama from the official website:</p>
        <a href="https://ollama.com" target="_blank" rel="noreferrer" style={{ color: "#22d3ee", fontSize: 13, fontFamily: "'JetBrains Mono', monospace", textDecoration: "none", borderBottom: "1px solid #22d3ee44" }}>
          https://ollama.com ↗
        </a>
      </div>
    ),
  },
  {
    num: 2,
    accent: "#60a5fa",
    bg: "#0e1a2b",
    title: "Download LLM Model",
    desc: "Pull the local AI model used for generation",
    content: (
      <CodeBlock code="ollama run llama3.2:3b" />
    ),
  },
  {
    num: 3,
    accent: "#34d399",
    bg: "#0b1f18",
    title: "Configure API Keys",
    desc: "Setup Serper API for recruiter discovery",
    content: (
      <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
        <p style={{ fontSize: 13, color: "#64748b", marginBottom: 4 }}>Create a <code style={{ background: "#0f1623", color: "#22d3ee", padding: "2px 8px", borderRadius: 5, fontFamily: "JetBrains Mono, monospace", fontSize: 12 }}>.env</code> file inside <code style={{ background: "#0f1623", color: "#22d3ee", padding: "2px 8px", borderRadius: 5, fontFamily: "JetBrains Mono, monospace", fontSize: 12 }}>backend/</code></p>
        <CodeBlock code="SERPER_API_KEY=your_serper_api_key" />
        <div style={{ background: "#0e1a2b", border: "1px solid #1d3a5f", borderRadius: 12, padding: "14px 18px" }}>
          <div style={{ fontSize: 12, fontWeight: 700, color: "#38bdf8", marginBottom: 6 }}>How to get Serper API Key</div>
          <p style={{ fontSize: 12.5, color: "#475569", lineHeight: 1.75 }}>Visit <span style={{ color: "#22d3ee" }}>https://serper.dev</span>, create a free account, and copy your API key into the .env file.</p>
        </div>
      </div>
    ),
  },
  {
    num: 4,
    accent: "#a78bfa",
    bg: "#1a0e2b",
    title: "Paste Job Portal HTML",
    desc: "Add Naukri / Foundit / Internshala HTML",
    content: (
      <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
        <CodeBlock code="backend/sample.html" />
        <div style={{ background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 12, padding: "14px 18px" }}>
          <p style={{ fontSize: 13, color: "#64748b", lineHeight: 1.8 }}>Open a job portal page, inspect the page, copy the full HTML source, and paste it into <code style={{ color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", fontSize: 12 }}>sample.html</code>.</p>
        </div>
      </div>
    ),
  },
  {
    num: 5,
    accent: "#fb923c",
    bg: "#1f150a",
    title: "Start Backend Server",
    desc: "Run FastAPI + LangGraph backend",
    content: <CodeBlock code="uvicorn app.main:app --reload" />,
  },
  {
    num: 6,
    accent: "#f87171",
    bg: "#1f0a0a",
    title: "Start Frontend",
    desc: "Launch the React dashboard",
    content: <CodeBlock code="npm run dev" />,
  },
];

function CodeBlock({ code }) {
  return (
    <div style={{ background: "#050507", border: "1px solid #0f1420", borderRadius: 12, padding: "16px 20px", overflowX: "auto" }}>
      <pre style={{ margin: 0, fontFamily: "'JetBrains Mono', 'Fira Code', monospace", fontSize: 13, color: "#4ade80", lineHeight: 1.7 }}>{code}</pre>
    </div>
  );
}

const workflowSteps = [
  { icon: "🌐", title: "Parse HTML", desc: "Extracts companies and job roles from Naukri, Foundit, and Internshala HTML." },
  { icon: "🔍", title: "Find Emails", desc: "Uses Serper API + Google Search to discover real recruiter emails." },
  { icon: "🧠", title: "Research", desc: "AI researches company info to personalize outreach emails." },
  { icon: "✍️", title: "Generate", desc: "Ollama LLM generates personalized recruiter outreach emails." },
  { icon: "🚀", title: "Send", desc: "Edit content, attach resumes, and send via Gmail SMTP." },
];

const troubleshoot = [
  { accent: "#f87171", bg: "#1f0a0a", border: "#3b1a1a", title: "Gmail Authentication Failed", desc: "Ensure Google 2FA is enabled and App Password is correctly added to .env" },
  { accent: "#fbbf24", bg: "#1a1100", border: "#3b2a00", title: "No Recruiter Emails Found", desc: "Verify Serper API key and ensure recruiter/company information exists publicly." },
  { accent: "#60a5fa", bg: "#0e1a2b", border: "#1d3a5f", title: "Ollama Model Not Responding", desc: "Ensure Ollama is running locally and the llama3.2:3b model is downloaded." },
];

export default function SetupGuide() {
  return (
    <div style={{
      minHeight: "100vh",
      background: "#080809",
      color: "#e2e8f0",
      fontFamily: "'Inter', 'DM Sans', sans-serif",
      overflowX: "hidden",
    }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        .nav-link { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 500; transition: color 0.2s; }
        .nav-link:hover { color: #e2e8f0; }
        .btn-primary { background: #22d3ee; color: #020617; padding: 13px 28px; border-radius: 10px; font-weight: 700; font-size: 14px; text-decoration: none; display: inline-block; transition: all 0.2s; }
        .btn-primary:hover { background: #67e8f9; transform: translateY(-1px); }
        .btn-white { background: #f1f5f9; color: #0f172a; padding: 14px 36px; border-radius: 10px; font-weight: 700; font-size: 15px; text-decoration: none; display: inline-block; transition: all 0.2s; }
        .btn-white:hover { background: #fff; transform: translateY(-1px); }
        .step-card { background: #0d0f14; border: 1px solid #1a2030; border-radius: 18px; padding: 32px; transition: border-color 0.2s; }
        .step-card:hover { border-color: #22d3ee22; }
        .grid-bg { background-image: linear-gradient(#0e1a2b18 1px, transparent 1px), linear-gradient(90deg, #0e1a2b18 1px, transparent 1px); background-size: 48px 48px; }
        .glow-dot { width: 8px; height: 8px; border-radius: 50%; background: #22d3ee; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; box-shadow: 0 0 0 0 #22d3ee44; } 50% { opacity: 0.7; box-shadow: 0 0 0 6px #22d3ee00; } }
      `}</style>

      <div className="grid-bg" style={{ position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0 }} />

      {/* NAV */}
      <nav style={{ position: "sticky", top: 0, zIndex: 50, borderBottom: "1px solid #111827", background: "rgba(8,8,9,0.88)", backdropFilter: "blur(12px)" }}>
        <div style={{ maxWidth: 1200, margin: "0 auto", padding: "0 24px", height: 64, display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <div style={{ width: 38, height: 38, borderRadius: 10, background: "#22d3ee", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 900, fontSize: 18, color: "#020617", fontFamily: "JetBrains Mono, monospace" }}>P</div>
            <span style={{ fontSize: 18, fontWeight: 800, letterSpacing: "-0.02em", color: "#f1f5f9" }}>PlacementGPT</span>
          </div>
          <div style={{ display: "flex", gap: 32, alignItems: "center" }}>
            <Link to="/" className="nav-link">Home</Link>
            <Link to="/setup" className="nav-link" style={{ color: "#22d3ee" }}>Guide</Link>
            <Link to="/dashboard" className="nav-link">Dashboard</Link>
            <Link to="/dashboard" className="btn-primary" style={{ padding: "9px 20px", fontSize: 13 }}>Launch App</Link>
          </div>
        </div>
      </nav>

      {/* HERO */}
      <section style={{ maxWidth: 900, margin: "0 auto", padding: "90px 24px 60px", textAlign: "center", position: "relative", zIndex: 1 }}>
        <div style={{ display: "inline-flex", alignItems: "center", gap: 8, background: "#0e1a2b", border: "1px solid #1d3a5f", borderRadius: 100, padding: "7px 16px", marginBottom: 28 }}>
          <div className="glow-dot" />
          <span style={{ fontSize: 12, fontWeight: 600, color: "#38bdf8", fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.04em" }}>Complete Local AI Setup Guide</span>
        </div>
        <h1 style={{ fontSize: 60, fontWeight: 900, lineHeight: 1.05, letterSpacing: "-0.03em", color: "#f8fafc", marginBottom: 20 }}>
          Setup<br /><span style={{ color: "#22d3ee" }}>PlacementGPT</span>
        </h1>
        <p style={{ fontSize: 16, color: "#64748b", lineHeight: 1.8, maxWidth: 540, margin: "0 auto" }}>
          Configure Ollama, Serper API, LangGraph workflow, and the React frontend locally to start generating personalized recruiter outreach emails.
        </p>
      </section>

      {/* STEPS */}
      <section style={{ maxWidth: 860, margin: "0 auto", padding: "0 24px 80px", position: "relative", zIndex: 1 }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
          {steps.map((s) => (
            <div key={s.num} className="step-card">
              <div style={{ display: "flex", alignItems: "flex-start", gap: 20 }}>
                <div style={{ width: 52, height: 52, borderRadius: 14, background: s.bg, border: `1px solid ${s.accent}44`, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0, fontFamily: "JetBrains Mono, monospace", fontSize: 18, fontWeight: 700, color: s.accent }}>
                  {s.num}
                </div>
                <div style={{ flex: 1 }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
                    <span style={{ fontSize: 10, fontWeight: 700, color: s.accent, fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.1em", textTransform: "uppercase" }}>Step {s.num}</span>
                  </div>
                  <h2 style={{ fontSize: 20, fontWeight: 800, color: "#f1f5f9", letterSpacing: "-0.01em", marginBottom: 4 }}>{s.title}</h2>
                  <p style={{ fontSize: 13, color: "#475569", marginBottom: 20 }}>{s.desc}</p>
                  {s.content}
                </div>
              </div>
            </div>
          ))}

          {/* READY CARD */}
          <div style={{ background: "#0d0f14", border: "1px solid #22d3ee33", borderRadius: 18, padding: 40, position: "relative", overflow: "hidden", textAlign: "center" }}>
            <div style={{ position: "absolute", top: 0, left: "50%", transform: "translateX(-50%)", width: 200, height: 1, background: "linear-gradient(90deg, transparent, #22d3ee, transparent)" }} />
            <h2 style={{ fontSize: 36, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.02em", marginBottom: 16 }}>You're Ready 🚀</h2>
            <p style={{ fontSize: 14, color: "#64748b", lineHeight: 1.9, maxWidth: 500, margin: "0 auto 28px" }}>
              PlacementGPT can now scrape companies from job portals, discover recruiter emails, research companies, and generate personalized AI-powered outreach emails.
            </p>
            <Link to="/dashboard" className="btn-primary">Open Dashboard →</Link>
          </div>
        </div>
      </section>

      {/* WORKFLOW OVERVIEW */}
      <section style={{ background: "#050507", borderTop: "1px solid #0f1420", borderBottom: "1px solid #0f1420", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ maxWidth: 1100, margin: "0 auto" }}>
          <div style={{ marginBottom: 48 }}>
            <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>Under the Hood</div>
            <h2 style={{ fontSize: 38, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 12 }}>How PlacementGPT Works</h2>
            <p style={{ fontSize: 14, color: "#64748b", lineHeight: 1.8, maxWidth: 560 }}>A multi-agent LangGraph workflow automates recruiter discovery, company research, personalized outreach generation, and email delivery.</p>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 12 }}>
            {workflowSteps.map((s, i) => (
              <div key={i} style={{ background: "#0a0c10", border: "1px solid #151c28", borderRadius: 14, padding: "20px 16px", textAlign: "center", position: "relative" }}>
                <div style={{ fontSize: 28, marginBottom: 12 }}>{s.icon}</div>
                <div style={{ fontSize: 10, fontWeight: 700, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.08em", marginBottom: 6 }}>0{i + 1}</div>
                <div style={{ fontSize: 13, fontWeight: 700, color: "#f1f5f9", marginBottom: 8 }}>{s.title}</div>
                <p style={{ fontSize: 11.5, color: "#475569", lineHeight: 1.7 }}>{s.desc}</p>
                {i < 4 && <div style={{ position: "absolute", right: -8, top: "50%", transform: "translateY(-50%)", color: "#22d3ee44", fontSize: 16, fontWeight: 900 }}>›</div>}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CSV WORKFLOW */}
      <section style={{ maxWidth: 1100, margin: "0 auto", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 20, padding: "40px 44px" }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>CSV Upload</div>
          <h2 style={{ fontSize: 38, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 12 }}>CSV Outreach Workflow</h2>
          <p style={{ fontSize: 14, color: "#64748b", lineHeight: 1.8, marginBottom: 28, maxWidth: 560 }}>PlacementGPT supports recruiter CSV uploads for personalized AI outreach generation.</p>
          <CodeBlock code={`company_name,hr_name,email,position\nGoogle,Rahul,rahul@google.com,SWE Intern\nMicrosoft,Priya,priya@microsoft.com,SDE Intern`} />
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16, marginTop: 24 }}>
            {[
              { label: "Supported Features", accent: "#22d3ee", bg: "#0e1a2b", border: "#1d3a5f", items: ["Upload recruiter CSV files", "Editable custom AI prompts", "Company research personalization", "AI-generated outreach emails", "Gmail sending integration", "Resume / portfolio attachments"] },
              { label: "Use Cases", accent: "#a78bfa", bg: "#1a0e2b", border: "#3b1d6e", items: ["Placement outreach", "Internship applications", "Cold email automation", "Recruiter networking", "Founder outreach", "Freelance pitching"] },
            ].map((col, i) => (
              <div key={i} style={{ background: col.bg, border: `1px solid ${col.border}`, borderRadius: 14, padding: "20px 22px" }}>
                <div style={{ fontSize: 12, fontWeight: 700, color: col.accent, fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.06em", marginBottom: 14 }}>{col.label}</div>
                <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                  {col.items.map((item, j) => (
                    <div key={j} style={{ display: "flex", alignItems: "center", gap: 8, fontSize: 13, color: "#94a3b8" }}>
                      <span style={{ color: col.accent, fontSize: 12 }}>✓</span> {item}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* GMAIL SMTP */}
      <section style={{ background: "#050507", borderTop: "1px solid #0f1420", borderBottom: "1px solid #0f1420", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ maxWidth: 1100, margin: "0 auto" }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>Email Delivery</div>
          <h2 style={{ fontSize: 38, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 12 }}>Gmail SMTP Setup</h2>
          <p style={{ fontSize: 14, color: "#64748b", marginBottom: 40, lineHeight: 1.8, maxWidth: 500 }}>PlacementGPT supports direct email sending using Gmail SMTP integration.</p>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
            <div>
              <div style={{ fontSize: 13, fontWeight: 700, color: "#f1f5f9", marginBottom: 16 }}>Enable App Password</div>
              <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                {["Enable Google 2-Factor Authentication", "Open Google App Passwords", "Generate a Mail App Password", "Add credentials inside backend/.env"].map((step, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "center", gap: 14, background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 10, padding: "13px 16px" }}>
                    <div style={{ width: 24, height: 24, borderRadius: 7, background: "#0e1a2b", border: "1px solid #22d3ee33", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, fontWeight: 700, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", flexShrink: 0 }}>{i + 1}</div>
                    <span style={{ fontSize: 13, color: "#94a3b8" }}>{step}</span>
                  </div>
                ))}
              </div>
            </div>
            <div style={{ display: "flex", alignItems: "center" }}>
              <div style={{ width: "100%" }}>
                <CodeBlock code={`EMAIL_ADDRESS=yourgmail@gmail.com\n\nEMAIL_APP_PASSWORD=your_app_password`} />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* PROJECT STRUCTURE */}
      <section style={{ maxWidth: 1100, margin: "0 auto", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 20, padding: "40px 44px" }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>Architecture</div>
          <h2 style={{ fontSize: 38, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 28 }}>Project Structure</h2>
          <CodeBlock code={`backend/\n ├── app/\n │   ├── agents/\n │   ├── graph/\n │   ├── routes/\n │   ├── services/\n │   ├── models/\n │   └── main.py\n │\n ├── sample.html\n ├── .env\n │\nfrontend/\n ├── src/\n │   ├── pages/\n │   ├── components/\n │   └── App.jsx`} />
        </div>
      </section>

      {/* TROUBLESHOOTING */}
      <section style={{ background: "#050507", borderTop: "1px solid #0f1420", borderBottom: "1px solid #0f1420", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ maxWidth: 1100, margin: "0 auto" }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>Common Issues</div>
          <h2 style={{ fontSize: 38, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 36 }}>Troubleshooting</h2>
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {troubleshoot.map((t, i) => (
              <div key={i} style={{ background: t.bg, border: `1px solid ${t.border}`, borderRadius: 14, padding: "20px 24px", display: "flex", gap: 16, alignItems: "flex-start" }}>
                <div style={{ width: 6, height: 6, borderRadius: "50%", background: t.accent, marginTop: 6, flexShrink: 0 }} />
                <div>
                  <div style={{ fontSize: 14, fontWeight: 700, color: t.accent, marginBottom: 6 }}>{t.title}</div>
                  <p style={{ fontSize: 13, color: "#64748b", lineHeight: 1.75 }}>{t.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FINAL CTA */}
      <section style={{ maxWidth: 800, margin: "0 auto", padding: "100px 24px", textAlign: "center", position: "relative", zIndex: 1 }}>
        <div style={{ background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 24, padding: "60px 48px", position: "relative", overflow: "hidden" }}>
          <div style={{ position: "absolute", top: 0, left: "50%", transform: "translateX(-50%)", width: 240, height: 1, background: "linear-gradient(90deg, transparent, #22d3ee, transparent)" }} />
          <h2 style={{ fontSize: 42, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 16 }}>Start Automating Outreach</h2>
          <p style={{ color: "#475569", fontSize: 14, marginBottom: 36, lineHeight: 1.9, maxWidth: 420, margin: "0 auto 32px" }}>
            PlacementGPT combines AI agents, LangGraph workflows, recruiter discovery, personalized outreach, and Gmail automation into one intelligent platform.
          </p>
          <Link to="/dashboard" className="btn-primary" style={{ fontSize: 15, padding: "14px 36px" }}>Launch Dashboard →</Link>
        </div>
      </section>

      {/* FOOTER */}
      <footer style={{ borderTop: "1px solid #0f1420", background: "#050507", padding: "32px 24px" }}>
        <div style={{ maxWidth: 1200, margin: "0 auto", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <div style={{ width: 30, height: 30, borderRadius: 8, background: "#22d3ee", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 900, fontSize: 14, color: "#020617" }}>P</div>
            <div>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#f1f5f9" }}>PlacementGPT</div>
              <div style={{ fontSize: 11, color: "#334155", marginTop: 1 }}>AI Powered Placement Outreach Automation</div>
            </div>
          </div>
          <div style={{ fontSize: 11, color: "#334155", fontFamily: "JetBrains Mono, monospace" }}>React · FastAPI · LangGraph · Ollama · Serper</div>
        </div>
      </footer>
    </div>
  );
}