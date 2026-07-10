"""
Chunking service for splitting text into meaningful chunks.
This service is responsible only for splitting text into chunks.
It does not perform database operations, embedding generation, retrieval, or LLM calls.
"""

import os
import re
from typing import List, Dict, Any

# Default values for chunking
DEFAULT_CHUNK_SIZE = 500
DEFAULT_CHUNK_OVERLAP = 50

def _get_env_int(env_var: str, default: int) -> int:
    """Get integer from environment variable with fallback."""
    try:
        return int(os.getenv(env_var, str(default)))
    except (ValueError, TypeError):
        return default

CHUNK_SIZE = _get_env_int("CHUNK_SIZE", DEFAULT_CHUNK_SIZE)
CHUNK_OVERLAP = _get_env_int("CHUNK_OVERLAP", DEFAULT_CHUNK_OVERLAP)


def _split_into_sentences(text: str) -> List[str]:
    """
    Split text into sentences using regex.
    Handles common sentence endings: . ! ?
    """
    # Split by [.!?] followed by whitespace or end of string
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Filter out empty strings
    return [s.strip() for s in sentences if s.strip()]


def chunk_text(text: str) -> List[str]:
    """
    Split a large text string into clean semantic chunks.
    Attempts to break at sentence boundaries to avoid cutting sentences.

    Args:
        text: The input text to chunk.

    Returns:
        A list of text chunks.
    """
    if not text or not text.strip():
        return []

    # Split text into sentences
    sentences = _split_into_sentences(text)
    if not sentences:
        return [text.strip()]

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_len = len(sentence)

        # If a single sentence exceeds CHUNK_SIZE, we have to include it as-is
        # (better to have an oversized chunk than to cut a sentence)
        if sentence_len > CHUNK_SIZE:
            # Finalize current chunk if it exists
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_length = 0
            # Add the long sentence as its own chunk
            chunks.append(sentence)
            continue

        # Check if adding this sentence would exceed the chunk size
        if current_length + sentence_len > CHUNK_SIZE and current_chunk:
            # Finalize current chunk
            chunks.append(' '.join(current_chunk))

            # Prepare overlap for next chunk
            # We take sentences from the end of current_chunk that fit in CHUNK_OVERLAP
            overlap_sentences = []
            overlap_length = 0
            # Traverse current_chunk in reverse to build overlap
            for s in reversed(current_chunk):
                if overlap_length + len(s) <= CHUNK_OVERLAP:
                    overlap_sentences.insert(0, s)
                    overlap_length += len(s)
                else:
                    break

            # Start new chunk with overlap sentences
            current_chunk = overlap_sentences
            current_length = overlap_length

        # Add sentence to current chunk
        current_chunk.append(sentence)
        current_length += sentence_len

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


def chunk_company_information(company_data: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    Split company information into chunks by field, preserving field type.
    Skips empty fields.

    Args:
        company_data: Dictionary containing company information fields.
                     Expected keys: overview, products_services, tech_stack,
                     work_culture, hiring_information, recent_updates

    Returns:
        List of dictionaries with 'chunk_type' and 'chunk_text' keys.
    """
    chunks = []

    # Define the fields we want to process
    fields_to_process = [
        "overview",
        "products_services",
        "tech_stack",
        "work_culture",
        "hiring_information",
        "recent_updates"
    ]

    for field in fields_to_process:
        value = company_data.get(field)
        # Skip if value is None, empty string, or not a string
        if not value or not isinstance(value, str) or not value.strip():
            continue

        # Split the field value into text chunks
        text_chunks = chunk_text(value)

        # Create a chunk dictionary for each text chunk
        for chunk in text_chunks:
           chunks.append({
              "chunk_type": field,
            "chunk_text": chunk
            })

    return chunks