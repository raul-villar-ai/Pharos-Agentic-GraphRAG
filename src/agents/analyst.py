# src/agents/analyst.py
import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from rapidfuzz import process, fuzz
from src.config.prompts import get_analyst_prompt
from src.topology.graph_builder import PharosTopologyBuilder

# Load variables
load_dotenv()

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))
except Exception:
    client = None

topo_engine = PharosTopologyBuilder()
graph_network = topo_engine.create_govtech_supply_chain()
VALID_NODES_LIST = list(graph_network.nodes)

def normalize_input(query: str) -> str:
    """Strips noise to neutralize obfuscation."""
    return re.sub(r'[^a-zA-Z0-9]', '', query.lower())

def check_input_integrity(query: str) -> tuple[bool, str]:
    """Multi-stage Guardrail: Exact signature, Normalization, Fuzzy Intent."""
    if not query or not query.strip():
        return False, "Empty payload block rejected."

    clean_alpha = normalize_input(query)

    malicious_signatures = [
        "systemoverride", "ignoreprevious", "ignoreallinstructions",
        "printsystemprompt", "bypassconstraints", "developermode",
        "actasunrestricted", "override"
    ]
    
    for sig in malicious_signatures:
        if sig in clean_alpha:
            return False, f"Adversarial signature '{sig}' detected."

    adversarial_intents = [
        "system override", "forget safety rules", "ignore instructions",
        "dump internal credentials", "unrestricted mode"
    ]
    
    match, score, _ = process.extractOne(clean_alpha, adversarial_intents, scorer=fuzz.partial_ratio)
    
    if score > 80:
        return False, f"Adversarial intent intercepted (Confidence: {score:.1f})"

    return True, "Payload verified safe."

def run_analyst_agent(query: str, execution_logs: list) -> str:
    """
    Normalizes input, executes safety checks, and queries LLM with Grounding Validation.
    """
    execution_logs.append("[Analyst Agent] Launching deep payload integrity inspection.")
    
    is_safe, diagnostic_msg = check_input_integrity(query)
    if not is_safe:
        execution_logs.append(f"[Analyst Agent ALERT] Guardrail Intercept: {diagnostic_msg}")
        return "UNKNOWN"
        
    execution_logs.append("[Analyst Agent] Input integrity verified. Proceeding to semantic parsing.")
    target_node = "UNKNOWN"
    
    if client and os.getenv("OPENAI_API_KEY"):
        try:
            system_prompt = get_analyst_prompt(VALID_NODES_LIST)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                temperature=0.0
            )
            res_text = response.choices[0].message.content.strip()
            execution_logs.append(f"[Analyst Agent Raw Thought] {res_text}")
            
            match = re.search(r"TARGET_NODE:\s*(.*)", res_text, re.IGNORECASE)
            if match:
                extracted = match.group(1).strip()
                
                # 🛡️ NEW: STRICT SCHEMA VALIDATION (Grounding Check)
                # We only accept the LLM result if it exists in our topological matrix
                if extracted != "UNKNOWN" and extracted not in VALID_NODES_LIST:
                    execution_logs.append(f"[Analyst Agent Warning] Hallucination detected: '{extracted}' not in topology. Overriding to UNKNOWN.")
                    target_node = "UNKNOWN"
                else:
                    target_node = extracted
                    
        except Exception as e:
            execution_logs.append(f"[Analyst Agent Warning] Live LLM extraction failed ({str(e)}).")
            
    # Fallback keyword matrix
    if target_node == "UNKNOWN" or target_node.upper() == "UNKNOWN":
        text_upper = query.upper()
        # ... [Keep your existing fallback keyword matrix here] ...
        if "EU_EAST" in text_upper or "EU-EAST" in text_upper: target_node = "DC_EU_EAST"
        elif "UK_SOUTH" in text_upper or "UK-SOUTH" in text_upper: target_node = "DC_UK_SOUTH"
        elif "AUTH" in text_upper: target_node = "AUTH_MODULE_v2"
        elif "LOG" in text_upper or "LIB" in text_upper: target_node = "OPEN_SOURCE_LOGGING_LIB"
        elif "PORTAL" in text_upper or "GOV" in text_upper: target_node = "GOV_PORTAL_CORE"
        elif "PRIME" in text_upper or "ALPHA" in text_upper: target_node = "PRIME_ALPHA"
        elif "SUB" in text_upper or "BETA" in text_upper: target_node = "SUB_BETA"
        
        if target_node != "UNKNOWN":
            execution_logs.append(f"[Analyst Agent Safety Net] Keyword scanner caught explicit node token: '{target_node}'")

    return target_node