import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Outage Comms Drafter",
    page_icon="🚨",
    layout="wide"
)

# Title
st.title("🚨 Customer Outage Comms Drafter")
st.markdown("**Turn technical timelines into customer-ready messages instantly.**")
st.markdown("---")

# INPUT SECTION
st.subheader("📋 Step 1: Enter the Technical Timeline")
timeline = st.text_area(
    "What happened during the outage? (paste technical details)",
    placeholder="Example:\n14:02 - Payment service crashed\n14:18 - Team rolled back the update\n14:45 - Systems back to normal",
    height=180
)

st.subheader("🎛️ Step 2: Choose Settings")
col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox(
        "🎙️ Message Tone",
        ["Empathetic", "Calm", "Concise"],
        help="Empathetic = caring, Calm = neutral, Concise = short and direct"
    )

with col2:
    severity = st.selectbox(
        "⚠️ Severity Level",
        ["Low", "Medium", "High"],
        help="How serious was the outage?"
    )

st.markdown("---")

# GENERATE BUTTON
st.subheader("⚡ Step 3: Generate Drafts")
generate_clicked = st.button("🚀 Generate Customer Messages", use_container_width=True)

if generate_clicked:
    if not timeline.strip():
        st.error("❌ Please enter a timeline before generating!")
    else:
        with st.spinner("🤖 AI is generating your 3 drafts... please wait"):
            try:
                response = requests.post(
                    "http://localhost:8000/generate",
                    json={
                        "timeline": timeline,
                        "tone": tone,
                        "severity": severity
                    },
                    timeout=30
                )
                data = response.json()

                st.success("✅ Drafts generated successfully!")
                st.markdown("---")
                st.subheader("📨 Your 3 Customer-Facing Drafts")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown("### 🟡 Initial Alert")
                    st.caption("Send this FIRST when issue is detected")
                    st.text_area(
                        "Copy this message:",
                        value=data.get("initial", ""),
                        height=220,
                        key="draft_initial"
                    )

                with col2:
                    st.markdown("### 🔵 In-Progress Update")
                    st.caption("Send this WHILE team is fixing it")
                    st.text_area(
                        "Copy this message:",
                        value=data.get("in_progress", ""),
                        height=220,
                        key="draft_inprog"
                    )

                with col3:
                    st.markdown("### 🟢 Resolved Notice")
                    st.caption("Send this AFTER issue is fixed")
                    st.text_area(
                        "Copy this message:",
                        value=data.get("resolved", ""),
                        height=220,
                        key="draft_resolved"
                    )

            except requests.exceptions.ConnectionError:
                st.warning("⚠️ Backend not connected. Showing DEMO output.")
                st.markdown("---")
                st.subheader("📨 Demo Output")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown("### 🟡 Initial Alert")
                    st.text_area(
                        "Copy this message:",
                        value="We are aware that some customers may be experiencing issues with our payment service. Our team has been notified and is actively investigating. We apologize for the inconvenience and will provide updates shortly.",
                        height=220,
                        key="demo1"
                    )

                with col2:
                    st.markdown("### 🔵 In-Progress")
                    st.text_area(
                        "Copy this message:",
                        value="We have identified the root cause of the payment service disruption and our engineering team is working hard to restore full functionality. We appreciate your patience during this time.",
                        height=220,
                        key="demo2"
                    )

                with col3:
                    st.markdown("### 🟢 Resolved")
                    st.text_area(
                        "Copy this message:",
                        value="We are pleased to inform you that the payment service issue has been fully resolved. All systems are operating normally. We sincerely apologize for any inconvenience caused and thank you for your patience.",
                        height=220,
                        key="demo3"
                    )

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# HISTORY SECTION
st.markdown("---")
st.subheader("🕓 Past Generations")

try:
    history_response = requests.get("http://localhost:8000/history", timeout=5)
    history = history_response.json()

    if history:
        for item in reversed(history[-5:]):
            with st.expander(f"🕐 {item.get('timestamp', 'N/A')} — Tone: {item.get('tone', 'N/A')} | Severity: {item.get('severity', 'N/A')}"):
                st.write("**Timeline:**", item.get('timeline', '')[:150] + "...")
    else:
        st.info("No history yet. Generate some drafts first!")

except:
    st.info("History will appear here once the backend is running.")

# FOOTER
st.markdown("---")
st.caption("Built for Infinite Computer Solutions – AI Prototype Challenge 2026")
