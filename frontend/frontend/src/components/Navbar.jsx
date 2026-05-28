import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
  const location = useLocation();

  const navItem = (path, label) => (
    <Link
      to={path}
      style={{
        padding: "8px 16px",
        borderRadius: 8,
        fontSize: 14,
        fontWeight: 500,
        textDecoration: "none",
        fontFamily: "'Inter', sans-serif",
        transition: "all 0.2s",
        ...(location.pathname === path
          ? { background: "#0e1a2b", color: "#22d3ee", border: "1px solid #1d3a5f" }
          : { color: "#64748b", border: "1px solid transparent" }),
      }}
      onMouseEnter={(e) => {
        if (location.pathname !== path) {
          e.target.style.color = "#94a3b8";
          e.target.style.background = "#0d0f14";
        }
      }}
      onMouseLeave={(e) => {
        if (location.pathname !== path) {
          e.target.style.color = "#64748b";
          e.target.style.background = "transparent";
        }
      }}
    >
      {label}
    </Link>
  );

  return (
    <nav style={{
      width: "100%",
      background: "rgba(8,8,9,0.88)",
      backdropFilter: "blur(12px)",
      borderBottom: "1px solid #111827",
      position: "sticky",
      top: 0,
      zIndex: 50,
    }}>
      <div style={{
        maxWidth: 1280,
        margin: "0 auto",
        padding: "0 24px",
        height: 64,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
      }}>

        {/* LOGO */}
        <Link to="/" style={{ textDecoration: "none", display: "flex", alignItems: "center", gap: 10 }}>
          <div style={{
            width: 34,
            height: 34,
            borderRadius: 9,
            background: "#22d3ee",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontWeight: 900,
            fontSize: 16,
            color: "#020617",
            fontFamily: "'JetBrains Mono', monospace",
          }}>P</div>
          <span style={{
            fontSize: 17,
            fontWeight: 800,
            letterSpacing: "-0.02em",
            color: "#f1f5f9",
            fontFamily: "'Inter', sans-serif",
          }}>PlacementGPT</span>
        </Link>

        {/* LINKS */}
        <div style={{ display: "flex", gap: 6 }}>
          {navItem("/", "Home")}
          {navItem("/setup", "Setup")}
          {navItem("/dashboard", "Dashboard")}
        </div>

      </div>
    </nav>
  );
}