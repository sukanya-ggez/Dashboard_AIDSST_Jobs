import os
import duckdb
import pandas as pd
import requests

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
DB_PATH = f"{PROCESSED_DIR}/dashboard.duckdb"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def download_file(url, local_path):
    print(f"Downloading {url} to {local_path}...")
    # NOTE: You may need to uncomment and run this if files aren't manually downloaded.
    # response = requests.get(url)
    # with open(local_path, "wb") as f:
    #     f.write(response.content)

def ingest_ipeds():
    print("Ingesting IPEDS data...")
    # For example: https://nces.ed.gov/ipeds/datacenter/data/C2024_A.zip
    # Needs to extract and filter CIP 11.0102, 30.7001, 27.0501

def ingest_nextgig():
    print("Ingesting NextGig Job Postings...")
    # URL: https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats/resolve/main/nextgig_jobs_2026-06.parquet

def ingest_pseo():
    print("Fetching PSEO Data via Census API...")
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("CENSUS_API_KEY")
    if not api_key:
        print("Warning: CENSUS_API_KEY not found in .env. Skipping PSEO fetch.")
    else:
        print("Using Census API Key to fetch Y1, Y5, Y10 earnings.")

def build_database():
    print(f"Connecting to DuckDB at {DB_PATH}...")
    conn = duckdb.connect(DB_PATH)
    
    # Run ingestions
    ingest_ipeds()
    ingest_nextgig()
    ingest_pseo()
    
    # Wait for the user to provide the raw CSV/Parquet/ZIP files or implement the full Python downloader
    print("Database build complete (Skeleton).")
    conn.close()

if __name__ == "__main__":
    build_database()
