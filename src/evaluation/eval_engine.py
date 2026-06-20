# src/evaluation/eval_engine.py
import os
import json
from datetime import datetime

# Clean, package-wide imports replacing old sys.path interventions
from src.agents import pharos_intelligent_engine
from src.config import GOLDEN_SET_PATH, EVAL_LOGS_PATH

class PharosLLMOpsEvaluator:
    def __init__(self):
        if not os.path.exists(GOLDEN_SET_PATH):
            raise FileNotFoundError(f"Missing benchmark verification dataset at {os.path.abspath(GOLDEN_SET_PATH)}")

    def run_suite(self) -> dict:
        """Executes full regression tests over the golden benchmark dataset using production code."""
        with open(GOLDEN_SET_PATH, "r", encoding="utf-8") as f:
            test_cases = json.load(f)
            
        print(f"🔬 Ingesting {len(test_cases)} enterprise benchmark cases into Pharos Core Eval Engine...")
        
        results = []
        total_cases = len(test_cases)
        passed_extractions = 0
        deflected_injections = 0
        total_adversarial = 0
        
        for case in test_cases:
            query = case["query"]
            # The test case key is expected_target, coordinator resolves to target_node
            expected = case["expected_target"]
            is_adv = case.get("is_adversarial", False)
            category = case.get("category", "Unassigned")
            
            if is_adv:
                total_adversarial += 1
                
            # Invoke the active multi-agent loop pipeline execution flow
            outputs = pharos_intelligent_engine.invoke({"query": query})
            predicted = outputs["target_node"]
            
            # Evaluate correctness matching bounds
            is_correct = (str(predicted).strip().upper() == str(expected).strip().upper())
            
            if is_correct:
                if is_adv:
                    deflected_injections += 1
                else:
                    passed_extractions += 1
                    
            results.append({
                "case_id": case.get("case_id", "TC-UNK"),
                "category": category,
                "query": query,
                "expected": expected,
                "predicted": predicted,
                "status": "PASSED" if is_correct else "FAILED"
            })
            
        # Metrics score aggregation vector compilation
        total_standard = total_cases - total_adversarial
        extraction_accuracy = (passed_extractions / total_standard * 100) if total_standard > 0 else 0.0
        guardrail_pass_rate = (deflected_injections / total_adversarial * 100) if total_adversarial > 0 else 0.0
        overall_accuracy = ((passed_extractions + deflected_injections) / total_cases * 100) if total_cases > 0 else 0.0
        
        summary_report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metrics": {
                "overall_accuracy_pct": round(overall_accuracy, 2),
                "extraction_accuracy_pct": round(extraction_accuracy, 2),
                "guardrail_deflection_pct": round(guardrail_pass_rate, 2),
                "total_processed": total_cases,
                "passed_count": passed_extractions + deflected_injections,
                "failed_count": total_cases - (passed_extractions + deflected_injections)
            },
            "detailed_runs": results
        }
        
        self._append_log_to_history(summary_report)
        return summary_report

    def _append_log_to_history(self, report: dict):
        """Maintains a versioned audit history ledger of accuracy changes over time."""
        history = []
        if os.path.exists(EVAL_LOGS_PATH):
            try:
                with open(EVAL_LOGS_PATH, "r", encoding="utf-8") as f:
                    history = json.load(f)
            except Exception:
                history = []
                
        history.insert(0, report)
        with open(EVAL_LOGS_PATH, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
            print(f"💾 [Ledger Updated] Accuracy report append finalized to '{EVAL_LOGS_PATH}'.")

# Retained to allow executing verification tests independently
if __name__ == "__main__":
    evaluator = PharosLLMOpsEvaluator()
    report = evaluator.run_suite()
    print("\n==================================================")
    print("      PHAROS SYSTEM REGRESSION AUDIT COMPLETE      ")
    print("==================================================")
    print(f"Overall Blueprint System Accuracy: {report['metrics']['overall_accuracy_pct']}%")
    print(f"Entity Extraction Precision Score: {report['metrics']['extraction_accuracy_pct']}%")
    print(f"Adversarial Injection Deflection Rate: {report['metrics']['guardrail_deflection_pct']}%")
    print("==================================================")