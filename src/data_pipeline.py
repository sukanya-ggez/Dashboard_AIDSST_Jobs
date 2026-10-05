import os
import duckdb
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
DB_PATH = f"{PROCESSED_DIR}/dashboard.duckdb"

os.makedirs(PROCESSED_DIR, exist_ok=True)

def build_database():
    print(f"Connecting to DuckDB at {DB_PATH}...")
    conn = duckdb.connect(DB_PATH)
    
    # Check if raw files exist
    required_files = [
        "ipeds_graduates.csv",
        "oews_employment.csv",
        "course_skills.csv",
        "job_skills_demand.csv",
        "job_postings.csv"
    ]
    
    for f in required_files:
        if not os.path.exists(f"{RAW_DIR}/{f}"):
            print(f"Warning: {f} not found in {RAW_DIR}. Please ensure raw data is available.")
            return

    print("Loading data into DuckDB...")
    
    # Load ipeds_graduates
    conn.execute(f"CREATE TABLE IF NOT EXISTS graduate_supply AS SELECT * FROM read_csv_auto('{RAW_DIR}/ipeds_graduates.csv')")
    
    # Load oews_employment
    conn.execute(f"CREATE TABLE IF NOT EXISTS job_demand AS SELECT * FROM read_csv_auto('{RAW_DIR}/oews_employment.csv')")
    
    # Load skills
    conn.execute(f"CREATE TABLE IF NOT EXISTS course_skills AS SELECT * FROM read_csv_auto('{RAW_DIR}/course_skills.csv')")
    conn.execute(f"CREATE TABLE IF NOT EXISTS job_skills_demand AS SELECT * FROM read_csv_auto('{RAW_DIR}/job_skills_demand.csv')")
    
    # Load job postings
    conn.execute(f"CREATE TABLE IF NOT EXISTS job_postings AS SELECT * FROM read_csv_auto('{RAW_DIR}/job_postings.csv')")
    
    print("Database built successfully!")
    
    # Verify tables
    tables = conn.execute("SHOW TABLES").fetchall()
    print("Tables created:", [t[0] for t in tables])
    
    conn.close()

if __name__ == "__main__":
    build_database()
