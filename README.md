# Pharos Agentic GraphRAG

## Reference Architecture & Technical Proof of Concept

**An Automated, Resilient Supply Chain Cyber Triage & Control Center**

---

## Project Overview

Enterprise Security Operations Centers (SOCs) frequently encounter high volumes of infrastructure and supply chain alerts, making rapid cyber triage an operational bottleneck. When an alert fires, security engineers must immediately establish context: identifying the targeted asset, mapping its upstream and downstream dependencies, and calculating the systemic blast radius of the threat.

Pharos is a functional reference architecture and system prototype designed to automate this triage lifecycle. By integrating a multi-agent orchestration layer with a deterministic network topology knowledge graph (GraphRAG), Pharos analyzes raw infrastructure anomalies, resolves semantic relationships, computes deep topological paths, and generates containment playbooks.

---

## Architectural Foundations & Core Pillars

The reference architecture is governed by four core operational pillars designed for deployment in stable enterprise environments:

### 1. Active Guardrails & Token Sanitation

Before raw incident description data reaches the core intelligence layers, it passes through an inline sanitation filter inside `coordinator.py`. This layer scans for, intercepts, and blocks adversarial prompt injections, system override attempts, and malicious token payloads. If an injection is flagged, the pipeline short-circuits to an isolated triage state, protecting downstream LLM nodes from manipulation.

### 2. Strict Human-in-the-Loop (HITL) Controls

Pharos operates as an autonomous advisory network rather than an unmonitored automated execution engine. Prior to deploying any containment playbook or modifying network states, the orchestration engine forces an intercept gate. Triage results must be manually reviewed, validated, and authorized by a human supervisor via the control console before any mitigation scripts execute.

### 3. Immutable Forensic Audit Ledger & Telemetry Logs

System transparency is maintained through dual-layered logging structures. The system records every intermediate pipeline state, raw system prompt, graph-injected context, and unparsed LLM completion inside real-time execution traces. Concurrently, a rolling audit ledger writes completed triage events to persistent disk, ensuring forensic readiness for post-incident reviews and compliance reporting.

### 4. The LLMOps Accuracy Hub (Iterative Prompt Optimization Framework)

The system includes a native evaluation pipeline that treats prompts as software assets. By compiling model extraction accuracy against a standardized 100-case baseline dataset, this engine serves as a data-driven testing rig. It exposes exactly where the model fails (such as semantic negations or structured log parsing), allowing engineers to measure score drift, catch functional regressions, and optimize agent prompts through disciplined engineering loops.

---

## 🧬 System Architecture & Execution Philosophy

Pharos is designed around a strict architectural boundary that separates cognitive reasoning from deterministic execution. Unlike naive agentic frameworks that chain multiple LLMs together—which introduces high latency, runaway token costs, and a compounding probability of hallucinations—Pharos utilizes a disciplined, **hybrid multi-agent design**:

1. **Cognitive Tier (The Analyst Agent):** A singular LLM instance (`gpt-4o-mini`) used exclusively for what language models do best: parsing messy, unstructured, and novel alert log text to resolve semantic entities.
2. **Deterministic Tier (The Risk Agent):** A completely algorithmic execution engine. Once the target node is resolved, downstream blast-radius analysis is immediately offloaded to a local graph database engine (`NetworkX`) using mathematical ancestry tracking.

By confining fluid LLM reasoning strictly to the intake layer and using exact graph algorithms for impact analysis, Pharos guarantees $100\%$ predictable, repeatable, and cost-effective triage execution at enterprise scale.

### 🛡️ Core Operational Guardrails & Fallbacks

To ensure production readiness, the architecture enforces three non-negotiable operational boundaries:

* **Pre-Filter Input Guardrails:** A string-normalization token scanner inside `coordinator.py` intercepts payloads and forces an immediate circuit-breaker fallback to `UNKNOWN` if adversarial override phrases are detected.
* **Graceful Degradation Fallback:** If the external OpenAI API experiences a timeout or global outage, the system catches the exception and engages a local **Heuristic Signature Network** to extract critical infrastructure entities via regex matching, preventing system blackout.
* **Human-in-the-Loop (HITL) Intercept:** Pharos operates strictly as an advisory engine. A hard gate freezes the loop prior to containment deployment, requiring an operator to manually review and authorize the generated cryptographic shell script via the Streamlit console.

---

## Core System Architecture Workflow

The runtime execution flow maps the path from unstructured intake down to the automated script compilation block:

```
[Incoming Raw Alert String] ──► [Input Guardrails & Token Sanitation Filter]
                                              │
                        ┌─────────────────────┴─────────────────────┐
                        ▼                                           ▼
         [Heuristic Signature Network]               [Live LLM Cognitive Loop Tier]
          (Instant Regex / String Tokens)             (gpt-4o-mini Semantic Parsing)
                        │                                           │
                        └─────────────────────┬─────────────────────┘
                                              ▼
                               [Structural Entity Resolution]
                                              │
                           [NetworkX Graph Topology Traversal]
                              (Backward Ancestor Tracking)
                                              │
                             [Physics-Powered Visual Canvas]
                                              │
                        [Human-in-the-Loop Intercept Approval Gate]
                                              │
                          [Enforced Playbook Script Compilation]

```

---

## Technical Implementation Layout

The responsive web console maps directly to these architectural objectives across a structured, four-tab interface layout:

### Tab 1: Live Triage Console

* **Incident Intake & Guardrail Protection:** Hosts the active simulation environment where raw text alerts are processed, validated against injection strings, and normalized.
* **Heuristic Safety Net:** If the live cloud network encounters key constraints or timeouts, a local string-matching fallback matrix scans for explicit infrastructure tokens (such as `EU_EAST` or `AUTH_MODULE`). This hybrid design maintains triage availability under varying network conditions.
* **Dynamic PyVis Visual Mapping Canvas:** Renders calculated graph paths onto an interactive light-slate canvas. Nodes are scaled and color-coded based on active risk definitions (Target, Affected, or Mitigated), using high-contrast text-stroke shadows for scannability on enterprise dashboard displays.
* **HITL Approval Gate Component:** Renders the generated shell-script containment playbook side-by-side with interactive action triggers (`Approve & Execute` / `Reject & Quarantine`), pausing the backend workflow until manual clearance is granted.

### Tab 2: Agent Execution Trace

* **Granular Telemetry Logs:** Exposes the internal thought chains, system boundaries, and token tracking matrices of each individual agent (Analyst, Risk, and Coordinator).
* **Intermediate State Subqueries:** Displays the exact programmatic NetworkX graph queries used to pull topology context, along with unparsed LLM completions, providing complete debugging transparency.

### Tab 3: Audit Log History

* **Forensic Ledger Registry:** Provides concurrent access to a rolling dataframe ledger detailing every processed incident. Tracks timestamps, target nodes, calculated asset counts, and final control deployment statuses for continuous forensic auditability.

### Tab 4: LLMOps Accuracy Hub

* **Automated Regression Testing:** Allows engineering teams to run live performance audits against a version-controlled benchmark dataset to systematically surface edge-case failures.
* **Altair Score Vector Drift Graph:** Visualizes performance trends over time using an Altair chart engine bounded strictly between a 0 to 100 scale. Tilt-encoded timestamp vectors (angled at -45°) eliminate visual clipping, giving engineers a clean chart to verify that ongoing prompt modifications drive continuous system accuracy improvements.

---

## Data Schema & Graph Architecture

To construct the baseline reference infrastructure topology, Pharos normalizes disparate inventory registers and access matrices into a directed relational knowledge graph.

### 1. Ingested Data Sources

* **Security Telemetry:** Real-time infrastructure events, active CVE vulnerability matrices, and perimeter firewall anomalies.
* **Infrastructure Inventory:** Enterprise configuration asset registers mapping host allocations, deployment environments, and localization zones.
* **Access Control Matrices:** Active Directory path maps tracking administrative profiles, group permissions, and security scope perimeters.

### 2. Graph Schema Mapping

The underlying NetworkX database engine maps flat data blocks into directed entities (nodes) and relational operations (edges):

```
[User Group Entity] ───( ADMINISTERS )───► [Server / Host Entity]
                                                    │
                                             ( HOSTS / RUNS )
                                                    │
                                                    ▼
[Database Entity] ◄───( COMMUNICATES_WITH )─── [Application Entity]
       │                                                 │
  ( CONTAINS )                                      ( EXPOSES )
       │                                                 │
       ▼                                                 ▼
[Sensitive Data Entity]                         [Vulnerability Entity]

```

* **Node Definitions:**
* `Server / Host`: Computing hardware footprints, virtual cluster nodes, or cloud instances (`DC_EU_EAST`, `DC_UK_SOUTH`).
* `Application`: Active software deployments and backend microservices (`GOV_PORTAL_CORE`, `AUTH_MODULE_v2`).
* `Database`: Relational or non-relational core data clusters.
* `Vulnerability`: Active security exposures or software bugs (`OPEN_SOURCE_LOGGING_LIB`).
* `User Group`: IAM identity footprints and permission levels (`PRIME_ALPHA`, `SUB_BETA`).
* `Sensitive Data`: High-value data stores requiring zero-trust masking boundaries (PII, compliance logs).


* **Edge Operations:**
* `Server` ── `HOSTS` ──► `Application`
* `Application` ── `COMMUNICATES_WITH` ──► `Database`
* `Database` ── `CONTAINS` ──► `Sensitive Data`
* `User Group` ── `ADMINISTERS` ──► `Server`
* `Application` ── `EXPOSES` ──► `Vulnerability`



---

## Comprehensive Technology Stack Matrix

The implementation is constructed entirely using open-source, decoupled architectural blocks to maximize deployment portability and avoid infrastructure lock-in.

| Component | Technology | Architectural Purpose |
| --- | --- | --- |
| **Orchestration Layer** | Python / LangGraph | Manages system execution loops, dynamic state machines, and multi-agent cross-communication frames. |
| **Topology Graph Database** | NetworkX | Models network nodes and paths mathematically to run deterministic ancestry tracking algorithms. |
| **Intelligence Engine** | OpenAI API (`gpt-4o-mini`) | Delivers unstructured text contextual reasoning, language parsing, and semantic extraction features. |
| **Environment Security** | `python-dotenv` | Provides configuration isolation by loading API parameters from secure local files, keeping keys out of repository paths. |
| **User Interface Console** | Streamlit | Drives the enterprise responsive web layout dashboard, live simulator selectors, and action control triggers. |
| **Visual Mapping Canvas** | PyVis (HTML5 / JS) | Renders physics-powered graph visualizations, applying real-time updates to node states. |
| **Analytical Charting** | Altair | Visualizes continuous evaluation metrics using explicit datatypes and fixed scale boundaries. |
| **Telemetry Trace Layer** | Streamlit Expanders | Isolates and renders raw agent thoughts, underlying context queries, and JSON strings to guarantee auditability. |
| **Security & Auditing** | Custom Python Sanitation | Enforces input perimeters, processes security telemetry, and updates the audit ledger. |

---

## Continuous LLMOps Evaluation Framework

A defining feature of the Pharos architecture is its dedicated, native validation engine. Instead of treating agent prompts as static configurations, Pharos maintains an automated LLMOps Performance & Auditing Hub powered by a version-controlled Golden Dataset Benchmark.

### 1. The 100-Case Golden Dataset Matrix

The testing suite runs your code against a matrix of 100 diverse, enterprise-level cybersecurity test cases. These cases are categorized into five distinct evaluation profiles designed to test the limits of model reasoning:

* **Standard Extraction:** Verifies basic entity recognition accuracy against standard alert text formats.
* **Semantic Negation:** Evaluates whether the model can accurately distinguish real active threats from distracting phrases or false alarms (for example: *"Ignore the warning on database cluster alpha as it has completely recovered; the active compromise is located on portal core"*).
* **Structured Log Parsing:** Tests the system's ability to natively process and map raw nested JSON strings and string arrays without syntax errors.
* **Adversarial Prompt Injections:** Evaluates input guardrail defense strength by running malicious system override strings against the pipeline.
* **Ambiguous / Unmapped Targets:** Verifies that the model correctly outputs a generic fallback state (`UNKNOWN`) when logs contain completely unmapped or irrelevant infrastructure targets.

### 2. Statistical Metrics Analytics & Score Drift Engine

Every live audit run computes explicit metrics across your dataset to establish an overall performance profile. The baseline score calculation is handled programmatically:

$$\text{Overall Model Accuracy} = \frac{\text{Passed Benchmark Verdicts}}{\text{Total Golden Dataset Test Cases}} \times 100$$

To display these tracking trends cleanly without data compression or axis truncation, Pharos uses an Altair data engine. This dashboard component ensures:

* **Fixed Bounds Scaling:** The performance tracking axis stays strictly bounded between 0 to 100, keeping metrics visually intuitive and realistic.
* **Tilted Label Encodings:** Evaluation timestamps are rendered with a precise -45° alignment, preventing wide datetime labels from clipping or dropping beneath ellipses.
* **Vector Drift Insight:** By capturing and logging historical runs to a local ledger file (`eval_performance_history.json`), the system builds an audit history graph. This timeline instantly shows how modifications to agent prompts or system configurations alter performance over time.

---

## UI Engineering & Enterprise Accessibility Posture

The user interface is built as an accessible Light-Mode Enterprise Glass Console crafted to comply with strict WCAG AAA color contrast guidelines.

* **High-Contrast Design Elements:** Interactive buttons are rendered using a high-visibility enterprise royal blue background (`#1e40af`) paired with sharp, ultra-bold text formatting (`font-weight: 900`). This maintains visual scannability under high-glare operation center monitors.
* **Dynamic Canvas Optimization:** The visual graph network utilizes white stroke outlines around text elements. This ensures node labels remain crisp and scannable against light slate grid backdrops (`#f8fafc`).
* **Deep-Dive Raw Inspector:** Situated directly beneath the verification data tables, the layout provides a text-inspector panel. This component prints full raw query strings and raw JSON objects inside code snippets, removing string truncation bottlenecks so you can review entire payloads with absolute ease.

---

> **Project Status & Disclaimer**

> [IMPORTANT]
> Pharos is an independent, open-source personal research project built entirely using public libraries. It is not affiliated with, endorsed by, or representative of any commercial entity or employer.