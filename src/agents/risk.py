# src/agents/risk.py
from src.topology.graph_builder import PharosTopologyBuilder

# Instantiate the live network topology graph database layer for analytical queries
topo_engine = PharosTopologyBuilder()
graph_network = topo_engine.create_govtech_supply_chain()

def run_risk_agent(resolved_node: str, execution_logs: list) -> list:
    """
    Queries the NetworkX graph to analyze structural blast radius impact
    by traversing backwards from the compromised entry-point asset.
    """
    execution_logs.append("[Risk Agent] Accessing live NetworkX Directed Graph database infrastructure...")
    
    if resolved_node == "UNKNOWN" or resolved_node not in graph_network:
        execution_logs.append("[Risk Agent] Node target unrecognized in NetworkX topology schema. Blast radius safely calculated as 0.")
        return []

    # Executes analytical backwards-graph traversal tracking algorithms (ancestor tracking)
    upstream_impacted_assets = topo_engine.get_upstream_impact(resolved_node)
    blast_radius_count = len(upstream_impacted_assets)
    
    execution_logs.append(f"[Risk Agent Telemetry Log] Target node '{resolved_node}' evaluated. Network structural paths identify these upstream dependencies threatened: {upstream_impacted_assets}")
    execution_logs.append(f"[Risk Agent Conclusion] Detected {blast_radius_count} vulnerable vectors downstream/upstream from target node.")
    
    # 🛠️ AMENDMENT: Return the actual list of nodes, not just the integer count
    return upstream_impacted_assets