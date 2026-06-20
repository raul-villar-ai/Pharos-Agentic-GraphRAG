```markdown
# Pharos Agentic GraphRAG — User Guide
## Operational Deployment & Triage Walkthrough Manual

This manual provides instructions for initializing, simulating, and auditing the Pharos Agentic GraphRAG triage ecosystem.

---

## Prerequisites & Installation

Before initializing the console, verify that your local environment is configured with the required environment keys to authenticate cloud LLM transactions.

### 1. Clone the Repository & Initialize Environment
```bash
# Clone the showcase project repository
git clone [https://github.com/your-username/pharos-graphrag.git](https://github.com/your-username/pharos-graphrag.git)
cd pharos-graphrag

# Initialize and activate the Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\Activate.ps1

# Install core dependencies
pip install -r requirements.txt

```

### 2. Configure Environment Secrets

Pharos utilizes a live `gpt-4o-mini` engine for semantic parsing alongside a local signature-matching fallback network. Create a `.env` file in the root project directory to manage credentials securely:

```text
OPENAI_API_KEY=your_actual_secure_api_key_here

```

### 3. Launch the Web Console

Execute the Streamlit application engine from the terminal:

```bash
streamlit run app.py

```

The application will automatically compile and open inside your default browser workspace at `http://localhost:8501`.

---

## Step-by-Step Triage Operations

### Step 1: Ingesting an Incident Alert

1. Navigate to **Tab 1: Live Triage Console** on the primary interface.
2. Locate the **Incident Intake Panel** in the left column.
3. Select an incident simulation from the **Select a Threat Profile to Simulate** dropdown menu (such as *Scenario 1: Logging Library Zero-Day*).
4. The raw message text will auto-populate the description field. To evaluate custom assets, select *Custom Input* and paste raw infrastructure log text into the field.
5. Click **Execute Autonomous Triage**.

### Step 2: Evaluating the Graph Matrix & Blast Radius

1. Once execution concludes, review the **KPI Metrics Row** situated at the top of the right workspace column.
2. Inspect the **Calculated Blast Radius** metric to determine the precise number of upstream or downstream network assets threatened by lateral movement or cascading vulnerabilities.
3. Scroll down to the **Interactive Topology Blast Radius Map**. This physics-powered canvas maps active relational dependencies:
* **Red Target Node (🎯):** The verified root-cause entity where the attack or exploit originated.
* **Orange Affected Nodes (⚠️):** Adjacent downstream or upstream infrastructure assets threatened due to topological path linkages.
* **Silver Nominal Nodes (🟢):** Unaffected, healthy enterprise components.



### Step 3: Managing the Human-in-the-Loop Gate

1. If the multi-agent system flags a critical threat structure, the **Human-in-the-Loop Control Gate Intercept** panel unlocks at the base of the interface.
2. Review the programmatically compiled shell-script containment playbook within the code block display.
3. Select an enforcement action to conclude the triage cycle:
* **Approve & Execute (✅):** Authorizes the mitigation script. The interactive topology canvas dynamically transitions to reflect the updated security posture, turning affected systems a secure green color marked with a `🔒 LOCKED` indicator flag.
* **Reject & Quarantine (❌):** Terminates the active containment deployment, preserving original network paths in their baseline state for deep forensic manual tracing.



---

## Advanced Analysis & Performance Verification

### 1. Reviewing Deep Telemetry (Tab 2)

Select the **Agent Execution Trace** tab to evaluate the internal thought chains, system boundaries, and token sanitation matrices of each individual agent (Analyst, Risk, and Coordinator). This tab exposes raw system boundary prompts, the programmatic NetworkX graph lookups executed against the topology matrix, and the unparsed JSON payload returned by the cloud LLM before parsing.

### 2. Inspecting the Historical Ledger (Tab 3)

The **System Triage Ledger** tab renders a rolling data frame tracking the last 100 triage events processed by the machine. This ledger stores precise execution timestamps, resolved targets, calculated blast asset counts, and final manual control deployment statuses to maintain forensic readiness and compliance audatibility.

### 3. Running Continuous Performance Audits (Tab 4)

Prompts are version-controlled software assets. To test system accuracy and protect against structural regressions after making modifications to agent prompts or routing code bases:

1. Navigate to the **LLMOps Accuracy Hub** tab.
2. Click **Execute Live Performance Audit**.
3. The validation engine cycles through the 100-case version-controlled benchmark dataset across five distinct evaluation vectors: Standard Extraction, Semantic Negation, Structured Log Parsing, Input Guardrail Injections, and Unmapped Fallbacks.
4. Review the generated **Historical Evaluation Accuracy Score Vector Drift Graph** to verify that your structural changes drive continuous system accuracy improvements without triggering regression errors.

```

> **Project Status & Disclaimer** > Pharos is an independent, open-source personal research project built entirely using public libraries. It is not affiliated with, endorsed by, or representative of any commercial entity or employer.