"""
Retrieval service for retrieving relevant company knowledge chunks.
This service is responsible only for retrieving relevant chunks using embeddings.
It does not perform Google search, modify MongoDB, call LLMs, or generate emails.
"""

import os
import logging
from typing import List, Dict, Any, Tuple
import numpy as np

# Import existing services
from app.repositories.company_repository import get_company
from app.services.embedding_service import generate_embedding

logger = logging.getLogger(__name__)

# Configuration
try:
    TOP_K = int(os.getenv("TOP_K", "5"))
except ValueError:
    TOP_K = 5
    logger.warning("Invalid TOP_K environment variable, defaulting to 5")


def compute_cosine_similarity(embedding1: List[float], embedding2: List[float]) -> float:
    """
    Compute cosine similarity between two embeddings.

    Args:
        embedding1: First embedding vector.
        embedding2: Second embedding vector.

    Returns:
        Cosine similarity score between -1 and 1. Returns 0.0 on error.
    """
    try:
        # Convert to numpy arrays for efficient computation
        vec1 = np.array(embedding1, dtype=np.float32)
        vec2 = np.array(embedding2, dtype=np.float32)

        # Compute dot product
        dot_product = np.dot(vec1, vec2)
        # Compute norms
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)

        # Avoid division by zero
        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0

        similarity = dot_product / (norm1 * norm2)
        # Ensure the result is within valid range due to floating point errors
        return float(max(-1.0, min(1.0, similarity)))
    except Exception as e:
        logger.error(f"Error computing cosine similarity: {e}")
        return 0.0


def rank_chunks(
    chunks: List[Dict[str, Any]],
    query_embedding: List[float],
    embeddings: List[List[float]]
) -> List[Dict[str, Any]]:
    """
    Rank chunks by similarity to the query embedding.

    Args:
        chunks: List of chunk dictionaries with 'chunk_type' and 'chunk_text'.
        query_embedding: Embedding of the query.
        embeddings: List of embeddings corresponding to each chunk.

    Returns:
        List of chunks sorted by similarity score (descending), each with added 'score'.
    """
    if not chunks or not embeddings or len(chunks) != len(embeddings):
        logger.warning("Mismatch between chunks and embeddings lengths.")
        return []

    scored_chunks = []
    for chunk, embedding in zip(chunks, embeddings):
        # Skip if embedding is empty or invalid
        if not embedding or not isinstance(embedding, list):
            continue
        score = compute_cosine_similarity(query_embedding, embedding)
        # Only include chunks with a positive similarity score (optional threshold)
        # For now, we include all and let top_k filter
        scored_chunks.append({
            **chunk,
            "score": score
        })

    # Sort by score descending
    scored_chunks.sort(key=lambda x: x["score"], reverse=True)
    return scored_chunks


def retrieve_relevant_chunks(
    company_name: str,
    query: str,
    top_k: int = TOP_K
) -> List[Dict[str, Any]]:
    """
    Retrieve the top-k most relevant chunks for a company given a query.

    Steps:
    1. Fetch company document from repository.
    2. Extract knowledge_chunks and embeddings.
    3. Generate embedding for the query.
    4. Compute similarity and rank chunks.
    5. Return top_k chunks with scores.

    Args:
        company_name: Name of the company to search.
        query: The query text to embed and compare.
        top_k: Number of top results to return (default from TOP_K env var).

    Returns:
        List of dicts, each containing:
            - chunk_type: The field the chunk came from.
            - chunk_text: The text chunk.
            - score: Cosine similarity score.
        Returns empty list on error or if no data.
    """
    try:
        # 1. Get company document
        company = get_company(company_name)
        if not company:
            logger.warning(f"Company '{company_name}' not found in database.")
            return []

        # 2. Get chunks and embeddings
        chunks = company.get("knowledge_chunks", [])
        embeddings = company.get("embeddings", [])

        if not chunks or not embeddings:
            logger.warning(f"No chunks or embeddings found for company '{company_name}'.")
            return []

        if len(chunks) != len(embeddings):
            logger.warning(
                f"Mismatch in chunks ({len(chunks)}) and embeddings ({len(embeddings)}) "
                f"for company '{company_name}'."
            )
            # We could truncate to the shorter length, but for safety return empty.
            return []

        # 3. Generate query embedding
        query_embedding = generate_embedding(query)
        if not query_embedding:
            logger.warning(f"Failed to generate embedding for query: '{query}'")
            return []

        # 4. Rank chunks by similarity
        ranked_chunks = rank_chunks(chunks, query_embedding, embeddings)

        # 5. Return top_k
        return ranked_chunks[:top_k]

    except Exception as e:
        logger.error(f"Unexpected error in retrieve_relevant_chunks: {e}")
        return []