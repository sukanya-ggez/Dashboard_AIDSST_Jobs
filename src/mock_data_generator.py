import pandas as pd
import numpy as np
import os

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

np.random.seed(42)

def generate_ipeds_supply():
    # Universities
    unis = ["Tech University", "State College", "National Institute of Science", "Global Tech"]
    programs = [
        {"name": "B.S. Artificial Intelligence", "domain": "AI", "level": "Bachelor", "cip": "11.0102"},
        {"name": "M.S. Data Science", "domain": "DS", "level": "Master", "cip": "30.7001"},
        {"name": "B.S. Data Science", "domain": "DS", "level": "Bachelor", "cip": "30.7001"},
        {"name": "Ph.D. Statistics", "domain": "STAT", "level": "Doctoral", "cip": "27.0501"},
        {"name": "M.S. Applied Statistics", "domain": "STAT", "level": "Master", "cip": "27.0501"}
    ]
    
    data = []
    for year in [2022, 2023, 2024, 2025]:
        for uni in unis:
            for p in programs:
                graduates = np.random.randint(10, 150)
                tuition = np.random.randint(10000, 50000)
                emp_yr1 = min(graduates, int(graduates * np.random.uniform(0.6, 0.9)))
                emp_yr2 = min(graduates, int(graduates * np.random.uniform(0.7, 0.95)))
                emp_yr3 = min(graduates, int(graduates * np.random.uniform(0.8, 0.98)))
                
                data.append({
                    "year": year,
                    "institution": uni,
                    "program_name": p["name"],
                    "domain": p["domain"],
                    "degree_level": p["level"],
                    "cip_code": p["cip"],
                    "graduates": graduates,
                    "tuition_usd": tuition,
                    "employed_year_1": emp_yr1,
                    "employed_year_2": emp_yr2,
                    "employed_year_3": emp_yr3,
                    "country": "USA"
                })
                
    df = pd.DataFrame(data)
    df.to_csv(f"{RAW_DIR}/ipeds_graduates.csv", index=False)
    print("Generated ipeds_graduates.csv")

def generate_oews_demand():
    years = [2022, 2023, 2024, 2025]
    soc_codes = [
        {"soc": "15-1221", "title": "AI / ML Researcher (Proxy)", "domain": "AI"},
        {"soc": "15-2051", "title": "Data Scientist", "domain": "DS"},
        {"soc": "15-2041", "title": "Statistician", "domain": "STAT"}
    ]
    
    data = []
    for y in years:
        for s in soc_codes:
            emp = np.random.randint(20000, 300000)
            median_pay = np.random.randint(90000, 150000)
            p10_pay = median_pay * 0.6  # entry proxy
            data.append({
                "year": y,
                "soc_code": s["soc"],
                "job_title": s["title"],
                "domain": s["domain"],
                "employment": emp,
                "median_salary": median_pay,
                "p10_salary": p10_pay,
                "country": "USA"
            })
            
    df = pd.DataFrame(data)
    df.to_csv(f"{RAW_DIR}/oews_employment.csv", index=False)
    print("Generated oews_employment.csv")

def generate_skills_data():
    skills = [
        {"skill": "Python", "category": "Programming"},
        {"skill": "SQL", "category": "Database"},
        {"skill": "R", "category": "Programming"},
        {"skill": "Machine Learning", "category": "Machine Learning"},
        {"skill": "Deep Learning", "category": "AI / Deep Learning"},
        {"skill": "Statistics", "category": "Statistics & Mathematics"},
        {"skill": "Data Visualization", "category": "Visualization / BI"},
        {"skill": "Cloud (AWS/GCP)", "category": "Cloud"},
        {"skill": "Generative AI", "category": "Generative AI / LLM"}
    ]
    
    # Supply skills (what courses teach)
    course_skills = []
    programs = ["B.S. Artificial Intelligence", "M.S. Data Science", "B.S. Data Science", "Ph.D. Statistics", "M.S. Applied Statistics"]
    for p in programs:
        for s in skills:
            if np.random.rand() > 0.3: # 70% chance a program teaches a skill
                course_skills.append({
                    "program_name": p,
                    "skill_name": s["skill"],
                    "skill_category": s["category"],
                    "mapping_score": np.random.uniform(0.5, 1.0)
                })
    pd.DataFrame(course_skills).to_csv(f"{RAW_DIR}/course_skills.csv", index=False)
    
    # Demand skills (what jobs want)
    job_skills = []
    roles = ["AI", "DS", "STAT"]
    levels = ["Entry", "Intermediate", "Expert"]
    for r in roles:
        for lvl in levels:
            for s in skills:
                demand_pct = np.random.uniform(10, 90)
                job_skills.append({
                    "domain": r,
                    "career_level": lvl,
                    "skill_name": s["skill"],
                    "skill_category": s["category"],
                    "demand_pct": demand_pct
                })
    pd.DataFrame(job_skills).to_csv(f"{RAW_DIR}/job_skills_demand.csv", index=False)
    print("Generated skills datasets")

def generate_job_postings():
    companies = ["Google", "Microsoft", "Amazon", "Local Bank", "Health Corp", "Startup AI"]
    titles = ["Junior Data Analyst", "Data Scientist", "Senior ML Engineer", "Lead Statistician", "AI Researcher"]
    
    data = []
    for _ in range(500):
        c = np.random.choice(companies)
        t = np.random.choice(titles)
        if "Junior" in t or "Intern" in t:
            lvl = "Entry"
            sal = np.random.randint(60000, 90000)
        elif "Senior" in t or "Lead" in t or "Researcher" in t:
            lvl = "Expert"
            sal = np.random.randint(130000, 200000)
        else:
            lvl = "Intermediate"
            sal = np.random.randint(90000, 140000)
            
        if "Data" in t:
            dom = "DS"
        elif "ML" in t or "AI" in t:
            dom = "AI"
        else:
            dom = "STAT"
            
        data.append({
            "year": np.random.choice([2024, 2025]),
            "company": c,
            "job_title": t,
            "career_level": lvl,
            "domain": dom,
            "salary": sal,
            "country": "USA"
        })
    pd.DataFrame(data).to_csv(f"{RAW_DIR}/job_postings.csv", index=False)
    print("Generated job_postings.csv")

if __name__ == "__main__":
    print("Generating mock data for Phase 3...")
    generate_ipeds_supply()
    generate_oews_demand()
    generate_skills_data()
    generate_job_postings()
    print("Done!")
