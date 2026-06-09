# 🚨 Outage Comms Drafter — AI-Powered Customer Communication Tool

> Auto-generate customer-facing outage messages from raw technical descriptions using AI Agent + MCP.

---

## 🧠 What It Does

An engineer types a raw technical description like:
> "DB replication lag at 142ms, primary node failover initiated"

The AI agent automatically:
- 🔍 Detects severity (low / medium / high)
- ✍️ Generates 3 ready-to-send customer messages:
  - 📢 **Initial** — "We are aware of an issue..."
  - 🔄 **In Progress** — "Our team is actively working on..."
  - ✅ **Resolved** — "The issue has been fully resolved..."
- 📨 Posts to Slack automatically

---

## 🏗️ Architecture

```
Streamlit UI (app.py)
        │
        ▼
MCP Tool (mcp_tool.py)
        │
        ▼
AI Agent Loop (agent.py)
        │
        ├── Auto detect severity
        ├── Generate 3 customer drafts
        └── Self-correction quality check
        │
        ▼
Groq API — LLaMA 3.1 (Free Tier)
        │
        ▼
Slack API (slack_integration.py)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/Pooja26-maker/outage-comms-drafter.git
cd outage-comms-drafter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get free API keys
- **Groq API key** — Go to [console.groq.com](https://console.groq.com) → Create API key
- **Slack API key** — Go to [api.slack.com](https://api.slack.com) → Create app

### 4. Set your API keys
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
SLACK_BOT_TOKEN=your_slack_bot_token_here
SLACK_CHANNEL_ID=your_slack_channel_id_here
```

---

## ▶️ Run Instructions

### Run the Web App
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

### Run the MCP Tool
```bash
python mcp_tool.py
```

### Run Tests
```bash
pytest tests/test_app.py -v
```

---

## 🤖 AI Agent Loop

Our AI agent does NOT just call the API once — it self-corrects:

```
1. Takes technical timeline as input
2. Auto detects severity (low / medium / high)
3. Generates Initial → In-Progress → Resolved drafts
4. Checks tone quality for each draft
5. If tone is wrong → rewrites automatically (max 3 tries)
6. Returns all 3 final approved drafts
```

---

## 🔧 MCP Tools Exposed

| Tool | Description |
|------|-------------|
| `generate_outage_message` | Takes technical input → returns 3 customer drafts |
| `get_tone_options` | Returns available tone options |
| `get_severity_levels` | Returns available severity levels |

---

## 📂 Project Structure

```
outage-comms-drafter/
├── app.py                  # Streamlit web UI
├── agent.py                # AI agent loop + Groq integration
├── mcp_tool.py             # Custom MCP tool
├── slack_integration.py    # Slack API integration
├── requirements.txt        # Python dependencies
├── prompts.md              # Key prompts used
├── ai_usage.md             # AI usage notes
├── .env.example            # API keys template
├── README.md               # Project documentation
├── sample_data/
│   ├── input.json          # Sample inputs
│   └── output.json         # Sample outputs
└── tests/
    └── test_app.py         # Pytest test cases
```

---

## ⚠️ Assumptions & Limitations

- Uses **Groq free tier** — rate limits apply
- No persistent storage — messages generated fresh each time
- Severity detection is AI-based, may vary
- Designed for demo/prototype purposes
- Slack integration requires a free Slack workspace

---

## 🛠️ Tech Stack

| Category | Tool |
|----------|------|
| UI | Streamlit |
| AI Model | Groq — LLaMA 3.1 8B |
| MCP Protocol | FastMCP by Anthropic |
| API Integration | Slack SDK |
| Testing | Pytest |
| Source Control | GitHub |

---

## 👥 Team

| Member | Role |
|--------|------|
| Member 1 | Streamlit UI |
| Member 2 | AI Agent Loop + Groq Integration |
| Member 3 | Custom MCP Tool |
| Member 4 | Slack Integration + Docs + Tests |

---

