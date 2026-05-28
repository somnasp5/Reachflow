import { Link } from "react-router-dom";
import { useEffect, useRef, useState } from "react";

const terminalLines = [
  { text: "➜ Detecting Naukri HTML...", delay: 0 },
  { text: "➜ Extracting Companies...", delay: 600 },
  { text: "➜ Searching Recruiter Emails...", delay: 1200 },
  { text: "➜ Researching Company Info...", delay: 1800 },
  { text: "➜ Generating Personalized Emails...", delay: 2400 },
  { text: "✓ Workflow Completed", delay: 3200, done: true },
];

function TerminalWidget() {
  const [visible, setVisible] = useState([]);
  useEffect(() => {
    terminalLines.forEach((line, i) => {
      setTimeout(() => setVisible((v) => [...v, i]), line.delay + 400);
    });
  }, []);
  return (
    <div style={{
      background: "#0a0a0b",
      borderRadius: "12px",
      padding: "20px",
      fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
      fontSize: "13px",
      lineHeight: "1.9",
      border: "1px solid #1e2030",
    }}>
      <div style={{ display: "flex", gap: "7px", marginBottom: "16px" }}>
        <div style={{ width: 11, height: 11, borderRadius: "50%", background: "#ff5f56" }} />
        <div style={{ width: 11, height: 11, borderRadius: "50%", background: "#ffbd2e" }} />
        <div style={{ width: 11, height: 11, borderRadius: "50%", background: "#27c93f" }} />
      </div>
      {terminalLines.map((line, i) => (
        <div
          key={i}
          style={{
            color: line.done ? "#22d3ee" : "#a8b4c8",
            opacity: visible.includes(i) ? 1 : 0,
            transform: visible.includes(i) ? "translateY(0)" : "translateY(6px)",
            transition: "opacity 0.4s ease, transform 0.4s ease",
            fontWeight: line.done ? "600" : "400",
          }}
        >
          {line.text}
        </div>
      ))}
    </div>
  );
}

const features = [
  { icon: "🌐", bg: "#0e1a2b", accent: "#1d4ed8", title: "Portal Parsing", desc: "Supports Naukri, Foundit, Internshala, and custom HTML parsing workflows." },
  { icon: "🔍", bg: "#0b1f18", accent: "#059669", title: "Recruiter Discovery", desc: "Uses Serper API and Google Search to find real recruiter emails." },
  { icon: "🤖", bg: "#1a0e2b", accent: "#7c3aed", title: "AI Email Generation", desc: "Personalized placement outreach emails generated using local Ollama models." },
  { icon: "📄", bg: "#1f150a", accent: "#d97706", title: "CSV Workflow", desc: "Upload recruiter databases directly and generate outreach emails instantly." },
];

const steps = [
  { icon: "🌐", title: "Parse Jobs", desc: "Extract companies from Naukri, Foundit, Internshala, or CSV files." },
  { icon: "🔍", title: "Find Recruiters", desc: "Discover real recruiter and HR emails via Serper + Google Search." },
  { icon: "🧠", title: "AI Research", desc: "Research company info and generate context-aware outreach." },
  { icon: "✍️", title: "Edit Emails", desc: "Modify recruiter email, subject, attachments, and AI content." },
  { icon: "🚀", title: "Send Instantly", desc: "Send personalized outreach via Gmail SMTP integration." },
];

const stack = [
  { name: "React", desc: "Modern interactive frontend with live workflow streaming." },
  { name: "FastAPI", desc: "High-performance backend APIs for orchestration." },
  { name: "LangGraph", desc: "Multi-agent workflow orchestration for automation." },
  { name: "Ollama", desc: "Local LLM powered personalized email generation." },
];

export default function LandingPage() {
  const heroRef = useRef(null);

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
        .nav-link { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 500; letter-spacing: 0.01em; transition: color 0.2s; }
        .nav-link:hover { color: #e2e8f0; }
        .btn-primary {
          background: #22d3ee;
          color: #020617;
          padding: 13px 28px;
          border-radius: 10px;
          font-weight: 700;
          font-size: 14px;
          text-decoration: none;
          display: inline-block;
          letter-spacing: 0.01em;
          transition: all 0.2s;
          border: none;
          cursor: pointer;
        }
        .btn-primary:hover { background: #67e8f9; transform: translateY(-1px); }
        .btn-secondary {
          background: transparent;
          color: #94a3b8;
          padding: 13px 28px;
          border-radius: 10px;
          font-weight: 600;
          font-size: 14px;
          text-decoration: none;
          display: inline-block;
          border: 1px solid #1e2a3a;
          transition: all 0.2s;
        }
        .btn-secondary:hover { border-color: #334155; color: #e2e8f0; background: #0f1623; }
        .feature-card {
          background: #0d0f14;
          border: 1px solid #1a2030;
          border-radius: 16px;
          padding: 28px;
          transition: all 0.3s;
          position: relative;
          overflow: hidden;
        }
        .feature-card::before {
          content: '';
          position: absolute;
          inset: 0;
          opacity: 0;
          border-radius: 16px;
          transition: opacity 0.3s;
          border: 1px solid #22d3ee33;
        }
        .feature-card:hover { transform: translateY(-4px); border-color: #22d3ee22; background: #0f1219; }
        .feature-card:hover::before { opacity: 1; }
        .step-card {
          background: #0a0c10;
          border: 1px solid #151c28;
          border-radius: 14px;
          padding: 24px;
          position: relative;
          text-align: center;
        }
        .stack-card {
          background: #0d0f14;
          border: 1px solid #1a2030;
          border-radius: 16px;
          padding: 28px;
          transition: border-color 0.2s;
        }
        .stack-card:hover { border-color: #22d3ee33; }
        .grid-bg {
          background-image: linear-gradient(#0e1a2b18 1px, transparent 1px), linear-gradient(90deg, #0e1a2b18 1px, transparent 1px);
          background-size: 48px 48px;
        }
        .glow-dot { width: 8px; height: 8px; border-radius: 50%; background: #22d3ee; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; box-shadow: 0 0 0 0 #22d3ee44; } 50% { opacity: 0.7; box-shadow: 0 0 0 6px #22d3ee00; } }
        .step-connector {
          position: absolute;
          right: -20px;
          top: 50%;
          transform: translateY(-50%);
          color: #22d3ee44;
          font-size: 20px;
          z-index: 10;
        }
      `}</style>

      {/* GRID BACKGROUND */}
      <div className="grid-bg" style={{ position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0 }} />

      {/* NAV */}
      <nav style={{
        position: "sticky", top: 0, zIndex: 50,
        borderBottom: "1px solid #111827",
        background: "rgba(8,8,9,0.88)",
        backdropFilter: "blur(12px)",
      }}>
        <div style={{ maxWidth: 1200, margin: "0 auto", padding: "0 24px", height: 64, display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <div style={{ width: 38, height: 38, borderRadius: 10, background: "#22d3ee", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 900, fontSize: 18, color: "#020617", fontFamily: "JetBrains Mono, monospace" }}>P</div>
            <span style={{ fontSize: 18, fontWeight: 800, letterSpacing: "-0.02em", color: "#f1f5f9" }}>PlacementGPT</span>
          </div>
          <div style={{ display: "flex", gap: 32, alignItems: "center" }}>
            <Link to="/" className="nav-link">Home</Link>
            <Link to="/setup" className="nav-link">Guide</Link>
            <Link to="/dashboard" className="nav-link">Dashboard</Link>
            <Link to="/dashboard" className="btn-primary" style={{ padding: "9px 20px", fontSize: 13 }}>Launch App</Link>
          </div>
        </div>
      </nav>

      {/* HERO */}
      <section ref={heroRef} style={{ maxWidth: 1200, margin: "0 auto", padding: "100px 24px 80px", position: "relative", zIndex: 1 }}>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 64, alignItems: "center" }}>

          {/* LEFT */}
          <div>
            <div style={{ display: "inline-flex", alignItems: "center", gap: 8, background: "#0e1a2b", border: "1px solid #1d3a5f", borderRadius: 100, padding: "7px 16px", marginBottom: 28 }}>
              <div className="glow-dot" />
              <span style={{ fontSize: 12, fontWeight: 600, color: "#38bdf8", fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.04em" }}>LangGraph + Ollama + Serper</span>
            </div>

            <h1 style={{ fontSize: 62, fontWeight: 900, lineHeight: 1.05, letterSpacing: "-0.03em", color: "#f8fafc", marginBottom: 24 }}>
              AI Powered
              <br />
              <span style={{ color: "#22d3ee" }}>Placement</span>
              <br />
              Outreach
            </h1>

            <p style={{ fontSize: 16, color: "#64748b", lineHeight: 1.8, maxWidth: 440, marginBottom: 36 }}>
              Automate recruiter discovery, company research, and personalized placement outreach emails using LangGraph AI agents, Ollama LLMs, and Google-powered recruiter search.
            </p>

            <div style={{ display: "flex", gap: 14, flexWrap: "wrap" }}>
              <Link to="/dashboard" className="btn-primary">Launch Dashboard →</Link>
              <Link to="/setup" className="btn-secondary">Setup Guide</Link>
            </div>

            {/* STATS */}
            <div style={{ display: "flex", gap: 0, marginTop: 52, borderTop: "1px solid #111827", paddingTop: 32 }}>
              {[
                { val: "AI", label: "Multi Agent Workflow" },
                { val: "CSV", label: "Recruiter Workflow" },
                { val: "LIVE", label: "Workflow Streaming" },
              ].map((s, i) => (
                <div key={i} style={{ flex: 1, paddingRight: 24, borderRight: i < 2 ? "1px solid #111827" : "none", paddingLeft: i > 0 ? 24 : 0 }}>
                  <div style={{ fontSize: 28, fontWeight: 900, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", letterSpacing: "-0.02em" }}>{s.val}</div>
                  <div style={{ fontSize: 12, color: "#475569", marginTop: 4, fontWeight: 500 }}>{s.label}</div>
                </div>
              ))}
            </div>
          </div>

          {/* RIGHT */}
          <div style={{ position: "relative" }}>
            {/* Floating badge top */}
            <div style={{ position: "absolute", top: -20, right: -12, zIndex: 20, background: "#0e1a2b", border: "1px solid #1d4ed8", borderRadius: 12, padding: "12px 20px" }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#60a5fa" }}>LangGraph</div>
              <div style={{ fontSize: 11, color: "#3b5a8a", marginTop: 2 }}>Multi-Agent Workflow</div>
            </div>

            {/* Main card */}
            <div style={{ background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 20, padding: 24, position: "relative", zIndex: 10 }}>
              <TerminalWidget />

              {/* Email preview */}
              <div style={{ marginTop: 16, background: "#080a0e", border: "1px solid #151c28", borderRadius: 12, padding: 18 }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 12 }}>
                  <div>
                    <div style={{ fontWeight: 700, fontSize: 15, color: "#f1f5f9" }}>Capgemini</div>
                    <div style={{ fontSize: 12, color: "#475569", marginTop: 2 }}>Analyst Programmer</div>
                  </div>
                  <div style={{ fontSize: 11, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", background: "#0e1a2b", border: "1px solid #1d4ed833", borderRadius: 6, padding: "4px 10px" }}>careers@capgemini.com</div>
                </div>
                <div style={{ fontSize: 12.5, color: "#64748b", lineHeight: 1.8 }}>
                  Dear Hiring Team,<br /><br />
                  We are reaching out from the Placement Coordination Team of IIIT Bhubaneswar regarding internship and placement opportunities for our 2026 batch students...
                </div>
              </div>
            </div>

            {/* Floating badge bottom */}
            <div style={{ position: "absolute", bottom: -20, left: -12, zIndex: 20, background: "#0a0c10", border: "1px solid #1a2030", borderRadius: 12, padding: "12px 20px" }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#a78bfa" }}>Ollama</div>
              <div style={{ fontSize: 11, color: "#4c3d6e", marginTop: 2 }}>Local LLM Generation</div>
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section style={{ maxWidth: 1200, margin: "40px auto 0", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ textAlign: "center", marginBottom: 60 }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 12 }}>Core Capabilities</div>
          <h2 style={{ fontSize: 44, fontWeight: 900, letterSpacing: "-0.025em", color: "#f8fafc", marginBottom: 16 }}>Everything Automated</h2>
          <p style={{ color: "#475569", fontSize: 15, maxWidth: 480, margin: "0 auto" }}>Built for placement coordinators, outreach teams, and AI automation workflows.</p>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 }}>
          {features.map((f, i) => (
            <div key={i} className="feature-card">
              <div style={{ width: 48, height: 48, borderRadius: 12, background: f.bg, border: `1px solid ${f.accent}33`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22, marginBottom: 20 }}>{f.icon}</div>
              <h3 style={{ fontSize: 16, fontWeight: 700, color: "#f1f5f9", marginBottom: 10 }}>{f.title}</h3>
              <p style={{ fontSize: 13, color: "#475569", lineHeight: 1.75 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* WORKFLOW */}
      <section style={{ maxWidth: 1200, margin: "0 auto", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ textAlign: "center", marginBottom: 60 }}>
          <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 12 }}>Pipeline</div>
          <h2 style={{ fontSize: 44, fontWeight: 900, letterSpacing: "-0.025em", color: "#f8fafc", marginBottom: 16 }}>End-to-End AI Outreach</h2>
          <p style={{ color: "#475569", fontSize: 15, maxWidth: 520, margin: "0 auto" }}>PlacementGPT automates the entire outreach pipeline from recruiter discovery to personalized email delivery.</p>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 12, alignItems: "center" }}>
          {steps.map((s, i) => (
            <div key={i} style={{ position: "relative" }}>
              <div className="step-card">
                <div style={{ fontSize: 28, marginBottom: 14 }}>{s.icon}</div>
                <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", marginBottom: 6, letterSpacing: "0.06em" }}>STEP {i + 1}</div>
                <h3 style={{ fontSize: 15, fontWeight: 700, color: "#f1f5f9", marginBottom: 8 }}>{s.title}</h3>
                <p style={{ fontSize: 12, color: "#475569", lineHeight: 1.7 }}>{s.desc}</p>
              </div>
              {i < 4 && (
                <div style={{ position: "absolute", right: -10, top: "50%", transform: "translateY(-50%)", color: "#22d3ee55", fontSize: 18, zIndex: 10, fontWeight: 900 }}>›</div>
              )}
            </div>
          ))}
        </div>
      </section>

      {/* TECH STACK */}
      <section style={{ background: "#050507", borderTop: "1px solid #0f1420", borderBottom: "1px solid #0f1420", padding: "80px 24px", position: "relative", zIndex: 1 }}>
        <div style={{ maxWidth: 1200, margin: "0 auto" }}>
          <div style={{ textAlign: "center", marginBottom: 60 }}>
            <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", letterSpacing: "0.12em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 12 }}>Tech Stack</div>
            <h2 style={{ fontSize: 44, fontWeight: 900, letterSpacing: "-0.025em", color: "#f8fafc", marginBottom: 16 }}>Built on Modern AI</h2>
            <p style={{ color: "#475569", fontSize: 15 }}>AI Agents + Workflow Orchestration + Automation</p>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 }}>
            {stack.map((s, i) => (
              <div key={i} className="stack-card">
                <div style={{ fontSize: 22, fontWeight: 900, color: "#f1f5f9", fontFamily: "JetBrains Mono, monospace", letterSpacing: "-0.02em", marginBottom: 4 }}>{s.name}</div>
                <div style={{ width: 32, height: 2, background: "#22d3ee", borderRadius: 2, marginBottom: 14 }} />
                <p style={{ fontSize: 13, color: "#475569", lineHeight: 1.75 }}>{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section style={{ maxWidth: 800, margin: "0 auto", padding: "100px 24px", textAlign: "center", position: "relative", zIndex: 1 }}>
        <div style={{ background: "#0d0f14", border: "1px solid #1a2030", borderRadius: 24, padding: "60px 48px", position: "relative", overflow: "hidden" }}>
          <div style={{ position: "absolute", top: 0, left: "50%", transform: "translateX(-50%)", width: 240, height: 1, background: "linear-gradient(90deg, transparent, #22d3ee, transparent)" }} />
          <h2 style={{ fontSize: 40, fontWeight: 900, color: "#f8fafc", letterSpacing: "-0.025em", marginBottom: 16 }}>Ready to Automate?</h2>
          <p style={{ color: "#475569", fontSize: 15, marginBottom: 36, lineHeight: 1.8 }}>Launch the dashboard and start automating your placement outreach with AI agents today.</p>
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