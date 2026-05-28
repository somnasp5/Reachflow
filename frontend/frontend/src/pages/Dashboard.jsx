import { useState } from "react";
import Navbar from "../components/Navbar";

export default function Dashboard() {

  const [data, setData] = useState([]);
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [openIndex, setOpenIndex] = useState(null);
  const [activeTab, setActiveTab] = useState("html");
  const [search, setSearch] = useState("");
  const [csvFile, setCsvFile] = useState(null);
  const [attachments, setAttachments] = useState({});
  const [subjects, setSubjects] = useState({});
  const [sendingIndex, setSendingIndex] = useState(null);
  const [customPrompt, setCustomPrompt] = useState(`You are an AI outreach assistant.

Generate a highly professional and personalized outreach email.

The email should:
- sound human-written
- be concise and impactful
- personalize according to company background
- mention the role naturally
- avoid robotic wording
- maintain professional tone`);

  // =========================
  // COPY
  // =========================
  const copyText = (text) => {
    navigator.clipboard.writeText(text);
    alert("Copied!");
  };

  // =========================
  // ACCORDION
  // =========================
  const toggleAccordion = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  // =========================
  // SEND EMAIL
  // =========================
  const sendMail = async (item, index) => {
    try {
      setSendingIndex(index);
      const formData = new FormData();
      formData.append("receiver_email", item.company_email);
      formData.append("subject", subjects[index] || "Placement Opportunity from IIIT Bhubaneswar");
      formData.append("body", item.generated_email);
      if (attachments[index]) {
        formData.append("attachment", attachments[index]);
      }
      const response = await fetch("http://localhost:8000/send-email", { method: "POST", body: formData });
      const result = await response.json();
      if (result.success) {
        alert("Email Sent Successfully");
      } else {
        alert("Failed To Send Email");
      }
    } catch (err) {
      console.log(err);
      alert("Error Sending Email");
    } finally {
      setSendingIndex(null);
    }
  };

  // =========================
  // HTML WORKFLOW
  // =========================
  const startGeneration = async () => {
    try {
      setLoading(true);
      setLogs([]);
      setData([]);
      fetch("http://localhost:8000/run-placement-agent", { method: "POST" });
      const interval = setInterval(async () => {
        try {
          const logsRes = await fetch("http://localhost:8000/logs");
          const logsData = await logsRes.json();
          setLogs([...logsData.logs]);
          if (logsData.logs.includes("ALL TASKS COMPLETED")) {
            const resultRes = await fetch("http://localhost:8000/results");
            const resultData = await resultRes.json();
            setData(resultData.companies);
            setLoading(false);
            clearInterval(interval);
          }
        } catch (err) {
          console.log(err);
        }
      }, 1000);
    } catch (err) {
      console.log(err);
      setLoading(false);
    }
  };

  // =========================
  // CSV WORKFLOW
  // =========================
  const uploadCSV = async () => {
    if (!csvFile) {
      alert("Upload CSV First");
      return;
    }
    try {
      setLoading(true);
      setLogs([]);
      setData([]);
      setLogs([
        "Uploading CSV...",
        "Reading Recruiter Data...",
        "Researching Companies...",
        "Generating Personalized Emails..."
      ]);
      const formData = new FormData();
      formData.append("file", csvFile);
      formData.append("custom_prompt", customPrompt);
      const response = await fetch("http://localhost:8000/upload-csv", { method: "POST", body: formData });
      const result = await response.json();
      setData(result.companies);
      setLogs([
        "CSV Uploaded Successfully",
        "Company Research Completed",
        "Emails Generated Successfully"
      ]);
      setLoading(false);
    } catch (err) {
      console.log(err);
      setLoading(false);
    }
  };

  // =========================
  // FILTER
  // =========================
  const filteredData = data.filter(
    (item) =>
      item.company_name?.toLowerCase().includes(search.toLowerCase()) ||
      item.job_title?.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div style={{ minHeight: "100vh", background: "#080809", color: "#e2e8f0", fontFamily: "'Inter', 'DM Sans', sans-serif" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
        * { box-sizing: border-box; }
        .grid-bg { background-image: linear-gradient(#0e1a2b18 1px, transparent 1px), linear-gradient(90deg, #0e1a2b18 1px, transparent 1px); background-size: 48px 48px; }
        .glow-dot { width: 8px; height: 8px; border-radius: 50%; background: #22d3ee; animation: gdpulse 2s infinite; display: inline-block; }
        @keyframes gdpulse { 0%,100%{opacity:1;box-shadow:0 0 0 0 #22d3ee44}50%{opacity:.7;box-shadow:0 0 0 6px #22d3ee00} }
        .tab-btn { padding: 10px 24px; border-radius: 10px; font-size: 14px; font-weight: 600; cursor: pointer; border: 1px solid #1a2030; transition: all 0.2s; font-family: inherit; }
        .tab-active { background: #22d3ee; color: #020617; border-color: #22d3ee; }
        .tab-inactive { background: #0d0f14; color: #64748b; }
        .tab-inactive:hover { border-color: #22d3ee44; color: #94a3b8; }
        .card { background: #0d0f14; border: 1px solid #1a2030; border-radius: 18px; }
        .input-dark { width: 100%; background: #080a0e; border: 1px solid #1a2030; border-radius: 10px; padding: 12px 16px; color: #e2e8f0; font-size: 13px; font-family: inherit; outline: none; transition: border-color 0.2s; }
        .input-dark:focus { border-color: #22d3ee55; }
        .input-dark::placeholder { color: #334155; }
        .textarea-dark { width: 100%; background: #080a0e; border: 1px solid #1a2030; border-radius: 12px; padding: 14px 16px; color: #e2e8f0; font-size: 13px; font-family: 'JetBrains Mono', monospace; outline: none; resize: none; transition: border-color 0.2s; line-height: 1.7; }
        .textarea-dark:focus { border-color: #22d3ee55; }
        .file-input { width: 100%; background: #080a0e; border: 1px solid #1a2030; border-radius: 10px; padding: 12px 16px; color: #64748b; font-size: 13px; font-family: inherit; cursor: pointer; }
        .file-input::-webkit-file-upload-button { background: #0e1a2b; border: 1px solid #1d3a5f; color: #38bdf8; padding: 6px 14px; border-radius: 7px; font-size: 12px; font-weight: 600; cursor: pointer; margin-right: 12px; }
        .btn { padding: 10px 20px; border-radius: 9px; font-size: 13px; font-weight: 600; cursor: pointer; border: none; font-family: inherit; transition: all 0.2s; }
        .btn-cyan { background: #22d3ee; color: #020617; }
        .btn-cyan:hover { background: #67e8f9; }
        .btn-cyan:disabled { background: #1a2a2a; color: #334155; cursor: not-allowed; }
        .btn-blue { background: #1d4ed8; color: #fff; }
        .btn-blue:hover { background: #2563eb; }
        .btn-blue:disabled { background: #1a2030; color: #334155; cursor: not-allowed; }
        .btn-ghost { background: #0d0f14; color: #94a3b8; border: 1px solid #1a2030; }
        .btn-ghost:hover { border-color: #334155; color: #e2e8f0; }
        .btn-green { background: #065f46; color: #34d399; border: 1px solid #064e3b; }
        .btn-green:hover { background: #047857; }
        .btn-purple { background: #4c1d95; color: #a78bfa; border: 1px solid #3b0764; }
        .btn-purple:hover { background: #5b21b6; }
        .btn-purple:disabled { background: #1a2030; color: #334155; cursor: not-allowed; }
        .result-card { background: #0d0f14; border: 1px solid #1a2030; border-radius: 18px; overflow: hidden; transition: border-color 0.2s; }
        .result-card:hover { border-color: #22d3ee22; }
        .accordion-btn { width: 100%; padding: 24px 28px; background: transparent; border: none; cursor: pointer; display: flex; justify-content: space-between; align-items: center; transition: background 0.2s; font-family: inherit; }
        .accordion-btn:hover { background: #0a0c10; }
        .log-entry { background: #080a0e; border: 1px solid #0f1420; border-radius: 9px; padding: 10px 14px; font-size: 12.5px; color: #64748b; font-family: 'JetBrains Mono', monospace; }
        .log-entry.done { color: #22d3ee; border-color: #22d3ee22; }
        .stat-box { background: #080a0e; border: 1px solid #0f1420; border-radius: 12px; padding: 18px 20px; }
      `}</style>

      <div className="grid-bg" style={{ position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0 }} />

      <Navbar />

      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "40px 24px", position: "relative", zIndex: 1 }}>

        {/* HERO */}
        <div style={{ display: "flex", flexWrap: "wrap", gap: 32, justifyContent: "space-between", alignItems: "flex-start", marginBottom: 48 }}>
          <div>
            <div style={{ display: "inline-flex", alignItems: "center", gap: 8, background: "#0e1a2b", border: "1px solid #1d3a5f", borderRadius: 100, padding: "7px 16px", marginBottom: 20 }}>
              <div className="glow-dot" />
              <span style={{ fontSize: 12, fontWeight: 600, color: "#38bdf8", fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.04em" }}>AI Multi-Agent Workflow</span>
            </div>
            <h1 style={{ fontSize: 56, fontWeight: 900, letterSpacing: "-0.03em", color: "#f8fafc", lineHeight: 1.05, marginBottom: 16 }}>PlacementGPT</h1>
            <p style={{ fontSize: 15, color: "#64748b", lineHeight: 1.8, maxWidth: 520 }}>
              Generate personalized recruiter outreach emails using LangGraph, Ollama, Serper API, and AI-powered company research.
            </p>
          </div>

          {/* STATS */}
          <div className="card" style={{ padding: 28, width: 360, flexShrink: 0 }}>
            <div style={{ fontSize: 11, fontWeight: 700, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", letterSpacing: "0.1em", textTransform: "uppercase", marginBottom: 20 }}>Workflow Stats</div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
              <div className="stat-box">
                <div style={{ fontSize: 28, fontWeight: 900, color: "#f1f5f9", fontFamily: "JetBrains Mono, monospace", letterSpacing: "-0.02em" }}>{data.length}</div>
                <div style={{ fontSize: 11, color: "#475569", marginTop: 4 }}>Emails Generated</div>
              </div>
              <div className="stat-box">
                <div style={{ fontSize: 20, fontWeight: 900, color: loading ? "#22d3ee" : "#475569", fontFamily: "JetBrains Mono, monospace" }}>{loading ? "LIVE" : "IDLE"}</div>
                <div style={{ fontSize: 11, color: "#475569", marginTop: 4 }}>Workflow Status</div>
              </div>
              <div className="stat-box">
                <div style={{ fontSize: 20, fontWeight: 900, color: "#a78bfa", fontFamily: "JetBrains Mono, monospace" }}>AI</div>
                <div style={{ fontSize: 11, color: "#475569", marginTop: 4 }}>LangGraph Agents</div>
              </div>
              <div className="stat-box">
                <div style={{ fontSize: 20, fontWeight: 900, color: "#34d399", fontFamily: "JetBrains Mono, monospace" }}>CSV</div>
                <div style={{ fontSize: 11, color: "#475569", marginTop: 4 }}>Outreach Workflow</div>
              </div>
            </div>
          </div>
        </div>

        {/* TABS */}
        <div style={{ display: "flex", gap: 10, marginBottom: 24 }}>
          <button onClick={() => setActiveTab("html")} className={`tab-btn ${activeTab === "html" ? "tab-active" : "tab-inactive"}`}>HTML Workflow</button>
          <button onClick={() => setActiveTab("csv")} className={`tab-btn ${activeTab === "csv" ? "tab-active" : "tab-inactive"}`}>CSV Workflow</button>
        </div>

        {/* HTML WORKFLOW */}
        {activeTab === "html" && (
          <div className="card" style={{ padding: "28px 32px", marginBottom: 20, display: "flex", flexWrap: "wrap", gap: 24, alignItems: "center", justifyContent: "space-between" }}>
            <div>
              <h2 style={{ fontSize: 22, fontWeight: 800, color: "#f1f5f9", letterSpacing: "-0.01em", marginBottom: 8 }}>Generate From Job Portal HTML</h2>
              <p style={{ fontSize: 13, color: "#64748b", lineHeight: 1.8, maxWidth: 480 }}>
                Paste job portal HTML inside <code style={{ background: "#0e1a2b", color: "#22d3ee", padding: "1px 7px", borderRadius: 5, fontFamily: "JetBrains Mono, monospace", fontSize: 11 }}>backend/sample.html</code> and generate recruiter outreach emails automatically.
              </p>
            </div>
            <button onClick={startGeneration} disabled={loading} className={`btn ${loading ? "btn-ghost" : "btn-cyan"}`} style={{ padding: "12px 28px", fontSize: 14 }}>
              {loading ? "Running..." : "Generate Emails →"}
            </button>
          </div>
        )}

        {/* CSV WORKFLOW */}
        {activeTab === "csv" && (
          <div className="card" style={{ padding: "32px", marginBottom: 20 }}>
            <h2 style={{ fontSize: 22, fontWeight: 800, color: "#f1f5f9", letterSpacing: "-0.01em", marginBottom: 8 }}>AI Outreach Generator</h2>
            <p style={{ fontSize: 13, color: "#64748b", lineHeight: 1.8, marginBottom: 28, maxWidth: 520 }}>
              Upload recruiter/company CSV files and generate personalized AI outreach emails using customizable prompts.
            </p>

            <div style={{ marginBottom: 20 }}>
              <label style={{ display: "block", fontSize: 12, fontWeight: 700, color: "#94a3b8", letterSpacing: "0.06em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>Upload CSV File</label>
              <input type="file" accept=".csv" onChange={(e) => setCsvFile(e.target.files[0])} className="file-input" />
            </div>

            <div style={{ marginBottom: 24 }}>
              <label style={{ display: "block", fontSize: 12, fontWeight: 700, color: "#94a3b8", letterSpacing: "0.06em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 10 }}>Custom Prompt</label>
              <textarea value={customPrompt} onChange={(e) => setCustomPrompt(e.target.value)} className="textarea-dark" style={{ height: 280 }} />
            </div>

            <button onClick={uploadCSV} disabled={loading} className={`btn ${loading ? "btn-ghost" : "btn-blue"}`} style={{ padding: "12px 28px", fontSize: 14 }}>
              {loading ? "Generating..." : "Generate From CSV →"}
            </button>
          </div>
        )}

        {/* LOGS */}
        <div className="card" style={{ padding: "24px 28px", marginBottom: 20 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 16 }}>
            <div style={{ fontSize: 13, fontWeight: 700, color: "#f1f5f9" }}>Live Workflow Logs</div>
            {loading && <div className="glow-dot" />}
          </div>
          <div style={{ height: 260, overflowY: "auto", display: "flex", flexDirection: "column", gap: 8 }}>
            {logs.length === 0 && (
              <div style={{ fontSize: 12.5, color: "#1e2a3a", fontFamily: "JetBrains Mono, monospace", padding: "10px 0" }}>No logs yet...</div>
            )}
            {logs.map((log, index) => (
              <div key={index} className={`log-entry ${log.includes("Completed") || log.includes("COMPLETED") || log.includes("Successfully") ? "done" : ""}`}>
                ⚡ {log}
              </div>
            ))}
          </div>
        </div>

        {/* SEARCH */}
        <div style={{ marginBottom: 24 }}>
          <input
            type="text"
            placeholder="Search company or role..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="input-dark"
            style={{ padding: "14px 18px", fontSize: 14, borderRadius: 12 }}
          />
        </div>

        {/* RESULTS */}
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          {filteredData.map((item, index) => (
            <div key={index} className="result-card">

              {/* ACCORDION HEADER */}
              <button onClick={() => toggleAccordion(index)} className="accordion-btn">
                <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
                  <div style={{ width: 52, height: 52, borderRadius: 14, background: "#0e1a2b", border: "1px solid #1d4ed833", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 20, fontWeight: 900, color: "#22d3ee", fontFamily: "JetBrains Mono, monospace", flexShrink: 0 }}>
                    {item.company_name?.charAt(0)}
                  </div>
                  <div style={{ textAlign: "left" }}>
                    <div style={{ fontSize: 18, fontWeight: 800, color: "#f1f5f9", letterSpacing: "-0.01em" }}>{item.company_name}</div>
                    <div style={{ fontSize: 13, color: "#475569", marginTop: 3 }}>{item.job_title}</div>

                    {/* RECRUITER EMAIL inline */}
                    <div style={{ marginTop: 10 }} onClick={(e) => e.stopPropagation()}>
                      <input
                        type="text"
                        value={item.company_email}
                        onChange={(e) => {
                          const updated = [...data];
                          updated[index].company_email = e.target.value;
                          setData(updated);
                        }}
                        className="input-dark"
                        style={{ width: 280, fontSize: 12, padding: "7px 12px" }}
                        placeholder="Recruiter email..."
                      />
                    </div>
                  </div>
                </div>
                <div style={{ fontSize: 22, color: "#334155", fontWeight: 300 }}>{openIndex === index ? "−" : "+"}</div>
              </button>

              {/* ACCORDION BODY */}
              {openIndex === index && (
                <div style={{ borderTop: "1px solid #0f1420", background: "#080a0e", padding: "24px 28px" }}>

                  {/* SUBJECT */}
                  <div style={{ marginBottom: 18 }}>
                    <label style={{ display: "block", fontSize: 11, fontWeight: 700, color: "#475569", letterSpacing: "0.08em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 8 }}>Email Subject</label>
                    <input
                      type="text"
                      value={subjects[index] || "Placement Opportunity from IIIT Bhubaneswar"}
                      onChange={(e) => setSubjects({ ...subjects, [index]: e.target.value })}
                      className="input-dark"
                    />
                  </div>

                  {/* EMAIL CONTENT */}
                  <div style={{ marginBottom: 18 }}>
                    <label style={{ display: "block", fontSize: 11, fontWeight: 700, color: "#475569", letterSpacing: "0.08em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 8 }}>Email Content</label>
                    <textarea
                      value={item.generated_email}
                      onChange={(e) => {
                        const updated = [...data];
                        updated[index].generated_email = e.target.value;
                        setData(updated);
                      }}
                      className="textarea-dark"
                      style={{ height: 300 }}
                    />
                  </div>

                  {/* ATTACHMENT */}
                  <div style={{ marginBottom: 24 }}>
                    <label style={{ display: "block", fontSize: 11, fontWeight: 700, color: "#475569", letterSpacing: "0.08em", textTransform: "uppercase", fontFamily: "JetBrains Mono, monospace", marginBottom: 8 }}>Attach Resume / Portfolio</label>
                    <input
                      type="file"
                      onChange={(e) => setAttachments({ ...attachments, [index]: e.target.files[0] })}
                      className="file-input"
                    />
                  </div>

                  {/* ACTION BUTTONS */}
                  <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
                    <button onClick={() => copyText(item.company_email)} className="btn btn-ghost">Copy Email</button>
                    <button onClick={() => copyText(item.generated_email)} className="btn btn-blue">Copy Content</button>
                    <a
                      href={`mailto:${item.company_email}?subject=${encodeURIComponent(subjects[index] || "Placement Opportunity from IIIT Bhubaneswar")}&body=${encodeURIComponent(item.generated_email)}`}
                      className="btn btn-green"
                      style={{ textDecoration: "none", display: "inline-flex", alignItems: "center" }}
                    >
                      Open Mail App
                    </a>
                    <button
                      onClick={() => sendMail(item, index)}
                      disabled={sendingIndex === index}
                      className={`btn ${sendingIndex === index ? "btn-ghost" : "btn-purple"}`}
                    >
                      {sendingIndex === index ? "Sending..." : "Send Email"}
                    </button>
                  </div>

                </div>
              )}
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}