"""
Embedding service for generating text embeddings.
This service is responsible only for generating embeddings using a configurable model.
It does not perform database operations, chunking, or retrieval.
"""

import os
import logging
from typing import List, Union

logger = logging.getLogger(__name__)

# Default model name if not set in environment
DEFAULT_MODEL_NAME = "all-MiniLM-L6-v2"

class EmbeddingService:
    """
    Service for generating embeddings using a sentence-transformers model.
    The model is loaded lazily and cached as a class attribute.
    """
    _model = None
    _model_name = None

    @classmethod
    def _get_model_name(cls) -> str:
        """Get model name from environment variable, with fallback."""
        if cls._model_name is None:
            cls._model_name = os.getenv("EMBEDDING_MODEL", DEFAULT_MODEL_NAME)
        return cls._model_name

    @classmethod
    def _load_model(cls):
        """Load the sentence-transformers model if not already loaded."""
        if cls._model is not None:
            return

        try:
            from sentence_transformers import SentenceTransformer
            model_name = cls._get_model_name()
            logger.info(f"Loading embedding model: {model_name}")
            cls._model = SentenceTransformer(model_name)
            logger.info(f"Embedding model '{model_name}' loaded successfully.")
        except ImportError:
            logger.error(
                "sentence-transformers package is not installed. "
                "Please install it to use the embedding service."
            )
            cls._model = None
        except Exception as e:
            logger.error(f"Failed to load embedding model: {e}")
            cls._model = None

    @classmethod
    def _get_model(cls):
        """Ensure model is loaded and return it."""
        if cls._model is None:
            cls._load_model()
        return cls._model

    @classmethod
    def generate_embedding(cls, text: str) -> List[float]:
        """
        Generate an embedding for a single text string.

        Args:
            text: The input text to embed.

        Returns:
            A list of floats representing the embedding vector.
            Returns an empty list if the model fails to load or an error occurs.
        """
        try:
            model = cls._get_model()
            if model is None:
                logger.warning("Embedding model not available; returning empty embedding.")
                return []
            # Encode returns a numpy array; convert to list of floats
            embedding = model.encode(text, convert_to_numpy=True)
            return embedding.tolist()
        except Exception as e:
            logger.error(f"Error generating embedding for text: {e}")
            return []

    @classmethod
    def generate_embeddings(cls, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of text strings.

        Args:
            texts: A list of input texts to embed.

        Returns:
            A list of embedding vectors (each a list of floats).
            Returns a list of empty lists if the model fails.
        """
        try:
            model = cls._get_model()
            if model is None:
                logger.warning("Embedding model not available; returning empty embeddings.")
                return [[] for _ in texts]
            # Encode returns a numpy array of shape (len(texts), dim)
            embeddings = model.encode(texts, convert_to_numpy=True)
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Error generating embeddings for batch: {e}")
            return [[] for _ in texts]


# Convenience module-level functions for backward compatibility
def generate_embedding(text: str) -> List[float]:
    """
    Generate an embedding for a single text string.
    Delegates to EmbeddingService.generate_embedding.
    """
    return EmbeddingService.generate_embedding(text)


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of text strings.
    Delegates to EmbeddingService.generate_embeddings.
    """
    return EmbeddingService.generate_embeddings(texts)