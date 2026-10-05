# Dashboard: AI / Data Science / Statistics — Graduate Supply, Job Demand & Skills Mismatch

## 📌 Project Overview
This project aims to build an interactive analytical dashboard using **Python, Dash, and Plotly** to explore and connect three main aspects of the AI, Data Science, and Statistics fields:
1. **Graduate Supply:** How many students are graduating, from which programs, what skills they learn, and how quickly they get employed.
2. **Job Demand:** How many jobs are available, which companies are hiring, what skills they require, and the salary distributions across career levels.
3. **Skills Mismatch Analysis:** How well the skills taught in academic programs align with the skills demanded by the job market.

The dashboard serves as a tool for students, educators, career advisors, and curriculum developers to understand the current workforce and education landscape.

## 🎯 Business Objectives
- Visualize the "Supply" of graduates and "Demand" from the labor market.
- Compare tuition costs, graduate employment rates, and program details.
- Identify the most in-demand skills and compare them against university curricula.
- Highlight skill gaps: "skills taught but not demanded" and "skills demanded but not taught enough."
- Provide clear evidence for science communication and workforce planning.

## 🛠️ Technology Stack
- **Backend/Data Processing:** Python 3.11+, Pandas, Polars, Numpy, DuckDB, SQLAlchemy, PyArrow
- **Frontend/Visualization:** Dash, Dash Bootstrap Components, Plotly
- **Advanced Mapping (Future Phase):** Scikit-learn, Rapidfuzz, Sentence-Transformers
- **Data Storage:** Raw data (`/data/raw/`), Processed (`/data/processed/`), Analytics (DuckDB)

## 🗂️ Information Architecture
The dashboard consists of 3 main tabs connected by global filters (Year, Country, Domain, Degree Level, Institution, Career Level, Company, Skill Category):
- **TAB 1: Graduate Supply & Curriculum Skills** (KPIs, Program Graduates, Required Courses & Skills, Employment Outcomes, Tuition)
- **TAB 2: Job Demand & Required Skills** (Job Postings, Top Skills by Career Level, Company Analysis)
- **TAB 3: Skills Mismatch Analysis** (Gap Analysis between Supply and Demand)

## 📊 Data Sources (Open Data)
- **Education Supply:** NCES IPEDS (e.g., Completions C2024_A)
- **Employment & Salary:** BLS OEWS (Occupational Employment and Wage Statistics)
- **Skills & Jobs:** O*NET 31.0, Qarera Skills 2026, Datamata Skill Demand Index, open `data_jobs` datasets.

## 🚀 Getting Started
*(Instructions for environment setup, data pipeline execution, and dashboard deployment will be added here as the implementation progresses.)*
