"""
Repository layer for managing company knowledge in MongoDB.
All direct MongoDB interactions should go through this layer.
"""

from typing import List, Dict, Any, Optional
from pymongo.errors import PyMongoError
from app.database.mongodb import get_company_collection


def get_company(company_name: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve a company document by company name.

    Args:
        company_name: The name of the company to retrieve.

    Returns:
        The company document if found, None otherwise.
    """
    try:
        collection = get_company_collection()
        return collection.find_one({"company_name": company_name})
    except PyMongoError as e:
        # Log the error (in a real app, use logging)
        print(f"Error retrieving company {company_name}: {e}")
        return None


def company_exists(company_name: str) -> bool:
    """
    Check if a company document exists.

    Args:
        company_name: The name of the company to check.

    Returns:
        True if the company exists, False otherwise.
    """
    try:
        collection = get_company_collection()
        return collection.count_documents({"company_name": company_name}, limit=1) > 0
    except PyMongoError as e:
        print(f"Error checking existence of company {company_name}: {e}")
        return False


def insert_company(company_data: Dict[str, Any]) -> bool:
    """
    Insert a new company document.
    Does not insert if a company with the same name already exists.

    Args:
        company_data: The company data to insert.

    Returns:
        True if inserted, False if duplicate or error.
    """
    try:
        collection = get_company_collection()
        # Check for duplicate
        if collection.count_documents({"company_name": company_data.get("company_name")}, limit=1) > 0:
            return False
        result = collection.insert_one(company_data)
        return result.acknowledged
    except PyMongoError as e:
        print(f"Error inserting company {company_data.get('company_name')}: {e}")
        return False


def update_company(company_name: str, updated_fields: Dict[str, Any]) -> bool:
    """
    Update only the provided fields of a company document.
    Does not overwrite the entire document.

    Args:
        company_name: The name of the company to update.
        updated_fields: A dictionary of fields to update.

    Returns:
        True if update was successful, False otherwise.
    """
    try:
        collection = get_company_collection()
        result = collection.update_one(
            {"company_name": company_name},
            {"$set": updated_fields}
        )
        return result.acknowledged and result.modified_count > 0
    except PyMongoError as e:
        print(f"Error updating company {company_name}: {e}")
        return False


def save_chunks(company_name: str, chunks: List[Dict[str, Any]]) -> bool:
    """
    Store or replace the knowledge_chunks field for a company.

    Args:
        company_name: The name of the company.
        chunks: The knowledge chunks to store.

    Returns:
        True if successful, False otherwise.
    """
    try:
        collection = get_company_collection()
        result = collection.update_one(
            {"company_name": company_name},
            {"$set": {"knowledge_chunks": chunks}}
        )
        return result.acknowledged and result.modified_count > 0
    except PyMongoError as e:
        print(f"Error saving chunks for company {company_name}: {e}")
        return False


def save_embeddings(company_name: str, embeddings: List[List[float]]) -> bool:
    """
    Store or replace the embeddings field for a company.

    Args:
        company_name: The name of the company.
        embeddings: The embeddings to store.

    Returns:
        True if successful, False otherwise.
    """
    try:
        collection = get_company_collection()
        result = collection.update_one(
            {"company_name": company_name},
            {"$set": {"embeddings": embeddings}}
        )
        return result.acknowledged and result.modified_count > 0
    except PyMongoError as e:
        print(f"Error saving embeddings for company {company_name}: {e}")
        return False


def update_source_urls(company_name: str, urls: List[str]) -> bool:
    """
    Merge new URLs with existing source_urls for a company.
    Avoids duplicates.

    Args:
        company_name: The name of the company.
        urls: New URLs to add.

    Returns:
        True if successful, False otherwise.
    """
    try:
        collection = get_company_collection()
        # Get existing company
        company = collection.find_one({"company_name": company_name})
        if not company:
            return False

        existing_urls = set(company.get("source_urls", []))
        new_urls = set(urls)
        # Union to avoid duplicates
        merged_urls = list(existing_urls.union(new_urls))

        result = collection.update_one(
            {"company_name": company_name},
            {"$set": {"source_urls": merged_urls}}
        )
        return result.acknowledged and result.modified_count > 0
    except PyMongoError as e:
        print(f"Error updating source URLs for company {company_name}: {e}")
        return False


def delete_company(company_name: str) -> bool:
    """
    Delete a company document.

    Args:
        company_name: The name of the company to delete.

    Returns:
        True if deleted, False otherwise.
    """
    try:
        collection = get_company_collection()
        result = collection.delete_one({"company_name": company_name})
        return result.acknowledged and result.deleted_count > 0
    except PyMongoError as e:
        print(f"Error deleting company {company_name}: {e}")
        return False


def list_companies() -> List[str]:
    """
    Return all stored company names.

    Returns:
        A list of company names.
    """
    try:
        collection = get_company_collection()
        # Distinct company names
        return collection.distinct("company_name")
    except PyMongoError as e:
        print(f"Error listing companies: {e}")
        return []