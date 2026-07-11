"""
Enterprise AI Incident Resolution System
Knowledge Base Ingestion Pipeline

Features
--------
✓ Recursively loads all Markdown files
✓ Splits using RecursiveCharacterTextSplitter
✓ Rich metadata
✓ Google Gemini Embeddings
✓ Pinecone latest SDK
✓ LangChain Pinecone Vector Store
✓ Batch uploads
✓ Progress bars
✓ Duplicate-safe IDs
✓ Production logging

Directory

project/
│
├── knowledge-base/
│     ├── aws/
│     ├── azure/
│     ├── kubernetes/
│     └── ...
│
├── upload_to_pinecone.py
├── .env
└── requirements.txt
"""

from __future__ import annotations

import hashlib
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from tqdm import tqdm

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# ------------------------------------------------------
# Configuration
# ------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(PROJECT_ROOT / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX", "apexpay-incident-kb")

# Absolute path to knowledge-base folder
KNOWLEDGE_BASE = PROJECT_ROOT / "knowledge-base"


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

BATCH_SIZE = 100

# ------------------------------------------------------
# Logging
# ------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

print("Google Key:", GOOGLE_API_KEY[:10] + "..." if GOOGLE_API_KEY else None)
print("Pinecone Key:", PINECONE_API_KEY[:10] + "..." if PINECONE_API_KEY else None)
print("Index:", INDEX_NAME)
print("Knowledge Base:", KNOWLEDGE_BASE.resolve())


# ------------------------------------------------------
# Validation
# ------------------------------------------------------

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY missing.")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY missing.")

if not KNOWLEDGE_BASE.exists():
    raise FileNotFoundError("knowledge-base folder not found.")

# ------------------------------------------------------
# Embedding Model
# ------------------------------------------------------
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY,
)
# ------------------------------------------------------
# Pinecone Vector Store
# ------------------------------------------------------

vectorstore = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=PINECONE_API_KEY,
)

# ------------------------------------------------------
# Text Splitter
# ------------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=[
        "\n# ",
        "\n## ",
        "\n### ",
        "\n\n",
        "\n",
        ". ",
        " ",
        "",
    ],
)

# ------------------------------------------------------
# Load Markdown Files
# ------------------------------------------------------


def load_markdown_documents():

    documents = []

    md_files = list(KNOWLEDGE_BASE.rglob("*.md"))

    logger.info(f"Found {len(md_files)} markdown files.")

    for path in tqdm(md_files):

        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        relative_path = path.relative_to(KNOWLEDGE_BASE)

        metadata = {
            "source": str(relative_path),
            "filename": path.name,
            "category": (
                relative_path.parts[0]
                if len(relative_path.parts) > 1
                else "general"
            ),
            "filetype": "markdown",
        }

        documents.append(
            Document(
                page_content=text,
                metadata=metadata,
            )
        )

    return documents


# ------------------------------------------------------
# Chunk Documents
# ------------------------------------------------------


def split_documents(documents):

    chunks = splitter.split_documents(documents)

    logger.info(f"Created {len(chunks)} chunks.")

    for i, chunk in enumerate(chunks):

        chunk.metadata["chunk"] = i

        uid = hashlib.sha256(
            (
                chunk.metadata["source"]
                + str(i)
                + chunk.page_content[:100]
            ).encode()
        ).hexdigest()

        chunk.metadata["id"] = uid

    return chunks


# ------------------------------------------------------
# Upload
# ------------------------------------------------------


def upload(chunks):

    logger.info("Uploading to Pinecone...")

    total = len(chunks)

    for i in tqdm(range(0, total, BATCH_SIZE)):

        batch = chunks[i : i + BATCH_SIZE]

        ids = [doc.metadata["id"] for doc in batch]

        vectorstore.add_documents(
            documents=batch,
            ids=ids,
        )

    logger.info("Upload complete.")


# ------------------------------------------------------
# Main
# ------------------------------------------------------


def main():

    docs = load_markdown_documents()

    chunks = split_documents(docs)

    upload(chunks)

    logger.info("Knowledge base successfully indexed.")


if __name__ == "__main__":
    main()
    