# src/config/paths.py
import os

# Resolves the absolute path to the Pharos root directory
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CONFIG_DIR, "..", ".."))

# Centralized data ledger and evaluation paths
HISTORY_FILE = os.path.join(ROOT_DIR, "triage_history.json")
GOLDEN_SET_PATH = os.path.join(ROOT_DIR, "tests", "evaluation_golden_set.json")
EVAL_LOGS_PATH = os.path.join(ROOT_DIR, "tests", "eval_performance_history.json")