import streamlit as st
from agent import agent_loop
 
st.set_page_config(
    page_title="OutageComms AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
 
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"], .stApp {
    font-family: 'Space Grotesk', sans-serif !important;
    background: #03020a !important;
    color: #ddd9f5 !important;
}
#MainMenu, header, footer, .stDeployButton { display: none !important; }
.block-container { padding: 0 3rem 4rem !important; max-width: 1300px !important; }
 
/* ANIMATED GRID BACKGROUND */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(88,28,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(88,28,255,0.04) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: gridMove 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}
 
@keyframes gridMove {
    0% { background-position: 0 0; }
    100% { background-position: 50px 50px; }
}
 
/* ANIMATED GRADIENT ORBS */
.orb1 {
    position: fixed;
    width: 700px; height: 700px;
    background: radial-gradient(circle, rgba(124,58,237,0.15), transparent 70%);
    top: -300px; left: -300px;
    border-radius: 50%;
    animation: float1 8s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}
.orb2 {
    position: fixed;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(6,182,212,0.1), transparent 70%);
    bottom: -200px; right: -200px;
    border-radius: 50%;
    animation: float2 10s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}
.orb3 {
    position: fixed;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(236,72,153,0.08), transparent 70%);
    top: 50%; left: 50%;
    border-radius: 50%;
    animation: float3 12s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}
 
@keyframes float1 {
    0%, 100% { transform: translate(0,0) scale(1); }
    50% { transform: translate(80px, 60px) scale(1.1); }
}
@keyframes float2 {
    0%, 100% { transform: translate(0,0) scale(1); }
    50% { transform: translate(-60px, -40px) scale(1.15); }
}
@keyframes float3 {
    0%, 100% { transform: translate(-50%,-50%) scale(1); }
    33% { transform: translate(-40%,-60%) scale(1.2); }
    66% { transform: translate(-60%,-40%) scale(0.9); }
}
 
/* HERO SECTION */
.hero {
    padding: 5rem 0 2.5rem;
    text-align: center;
    position: relative;
    z-index: 1;
}
 
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(6,182,212,0.1));
    border: 1px solid rgba(124,58,237,0.3);
    border-radius: 100px;
    padding: 8px 22px;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 2rem;
    animation: fadeInDown 0.8s ease forwards;
}
 
.live-dot {
    width: 7px; height: 7px;
    background: #22c55e;
    border-radius: 50%;
    animation: livePulse 1.5s ease-in-out infinite;
    box-shadow: 0 0 8px #22c55e;
}
 
@keyframes livePulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.4); opacity: 0.6; }
}
 
.hero-title {
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-weight: 700;
    line-height: 1.0;
    letter-spacing: -3px;
    color: #fff;
    margin-bottom: 0.8rem;
    animation: fadeInUp 0.8s ease 0.2s both;
}
 
.hero-title .grad {
    background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 50%, #ec4899 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 4s linear infinite;
}
 
@keyframes gradientShift {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}
 
.hero-desc {
    font-size: 1.05rem;
    color: #4a4668;
    font-weight: 400;
    max-width: 500px;
    margin: 0 auto 2.5rem;
    line-height: 1.7;
    animation: fadeInUp 0.8s ease 0.4s both;
}
 
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
 
/* STATS */
.stats {
    display: flex;
    justify-content: center;
    gap: 1px;
    margin-bottom: 3rem;
    background: #0f0d1a;
    border: 1px solid #1a1730;
    border-radius: 16px;
    overflow: hidden;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
    animation: fadeInUp 0.8s ease 0.6s both;
}
 
.stat-item {
    padding: 1rem 2rem;
    text-align: center;
    border-right: 1px solid #1a1730;
    position: relative;
}
.stat-item:last-child { border-right: none; }
 
.stat-num {
    font-size: 1.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
}
 
.stat-txt {
    font-size: 10px;
    color: #2e2b42;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 3px;
}
 
/* MAIN PANEL */
.panel {
    background: rgba(15,13,26,0.8);
    border: 1px solid #1a1730;
    border-radius: 24px;
    padding: 2rem;
    backdrop-filter: blur(20px);
    position: relative;
    z-index: 1;
    animation: fadeInUp 0.8s ease 0.8s both;
}
 
.panel::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 24px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(124,58,237,0.3), transparent, rgba(6,182,212,0.3));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}
 
.step-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #7c3aed;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
}
 
.step-label::before {
    content: '';
    width: 20px; height: 1px;
    background: #7c3aed;
}
 
.step-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #e2dff5;
    margin-bottom: 1rem;
}
 
/* INPUTS */
.stTextArea textarea {
    background: rgba(5,4,15,0.8) !important;
    border: 1px solid #1a1730 !important;
    border-radius: 14px !important;
    color: #b8b4d4 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.9rem !important;
    line-height: 1.8 !important;
    padding: 1.2rem !important;
    transition: all 0.3s !important;
}
.stTextArea textarea:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.12), 0 0 30px rgba(124,58,237,0.1) !important;
}
.stTextArea textarea::placeholder { color: #1e1c30 !important; }
.stTextArea label { display: none !important; }
 
.stSelectbox > div > div {
    background: rgba(5,4,15,0.8) !important;
    border: 1px solid #1a1730 !important;
    border-radius: 12px !important;
    color: #b8b4d4 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
 
/* BUTTON */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #5b21b6, #1e40af, #0e7490) !important;
    background-size: 200% auto !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1rem !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    transition: all 0.3s !important;
    position: relative !important;
    overflow: hidden !important;
}
.stButton > button:hover {
    background-position: right center !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 50px rgba(91,33,182,0.5), 0 0 30px rgba(6,182,212,0.2) !important;
}
 
/* MESSAGE CARDS */
.msg-wrap {
    background: rgba(10,8,20,0.9);
    border-radius: 20px;
    padding: 1.4rem;
    border: 1px solid #1a1730;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    animation: cardIn 0.6s ease forwards;
    position: relative;
    overflow: hidden;
}
 
.msg-wrap::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
 
.msg-wrap.initial::after { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
.msg-wrap.progress::after { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
.msg-wrap.resolved::after { background: linear-gradient(90deg, #10b981, #34d399); }
 
.msg-wrap:hover {
    transform: translateY(-5px) scale(1.01);
    border-color: #2a2545;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}
 
@keyframes cardIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
 
.msg-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 14px;
    border-radius: 100px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.7rem;
}
.chip-initial { background: rgba(245,158,11,0.1); color: #fbbf24; border: 1px solid rgba(245,158,11,0.25); }
.chip-progress { background: rgba(59,130,246,0.1); color: #60a5fa; border: 1px solid rgba(59,130,246,0.25); }
.chip-resolved { background: rgba(16,185,129,0.1); color: #34d399; border: 1px solid rgba(16,185,129,0.25); }
 
.msg-title {
    font-size: 1rem;
    font-weight: 600;
    color: #e2dff5;
    margin-bottom: 2px;
}
.msg-sub {
    font-size: 10px;
    color: #2a2740;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 1rem;
}
 
/* SUCCESS */
.success-banner {
    display: flex;
    align-items: center;
    gap: 14px;
    background: rgba(16,185,129,0.06);
    border: 1px solid rgba(16,185,129,0.15);
    border-radius: 16px;
    padding: 1rem 1.5rem;
    margin-bottom: 2rem;
    animation: fadeInDown 0.5s ease;
    position: relative;
    z-index: 1;
}
 
.sev-badge {
    padding: 3px 12px;
    border-radius: 100px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.sev-low { background: rgba(16,185,129,0.15); color: #34d399; }
.sev-medium { background: rgba(245,158,11,0.15); color: #fbbf24; }
.sev-high { background: rgba(239,68,68,0.15); color: #f87171; }
 
.divline {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #1a1730, transparent);
    margin: 2.5rem 0;
    position: relative;
    z-index: 1;
}
 
.footer-txt {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #1a1730;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding-bottom: 2rem;
    position: relative;
    z-index: 1;
}
</style>
 
<div class="orb1"></div>
<div class="orb2"></div>
<div class="orb3"></div>
 
<div class="hero">
    <div class="hero-badge">
        <div class="live-dot"></div>
        Infinite Computer Solutions · AI Prototype 2026
    </div>
    <div class="hero-title">Outage<br><span class="grad">Comms AI</span></div>
    <div class="hero-desc">Engineer types technical chaos. AI agent delivers calm, human-ready messages instantly.</div>
    <div class="stats">
        <div class="stat-item"><div class="stat-num">&lt;3s</div><div class="stat-txt">Generation</div></div>
        <div class="stat-item"><div class="stat-num">3×</div><div class="stat-txt">Drafts</div></div>
        <div class="stat-item"><div class="stat-num">AI</div><div class="stat-txt">Agent Loop</div></div>
        <div class="stat-item"><div class="stat-num">MCP</div><div class="stat-txt">Protocol</div></div>
        <div class="stat-item"><div class="stat-num">Slack</div><div class="stat-txt">Integration</div></div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# INPUT
col_l, col_r = st.columns([3, 2], gap="large")
 
with col_l:
    st.markdown("""
    <div style="position:relative;z-index:1;">
        <div class="step-label">Step 01</div>
        <div class="step-title">Paste Technical Timeline</div>
    </div>
    """, unsafe_allow_html=True)
    timeline = st.text_area("", 
        placeholder="14:02 — Payment gateway returning 500 errors on checkout\n14:18 — Root cause: DB connection pool exhausted\n14:35 — Fix deployed, monitoring in progress\n14:52 — All systems back to normal",
        height=220, label_visibility="collapsed")
 
with col_r:
    st.markdown("""
    <div style="position:relative;z-index:1;">
        <div class="step-label">Step 02</div>
        <div class="step-title">Configure Output</div>
    </div>
    """, unsafe_allow_html=True)
    tone = st.selectbox("Tone", ["Empathetic", "Calm", "Concise"])
    severity = st.selectbox("Severity", ["Auto Detect", "Low", "Medium", "High"])
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="step-label" style="position:relative;z-index:1;">Step 03</div>', unsafe_allow_html=True)
    generate_clicked = st.button("⚡  Generate Customer Drafts", use_container_width=True)
 
st.markdown('<hr class="divline">', unsafe_allow_html=True)
 
if generate_clicked:
    if not timeline.strip():
        st.error("Please enter a technical timeline first.")
    else:
        with st.spinner("AI agent analyzing and self-correcting drafts..."):
            try:
                sev_input = None if severity == "Auto Detect" else severity.lower()
                results, detected_severity = agent_loop(timeline, tone.lower(), sev_input)
                data = {
                    "initial": results.get("initial", ""),
                    "in_progress": results.get("in-progress", ""),
                    "resolved": results.get("resolved", "")
                }
                sev = detected_severity.strip().lower()
                sev_cls = f"sev-{sev}" if sev in ["low","medium","high"] else "sev-medium"
 
                st.markdown(f"""
                <div class="success-banner">
                    <span style="color:#34d399;font-size:1.2rem">✦</span>
                    <span style="color:#34d399;font-weight:600">3 drafts generated</span>
                    <span style="color:#1a1730">·</span>
                    <span style="color:#4a4668">Severity</span>
                    <span class="sev-badge {sev_cls}">{sev.upper()}</span>
                    <span style="color:#1a1730">·</span>
                    <span style="color:#4a4668">Tone: <strong style="color:#a78bfa">{tone}</strong></span>
                </div>
                """, unsafe_allow_html=True)
 
                c1, c2, c3 = st.columns(3, gap="medium")
                with c1:
                    st.markdown("""<div class="msg-wrap initial">
                        <div class="msg-chip chip-initial">⬤ &nbsp;Initial Alert</div>
                        <div class="msg-title">First Response</div>
                        <div class="msg-sub">Send the moment issue is detected</div>
                    </div>""", unsafe_allow_html=True)
                    st.text_area("", value=data.get("initial",""), height=160, key="d1", label_visibility="collapsed")
 
                with c2:
                    st.markdown("""<div class="msg-wrap progress">
                        <div class="msg-chip chip-progress">⬤ &nbsp;In-Progress</div>
                        <div class="msg-title">Active Update</div>
                        <div class="msg-sub">Send while team is fixing</div>
                    </div>""", unsafe_allow_html=True)
                    st.text_area("", value=data.get("in_progress",""), height=160, key="d2", label_visibility="collapsed")
 
                with c3:
                    st.markdown("""<div class="msg-wrap resolved">
                        <div class="msg-chip chip-resolved">⬤ &nbsp;Resolved</div>
                        <div class="msg-title">All Clear</div>
                        <div class="msg-sub">Send after issue is fixed</div>
                    </div>""", unsafe_allow_html=True)
                    st.text_area("", value=data.get("resolved",""), height=160, key="d3", label_visibility="collapsed")
 
            except Exception as e:
                st.error(f"Something went wrong: {e}")
 
st.markdown('<div class="footer-txt">OutageComms AI · Built for Infinite Computer Solutions · AI Prototype Challenge 2026</div>', unsafe_allow_html=True)
