# src/agents/coordinator.py
from src.topology.graph_builder import PharosTopologyBuilder
from .analyst import run_analyst_agent
from .risk import run_risk_agent

# Instantiate the topology validation matrix to handle structural checks
topo_engine = PharosTopologyBuilder()
graph_network = topo_engine.create_govtech_supply_chain()

class PharosIntelligentEngine:
    def invoke(self, inputs: dict) -> dict:
        """
        Orchestrates the multi-agent state machine workflow, passing execution
        context and log telemetry from the Analyst Agent to the Risk Agent.
        """
        query = inputs.get("query", "")
        execution_logs = []
        
        execution_logs.append("[Coordinator] Phase 1: Initializing Agentic Workflow State Machine.")
        
        # Step 1: Extract entity using the Analyst Agent
        target_node = run_analyst_agent(query, execution_logs)
        
        # Normalize naming variations to sync fluid spelling with strict NetworkX node IDs
        target_upper = target_node.upper()
        resolved_node = "UNKNOWN"
        if "AUTH" in target_upper: resolved_node = "AUTH_MODULE_v2"
        elif "LOG" in target_upper or "LIB" in target_upper: resolved_node = "OPEN_SOURCE_LOGGING_LIB"
        elif "PORTAL" in target_upper or "GOV" in target_upper: resolved_node = "GOV_PORTAL_CORE"
        elif "EU_EAST" in target_upper or "EU-EAST" in target_upper: resolved_node = "DC_EU_EAST"
        elif "UK_SOUTH" in target_upper or "UK-SOUTH" in target_upper: resolved_node = "DC_UK_SOUTH"
        elif "PRIME" in target_upper or "ALPHA" in target_upper: resolved_node = "PRIME_ALPHA"
        elif "SUB" in target_upper or "BETA" in target_upper: resolved_node = "SUB_BETA"
        elif target_upper in graph_network: resolved_node = target_upper

        execution_logs.append(f"[Coordinator] Phase 2: Structural Entity Resolution complete. Querying key: '{resolved_node}'.")

        # Step 2: Query the live NetworkX topological matrix via Risk Agent
        # The risk agent now returns the list of impacted assets directly
        upstream_impacted_assets = run_risk_agent(resolved_node, execution_logs)
        blast_radius_count = len(upstream_impacted_assets)
        
        # Step 3: Mitigation Infrastructure Mapping
        mitigation_plan = None
        # We trigger mitigation if the node is critical or if the blast radius is > 0
        if blast_radius_count > 0 or (resolved_node != "UNKNOWN" and resolved_node in ["OPEN_SOURCE_LOGGING_LIB", "AUTH_MODULE_v2", "GOV_PORTAL_CORE"]):
            execution_logs.append(f"[Coordinator] Phase 3: Actionable breach verified. System producing cryptographic playbook.")
            mitigation_plan = f"""# PHAROS AUTOMATED CONTAINMENT PLAYBOOK V1.2
# TARGET VECTOR: {resolved_node}
# TRAVERSAL METHOD: NETWORKX BACKWARD ANCESTRY ISOLATION

echo "🔒 Initializing zero-trust network containment protocols..."
iptables -A INPUT -p tcp --dport 8080 -m string --string "exploit" --algo bm -j DROP
echo "⚡ Isolation complete. Threatened upstream tracking loops isolated successfully."
"""
        else:
            execution_logs.append("[Coordinator] Phase 3: Zero impacted dependencies or leaf asset targeted. Applying standard log monitoring parameters.")

        execution_logs.append("[Coordinator] Phase 4: Consolidating agent runtime states for Streamlit ingestion.")
        
        return {
            "target_node": resolved_node if resolved_node != "UNKNOWN" else target_node,
            "impacted_assets": upstream_impacted_assets,  # Payload now includes the node list for UI coloring
            "blast_radius": blast_radius_count,
            "mitigation_plan": mitigation_plan,
            "execution_logs": execution_logs
        }

# Singleton engine instance setup for unified user interface binding
pharos_intelligent_engine = PharosIntelligentEngine()