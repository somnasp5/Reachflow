"""
Company Research Agent - Orchestrates the complete company knowledge pipeline.
"""

import time
import logging
from typing import List, Dict, Any, Union

# Import existing services
from app.repositories.company_repository import (
    get_company,
    company_exists,
    insert_company,
    update_company,
    save_chunks,
    save_embeddings,
    update_source_urls
)
from app.services.chunking_service import chunk_company_information
from app.services.embedding_service import generate_embeddings
from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.google_search_service import search_google
from app.services.company_search_service import get_company_emails

logger = logging.getLogger(__name__)

# Configuration
try:
    DEFAULT_QUERY = "company overview hiring technology work culture internship recruitment"
    RETRIEVAL_QUERY = (
        # In a real app, you might get this from environment variables
        # For now, we'll use a default
        DEFAULT_QUERY
    )
except Exception:
    RETRIEVAL_QUERY = DEFAULT_QUERY

def _google_search_field(company_name: str, field_query: str) -> str:
    """
    Helper function to search for a specific field and return concatenated snippets.
    """
    try:
        query = f"{company_name} {field_query}"
        results = search_google(query)
        snippets = []
        for result in results[:3]:  # Top 3 results
            snippet = result.get("snippet", "")
            if snippet:
                snippets.append(snippet)
        return " ".join(snippets)
    except Exception as e:
        logger.error(f"Error searching for field '{field_query}' for company {company_name}: {e}")
        return ""

def _collect_company_data(company_name: str) -> Dict[str, Any]:
    """
    Collects company information from Google Search for various fields.
    Returns a dictionary with the field values and source URLs.
    """
    fields = {
        "overview": "company overview",
        "products_services": "products and services",
        "tech_stack": "technology stack",
        "work_culture": "work culture",
        "hiring_information": "hiring information",
        "recent_updates": "latest news"
    }

    company_data = {}
    all_urls = set()

    for field, query in fields.items():
        try:
            # Search for the field
            query_str = f"{company_name} {query}"
            results = search_google(query_str)

            # Collect snippets
            snippets = []
            for result in results:
                snippet = result.get("snippet", "")
                if snippet:
                    snippets.append(snippet)
                link = result.get("link", "")
                if link:
                    all_urls.add(link)

            company_data[field] = " ".join(snippets)

            # Log completion for this field (optional)
            logger.debug(f"Google Search completed for {company_name} - {field}")
        except Exception as e:
            logger.error(f"Error collecting {field} for {company_name}: {e}")
            company_data[field] = ""

    return {
        "data": company_data,
        "source_urls": list(all_urls)
    }

def _merge_company_data(existing: dict, new_data: dict, new_urls: list) -> dict:
    """
    Merges new company data with existing data, avoiding duplicates where possible.
    For text fields, we append new text if it's not already contained in the existing text.
    For source_urls, we use the repository's update_source_urls function (handled elsewhere).
    """
    merged = existing.copy()

    for field, new_value in new_data.items():
        if not new_value:  # Skip if new value is empty
            continue

        existing_value = merged.get(field, "")
        if not existing_value:
            # If existing is empty, just use new
            merged[field] = new_value
        else:
            # Simple deduplication: if new value is not already in existing, append
            # This is a basic approach; in reality, we might want more sophisticated deduplication
            if new_value not in existing_value:
                merged[field] = f"{existing_value} {new_value}".strip()
            # Otherwise, keep existing (to avoid duplication)

    return merged

def company_research_agent(state):
    """
    Orchestrates the company knowledge pipeline for each company in the state.
    """
    print("\n--- COMPANY RESEARCH AGENT RUNNING ---")
    # Assuming the logger is set up elsewhere; we'll use print for simplicity as in original
    # But we also have logger configured above

    researched_companies = state["researched_companies"]
    updated_companies = []

    for company_item in researched_companies:
        try:
            # Extract company name - handle both string and dict formats
            if isinstance(company_item, str):
                company_name = company_item
                job_title = ""  # Default if not provided
                existing_email = ""  # Not applicable
            elif isinstance(company_item, dict):
                company_name = company_item.get("company_name", "")
                job_title = company_item.get("job_title", "")
                existing_email = company_item.get("company_email", "")
            else:
                # Skip invalid items
                logger.warning(f"Skipping invalid company item: {company_item}")
                continue

            if not company_name:
                logger.warning("Skipping company with empty name")
                continue

            print(f"Processing company: {company_name}")

            # Step 1 & 2: Perform fresh Google Search and collect company information
            search_result = _collect_company_data(company_name)
            company_data = search_result["data"]
            new_urls = search_result["source_urls"]

            # Get company email using existing service
            email_list = get_company_emails(company_name)
            company_email = email_list[0] if email_list else ""
            if company_email:
                print(f"  Found company email: {company_email}")
            else:
                print(f"  No company email found")

            # Step 3: Check if company exists in MongoDB
            exists = company_exists(company_name)
            if exists:
                print(f"  Company '{company_name}' exists in database - merging data")
                existing_company = get_company(company_name)
                if existing_company:
                    # Merge the data
                    merged_data = _merge_company_data(existing_company, company_data, new_urls)
                    # Update the company document (excluding chunks and embeddings for now)
                    # We'll update the fields and source_urls separately
                    update_fields = {k: v for k, v in merged_data.items()
                                   if k not in ["_id", "knowledge_chunks", "embeddings", "created_at"]}
                    update_success = update_company(company_name, update_fields)
                    if update_success:
                        # Update source URLs (this merges and avoids duplicates)
                        url_update_success = update_source_urls(company_name, new_urls)
                        if url_update_success:
                            print("  Knowledge merged and source URLs updated")
                        else:
                            print("  Knowledge merged but failed to update source URLs")
                    else:
                        print("  Failed to update company data")
                        # Continue with merged data for embedding storage
                    # Use merged data for further processing
                    company_data = merged_data
                else:
                    print(f"  Could not retrieve existing company {company_name}, proceeding with new data")
            else:
                print(f"  Company '{company_name}' not found in database - creating new entry")

            # Prepare company document for storage
            timestamp = time.time()
            company_doc = {
                "company_name": company_name,
                "last_updated": timestamp,
                **company_data  # Includes all the fields we collected
            }
            # Add source_urls separately to avoid overlap in the merge above
            company_doc["source_urls"] = new_urls

            if not exists:
                company_doc["created_at"] = timestamp
                insert_success = insert_company(company_doc)
                if not insert_success:
                    print(f"  Failed to insert new company {company_name}")
                    # Continue anyway to try to store chunks/embeddings?
                else:
                    print(f"  New company {company_name} inserted")

            # Step 4: Pass the merged information to the chunking service
            # We need to pass only the fields that chunk_company_information expects
            chunkable_data = {
                k: v for k, v in company_doc.items()
                if k in ["overview", "products_services", "tech_stack",
                        "work_culture", "hiring_information", "recent_updates"]
                and isinstance(v, str) and v.strip()
            }
            chunks = chunk_company_information(chunkable_data)
            if chunks:
                print(f"  Chunks created: {len(chunks)}")
            else:
                print(f"  No chunks created for {company_name}")
                chunks = []  # Ensure we have an empty list

            # Step 5: Generate embeddings for every chunk
            if chunks:
                chunk_texts = [chunk["chunk_text"] for chunk in chunks]
                embeddings = generate_embeddings(chunk_texts)
                if embeddings and all(embeddings):  # Check if we got valid embeddings
                    print(f"  Embeddings generated: {len(embeddings)}")
                else:
                    print(f"  Failed to generate embeddings for {company_name}")
                    embeddings = [[]] * len(chunks)  # Placeholder to avoid index errors
            else:
                embeddings = []

            # Step 6: Store chunks and embeddings using the repository
            if chunks:
                # Store chunks
                chunks_to_store = [
                    {"chunk_type": chunk["chunk_type"], "chunk_text": chunk["chunk_text"]}
                    for chunk in chunks
                ]
                chunks_saved = save_chunks(company_name, chunks_to_store)
                # Store embeddings
                embeddings_saved = save_embeddings(company_name, embeddings)
                if chunks_saved and embeddings_saved:
                    print("  Knowledge stored (chunks and embeddings)")
                else:
                    print("  Failed to store chunks or embeddings")
            else:
                print("  No chunks to store")

            # Step 7: Retrieve the most relevant chunks using the retrieval service
            if chunks:  # Only retrieve if we have chunks
                retrieved_chunks = retrieve_relevant_chunks(
                    company_name=company_name,
                    query=RETRIEVAL_QUERY,
                    top_k=5  # Could be made configurable
                )
                if retrieved_chunks:
                    # Combine the chunk texts into a context string
                    context_parts = [
                        chunk["chunk_text"] for chunk in retrieved_chunks
                        if chunk.get("chunk_text")
                    ]
                    retrieved_context = " ".join(context_parts)
                    print(f"  Relevant context retrieved: {len(context_parts)} chunks")
                else:
                    retrieved_context = ""
                    print("  No relevant chunks found")
            else:
                retrieved_context = ""
                print("  No chunks available for retrieval")

            # Step 8: Prepare the output for this company
            # Get the latest company document to ensure we have the stored source_urls and timestamps
            latest_company = get_company(company_name)
            source_urls = []
            last_updated = timestamp  # fallback
            if latest_company:
                source_urls = latest_company.get("source_urls", [])
                last_updated = latest_company.get("last_updated", timestamp)

            company_output = {
                "company_name": company_name,
                "job_title": job_title,  # From input or default
                "company_email": company_email,
                "retrieved_context": retrieved_context,
                "source_urls": source_urls,
                "last_updated": last_updated
            }
            updated_companies.append(company_output)

        except Exception as e:
            logger.error(f"Error processing company {company_name if 'company_name' in locals() else 'unknown'}: {e}")
            print(f"  Error processing company: {e}")
            # Continue with the next company
            # Optionally, we could append the original item or a placeholder?
            # For now, we'll skip adding this company to the output to avoid breaking the flow
            # But we should still return something for this company? Let's append the original item
            # to maintain the same length? The requirement says to continue processing others.
            # We'll append the original item so the count remains the same.
            if isinstance(company_item, str):
                updated_companies.append(company_item)
            elif isinstance(company_item, dict):
                updated_companies.append(company_item)

    print(f"  Processed {len(updated_companies)} companies")
    return {
        "researched_companies": updated_companies
    }