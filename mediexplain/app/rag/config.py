# app/rag/config.py

import os

# Project root: folder that contains app/, html/, mediexplain_chromadb/, etc.
# __file__ is app/rag/config.py → go up three levels
_BASE = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(_BASE))

# --------- DATA LOCATIONS ---------
HTML_DIR = os.path.join(BASE_DIR, "html")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "mediexplain_chromadb")
COLLECTION_NAME = "MediExplainPMC"

# --------- CHUNKING ---------
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# --------- MODELS ---------
EMBED_MODEL = "text-embedding-3-small"
RAG_LLM_MODEL = "gpt-4o-mini"
