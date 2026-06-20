# src/topology/graph_builder.py
import networkx as nx

class PharosTopologyBuilder:
    def __init__(self):
        # Directed Graph represents directional supply chain dependencies
        self.graph = nx.DiGraph()

    def create_govtech_supply_chain(self) -> nx.DiGraph:
        """Populates the graph with a complex software supply chain topology."""
        self.graph.clear()
        
        # 1. Infrastructure Nodes (Where things are hosted)
        self.graph.add_node("DC_UK_SOUTH", type="Infrastructure", provider="AWS", region="UK-South")
        self.graph.add_node("DC_EU_EAST", type="Infrastructure", provider="Azure", region="EU-East")

        # 2. Organization Nodes (Who builds/operates things)
        self.graph.add_node("PRIME_ALPHA", type="Organization", criticality=9.5, domain="Defence")
        self.graph.add_node("SUB_BETA", type="Organization", criticality=6.0, domain="Software Dev")
        
        # 3. Component Nodes (The software stack elements)
        self.graph.add_node("GOV_PORTAL_CORE", type="Component", cve_count=0, integrity=1.0)
        self.graph.add_node("AUTH_MODULE_v2", type="Component", cve_count=2, integrity=0.85)
        self.graph.add_node("OPEN_SOURCE_LOGGING_LIB", type="Component", cve_count=1, integrity=0.40)

        # 4. Define the Topology Edges (Relationships)
        # Software-to-Software dependencies
        self.graph.add_edge("GOV_PORTAL_CORE", "AUTH_MODULE_v2", relation="DEPENDS_ON")
        self.graph.add_edge("AUTH_MODULE_v2", "OPEN_SOURCE_LOGGING_LIB", relation="DEPENDS_ON")
        
        # Organization-to-Component ownership
        self.graph.add_edge("SUB_BETA", "AUTH_MODULE_v2", relation="DEVELOPS")
        self.graph.add_edge("PRIME_ALPHA", "GOV_PORTAL_CORE", relation="OPERATES")
        
        # Deployment paths to Infrastructure
        self.graph.add_edge("GOV_PORTAL_CORE", "DC_UK_SOUTH", relation="DEPLOYED_TO")
        self.graph.add_edge("OPEN_SOURCE_LOGGING_LIB", "DC_EU_EAST", relation="HOSTED_IN")

        return self.graph

    def get_upstream_impact(self, compromised_node: str) -> list:
        """Traverses backwards through the directed edges to see who relies on this node."""
        if compromised_node not in self.graph:
            return []
        # nx.ancestors finds all nodes that have a path leading *into* the compromised node
        return list(nx.ancestors(self.graph, compromised_node))

# This block allows you to test this layer independently from your root directory
if __name__ == "__main__":
    builder = PharosTopologyBuilder()
    G = builder.create_govtech_supply_chain()
    print("--- Pharos NetworkX Topology Layer Initialized ---")
    print(f"Total Network Entities (Nodes): {G.number_of_nodes()}")
    print(f"Total Structural Dependencies (Edges): {G.number_of_edges()}")
    
    test_node = "OPEN_SOURCE_LOGGING_LIB"
    print(f"Upstream blast radius for '{test_node}': {builder.get_upstream_impact(test_node)}")