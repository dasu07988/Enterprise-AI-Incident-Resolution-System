from __future__ import annotations

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# ------------------------------------------------------
# Configuration
# ------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

load_dotenv(PROJECT_ROOT / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX", "apexpay-incident-kb")

# ------------------------------------------------------
# Logging
# ------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ------------------------------------------------------
# Validation
# ------------------------------------------------------

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY missing.")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY missing.")

# ------------------------------------------------------
# Embeddings
# ------------------------------------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY,
)

# ------------------------------------------------------
# Vector Store
# ------------------------------------------------------

vectorstore = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=PINECONE_API_KEY,
)

# ------------------------------------------------------
# Query
# ------------------------------------------------------

QUERY = "Users cannot establish a VPN connection to the corporate network."

TOP_K = 3

# ------------------------------------------------------
# Main
# ------------------------------------------------------

def main():

    logger.info("Running semantic retrieval test...")

    results = vectorstore.similarity_search_with_score(
        QUERY,
        k=TOP_K,
    )

    print("\n" + "=" * 80)
    print("Semantic Retrieval Results")
    print("=" * 80)
    print(f"\nQuery:\n{QUERY}\n")

    for i, (doc, score) in enumerate(results, start=1):

        print("-" * 80)
        print(f"Result #{i}")
        print(f"Score      : {score}")
        print(f"Category   : {doc.metadata.get('category')}")
        print(f"Filename   : {doc.metadata.get('filename')}")
        print(f"Source     : {doc.metadata.get('source')}")
        print(f"Chunk      : {doc.metadata.get('chunk')}")
        print("\nPreview\n")
        print(doc.page_content[:500])
        print()

    logger.info("Semantic retrieval completed successfully.")


if __name__ == "__main__":
    main()