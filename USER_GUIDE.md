# Pharos Agentic GraphRAG — User Guide

## Operational Deployment & Triage Walkthrough Manual

This manual provides instructions for initializing, simulating, and auditing the Pharos Agentic GraphRAG triage ecosystem.

---

## Prerequisites & Installation

Before initializing the console, verify that your local environment is configured with the required environment keys to authenticate cloud LLM transactions.

### 1. Clone the Repository & Initialize Environment

```bash
# Clone the showcase project repository
git clone https://github.com/your-username/pharos-graphrag.git
cd pharos-graphrag

# Initialize and activate the Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\Activate.ps1

# Install core dependencies
pip install -r requirements.txt

```

### 2. Configure Environment Secrets

Pharos utilizes a hybrid architecture: a live `gpt-4o-mini` engine for semantic parsing paired with a local, deterministic fallback network. Create a `.env` file in the root project directory to manage credentials:

```text
OPENAI_API_KEY=your_actual_secure_api_key_here

```

### 3. Launch the Web Console

Execute the Streamlit application engine:

```bash
streamlit run app.py

```

The console will open at `http://localhost:8501`.

> **Deployment Note:** If deploying to **Streamlit Community Cloud**, do not use a `.env` file. Instead, navigate to **Advanced Settings** in your deployment dashboard and input your key into the **Secrets** vault using TOML format: `OPENAI_API_KEY = "sk-..."`.

---

## Interface Overview: Engine Status

Upon launch, check the top-right header area for the **Runtime Engine Status**. This badge indicates your current operational mode:

* **🟢 ENGINE MODE: HYBRID COGNITIVE (LIVE LLM):** The system is successfully authenticated and utilizing GPT-4o-mini for intelligent parsing.
* **🟠 ENGINE MODE: DETERMINISTIC FALLBACK (OFFLINE):** The system has detected an API key missing or invalid, and is operating using local heuristic safety-layer patterns.

---

## Step-by-Step Triage Operations

### Step 1: Ingesting an Incident Alert

1. Navigate to **Tab 1: Live Triage Console**.
2. Select an incident simulation from the **Threat Profile** dropdown.
3. Click **Execute Autonomous Triage**.

### Step 2: Evaluating the Graph Matrix & Blast Radius

1. Review the **KPI Metrics Row** at the top right to assess the threat state.
2. The **Interactive Topology Blast Radius Map** visualizes relational dependencies:
* **🎯 Target Node:** Verified root-cause entity.
* **⚠️ Affected Nodes:** Downstream infrastructure threatened by path linkages.
* **🟢 Nominal Nodes:** Healthy enterprise components.



### Step 3: Managing the Human-in-the-Loop Gate

1. If the system flags a critical threat, the **Human-in-the-Loop Control Gate** unlocks.
2. Select an enforcement action:
* **Approve & Execute (✅):** Authorizes the containment playbook. The canvas will update to show nodes secured as `🔒 LOCKED`.
* **Reject & Quarantine (❌):** Terminates the deployment, preserving the network state for manual forensic tracing.



---

## Advanced Analysis & Performance Verification

### 1. Reviewing Deep Telemetry (Tab 2)

Select the **Agent Execution Trace** tab to inspect internal thought chains, system boundaries, and token sanitation matrices. This exposes the "raw" system prompts, programmatic NetworkX graph lookups, and the unparsed JSON payload returned by the LLM.

### 2. Inspecting the Historical Ledger (Tab 3)

The **System Triage Ledger** renders a rolling data frame tracking the last 100 triage events, storing execution timestamps, resolved targets, and final manual control statuses to maintain forensic readiness.

### 3. Running Continuous Performance Audits (Tab 4)

To protect against structural regressions after modifying code:

1. Navigate to the **LLMOps Accuracy Hub**.
2. Click **Execute Live Performance Audit**.
3. Review the **Accuracy Score Vector Drift Graph** to verify that structural changes maintain or improve system precision.

---

### 💡 Corporate Non-Affiliation Notice

*Pharos is an independent, open-source personal research project built entirely in my own time using public libraries. The code, architectural design, and synthetic datasets contained in this repository are created solely in an individual capacity for learning and brand-building purposes. They do not reflect the views, strategies, or technologies of any current or past employers.*