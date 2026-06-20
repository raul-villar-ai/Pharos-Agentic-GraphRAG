# src/config/__init__.py
"""
Configuration package for Pharos Agentic GraphRAG.
Centralizes system directory paths and dynamic prompt injection structures.
"""

from .paths import (
    ROOT_DIR,
    HISTORY_FILE,
    GOLDEN_SET_PATH,
    EVAL_LOGS_PATH
)
from .prompts import get_analyst_prompt