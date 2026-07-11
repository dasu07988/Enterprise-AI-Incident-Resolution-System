"""
config.py

Enterprise AI Incident Resolution System
Knowledge Base Ingestion Configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ============================================================
# Google Gemini Configuration
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ============================================================
# Pinecone Configuration
# ============================================================

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# Default namespace
NAMESPACE = "__default__"

# ============================================================
# Knowledge Base Configuration
# ============================================================

KNOWLEDGE_BASE_PATH = "../knowledge-base"

SUPPORTED_FILE_TYPES = [
    ".md"
]

# ============================================================
# Text Chunking Configuration
# ============================================================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ============================================================
# Embedding Model
# ============================================================

EMBEDDING_MODEL = "models/text-embedding-004"

# ============================================================
# Validation
# ============================================================

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please configure your .env file."
    )

if not PINECONE_API_KEY:
    raise ValueError(
        "PINECONE_API_KEY not found. Please configure your .env file."
    )

if not PINECONE_INDEX:
    raise ValueError(
        "PINECONE_INDEX not found. Please configure your .env file."
    )