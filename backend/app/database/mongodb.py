import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable is not set")

# Create a MongoClient
client = MongoClient(MONGODB_URI)

# Get the database (we'll use a default database name, or we can get from env)
DB_NAME = os.getenv("MONGODB_DB_NAME", "placementgpt")
db = client[DB_NAME]

# Get the company knowledge collection
company_collection = db["company_knowledge"]

def get_company_collection():
    return company_collection

def close_db_connection():
    client.close()