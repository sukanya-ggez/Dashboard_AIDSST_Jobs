# BRD — AI / Data Science / Statistics Dashboard
## Real Data Edition — สำหรับส่งต่อให้ Antigravity

**Version:** 2.0 — Real Data Only  
**Backend:** Python  
**Dashboard:** Plotly + Dash  
**Analytical storage:** DuckDB + Parquet  
**Default education geography:** United States  
**Default labor-market geography:** United States where supported by source  
**Rule สำคัญ:** Production dashboard **ห้ามใช้ mock / synthetic / randomly generated data**  
**ทุกกราฟต้องมี Ref ที่ผู้ใช้กดเปิด source ได้**

---

# 1. Business Goal

Dashboard นี้ต้องตอบคำถามหลัก 2 ข้อ และมี Tab 3 เพื่อเชื่อมข้อมูลทั้งสองฝั่ง

1. **ปริมาณคนที่จบและ Skills ที่เรียนมา**
2. **ปริมาณงานที่จ้างและ Skills ที่ต้องการ**
3. **Skills Mismatch** — เปรียบเทียบ Skills ที่หลักสูตรสอนกับ Skills ที่ตลาดต้องการ

แนวคิดหลัก:

```text
EDUCATION SUPPLY
จำนวนผู้จบ
→ หลักสูตร / สาขา
→ วิชาบังคับ
→ Skills ที่เรียน
→ ค่าเทอม
→ Employment Outcomes

VERSUS

LABOR DEMAND
จำนวนตำแหน่ง
→ Skills ที่ต้องการ
→ บริษัทที่รับ
→ Seniority
→ เงินเดือน

THEN

SKILLS MISMATCH
Demand Skill - Supply Skill
```

---

# 2. Non-Negotiable Data Rules

Antigravity ต้องปฏิบัติตามกฎนี้ทุกข้อ

1. ใช้ข้อมูลจริงจาก source ที่ระบุใน BRD นี้
2. ห้ามเติมข้อมูลที่ไม่มีใน source
3. ห้ามสร้าง Year 2 / Year 3 employment data ด้วย interpolation
4. ห้ามใช้ mock data ใน production
5. ทุก record ที่ผ่าน ETL ต้องมี `source_name`, `source_url`, `source_date`
6. ทุกกราฟต้องมีปุ่ม **Open source / เปิดแหล่งข้อมูล**
7. ทุก tooltip ต้องระบุอย่างน้อย `source` และ `data year/snapshot`
8. ถ้าข้อมูลไม่มี ให้แสดง `N/A` ไม่ใช่ `0`
9. ห้ามรวม `graduates`, `employment stock`, `annual openings`, `job postings` เป็น metric เดียว
10. ห้ามเรียก SOC 15-1221 ว่า “AI jobs ทั้งหมด” — ให้ใช้คำว่า **AI-related occupation proxy**

---

# 3. Important Change from Original Requirement

Requirement เดิมต้องการ:

```text
จำนวนบัณฑิตที่ได้งานในปีที่ 1
ปีที่ 2
ปีที่ 3
หลังเรียนจบ
```

แต่ **U.S. Census PSEO ซึ่งเป็น official public data ไม่มี Year 2 และ Year 3 แบบเทียบได้ทั่วชุดข้อมูล**

PSEO มี employment/earnings outcomes ที่:

```text
Year 1
Year 5
Year 10
```

ดังนั้น Production Dashboard ให้เปลี่ยนกราฟเป็น:

> **จำนวนบัณฑิตที่มีงานทำหลังจบ Year 1 / Year 5 / Year 10**

ถ้าต้องการคง UI Year 1 / Year 2 / Year 3 ให้แสดง:

```text
Year 1 = real data
Year 2 = N/A — source does not publish this measure
Year 3 = N/A — source does not publish this measure
```

**ห้ามประมาณค่า Year 2 หรือ Year 3**

Official PSEO documentation:  
https://www.census.gov/data/developers/data-sets/pseo.html

PSEO Earnings variables:  
https://api.census.gov/data/timeseries/pseo/earnings/variables.html

PSEO Flows variables:  
https://api.census.gov/data/timeseries/pseo/flows/variables.html

---

# 4. Real Data Source Registry

| ID | Source | ใช้กับ | Status / License | เปิดดู |
|---|---|---|---|---|
| SRC01 | NCES IPEDS Completions | จำนวนวุฒิ/ผู้จบ | U.S. official public data | https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7 |
| SRC02 | NCES CIP 2020 | นิยาม AI / DS / Statistics | U.S. official | https://nces.ed.gov/ipeds/cipcode/browse.aspx?y=56 |
| SRC03 | NCES IPEDS Cost | ค่าเทอม/fees ระดับสถาบัน | U.S. official public data | https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7 |
| SRC04 | U.S. Census PSEO | Employment outcomes หลังเรียนจบ | U.S. Census official | https://www.census.gov/data/developers/data-sets/pseo.html |
| SRC05 | UC Berkeley official curriculum | Data Science curriculum | Official university | https://undergraduate.catalog.berkeley.edu/programs/A50AMU |
| SRC06 | CMU official curriculum | AI curriculum | Official university | https://www.cmu.edu/ini/academics/msaie-is/curriculum_ms38.html |
| SRC07 | Penn State official curriculum | Statistics curriculum | Official university | https://bulletins.psu.edu/undergraduate/colleges/eberly-science/statistics-bs/ |
| SRC08 | NextGig Multi-ATS Snapshot | jobs, company, skill, seniority, salary | CC BY 4.0 | https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats |
| SRC09 | O*NET 31.0 | occupational / software skills | CC BY 4.0 | https://www.onetcenter.org/database.html |
| SRC10 | BLS OOH / Employment Projections | employment, openings, wage, education | U.S. official public domain | https://www.bls.gov/ooh/ |
| SRC11 | Aramente EU Tech Jobs | optional live job drill-through | CC BY 4.0 | https://huggingface.co/datasets/Aramente/eu-tech-jobs |

---

# 5. Exact Education Classification

ใช้ CIP 2020 เป็นตัวกำหนด field หลัก

## AI

```text
CIP 11.0102
Artificial Intelligence
```

Official definition:  
https://nces.ed.gov/ipeds/cipcode/cipdetail.aspx?cipid=89569&y=56

## Data Science

```text
CIP 30.7001
Data Science, General
```

Official definition:  
https://nces.ed.gov/ipeds/cipcode/cipdetail.aspx?cipid=92953&y=56

Optional expanded DS group:

```text
30.7099 Data Science, Other
30.7101 Data Analytics, General
30.7102 Business Analytics
30.7103 Data Visualization
30.7199 Data Analytics, Other
```

CIP browser:  
https://nces.ed.gov/ipeds/cipcode/browse.aspx?y=56

## Statistics

Core:

```text
27.0501 Statistics, General
```

Recommended expanded group:

```text
27.0501 Statistics, General
27.0502 Mathematical Statistics and Probability
27.0503 Mathematics and Statistics
27.0599 Statistics, Other
27.0601 Applied Statistics, General
26.1102 Biostatistics
```

Official Statistics definition:  
https://nces.ed.gov/Ipeds/cipcode/cipdetail.aspx?cip=27.0501&y=55

---

# 6. Real Files — IPEDS Graduate Supply

Use annual `CYYYY_A` files.

Latest available in the current design:

```text
C2025_A
Awards/degrees conferred by 6-digit CIP + award level
Reporting period: Jul 1 2024 – Jun 30 2025
```

Data Center:  
https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7

Direct download pattern:

```text
https://nces.ed.gov/ipeds/datacenter/data/C2025_A.zip
https://nces.ed.gov/ipeds/datacenter/data/C2024_A.zip
https://nces.ed.gov/ipeds/datacenter/data/C2023_A.zip
https://nces.ed.gov/ipeds/datacenter/data/C2022_A.zip
https://nces.ed.gov/ipeds/datacenter/data/C2021_A.zip
https://nces.ed.gov/ipeds/datacenter/data/C2020_A.zip
```

Institution directory:

```text
https://nces.ed.gov/ipeds/datacenter/data/HD2025.zip
```

## Fields required

From `CYYYY_A`:

```text
UNITID
CIPCODE
MAJORNUM
AWLEVEL
CTOTALT
```

Use:

```text
MAJORNUM = 1
```

for first major in the main graduate trend, unless the UI explicitly allows first + second major.

Use:

```text
CTOTALT
```

as total awards for the row.

Do not sum roll-up award levels with component award levels.

Primary degree levels:

```text
AWLEVEL 5  = Bachelor's
AWLEVEL 7  = Master's
AWLEVEL 17 = Doctor's – research/scholarship
AWLEVEL 18 = Doctor's – professional practice
AWLEVEL 19 = Doctor's – other
```

---

# 7. What “ชื่อหลักสูตร” Means in the Dashboard

IPEDS publishes:

```text
Institution
+
6-digit CIP program classification
+
Award level
```

IPEDS **does not guarantee the marketing name of the university degree**.

Therefore the main graph must label:

```text
Institution Name
+
CIP Title
+
Degree Level
```

Example display format:

```text
University X
Data Science, General
Bachelor's
```

Field name:

```text
program_display_name
```

generated from:

```text
institution_name + " — " + cip_title + " — " + degree_level
```

Do not pretend that `CIPTITLE` is the exact catalog degree name.

For exact named programs and curricula, use the curated official program registry in Section 9.

---

# 8. Tuition — Use Real Data Only

## National scalable source

Use IPEDS Cost:

```text
COST1_2024
Application fees, tuition and required fees,
food and housing for undergraduate and graduate students
```

IPEDS source page:  
https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7

Direct file:

```text
https://nces.ed.gov/ipeds/datacenter/data/COST1_2024.zip
```

**Important:** IPEDS tuition is primarily institution-level, not necessarily exact program-specific tuition.

Dashboard must display badge:

```text
Institution-level tuition
```

when using IPEDS.

## Official tuition refs for curated programs

UC Berkeley 2026–27 Fee Schedule:  
https://registrar.berkeley.edu/tuition-fees/fee-schedule/

Penn State official tuition:  
https://tuition.psu.edu/

Penn State tuition schedules:  
https://tuition.psu.edu/tuition-schedules

CMU 2026–27 graduate tuition:  
https://www.cmu.edu/sfs/tuition/graduate/

CMU College of Engineering:  
https://www.cmu.edu/sfs/tuition/graduate/cit.html

---

# 9. Real Curriculum Registry

The curriculum section must **not** be created from invented course lists.

Create:

```text
data/manual/program_source_registry.csv
```

Seed with official sources.

## AI — Carnegie Mellon University

Program:

```text
M.S. in Artificial Intelligence Engineering – Information Security
2026–27 curriculum
```

Official curriculum:  
https://www.cmu.edu/ini/academics/msaie-is/curriculum_ms38.html

Examples of real AI core courses visible in the official curriculum:

```text
14-763 Systems and Tool Chains for AI Engineering
18-786 / 24-788 Introduction to Deep Learning
24-784 Trustworthy and Ethical AI Engineering
14-757 / 18-661 / 24-787 Machine Learning options
```

**Ref must be stored on every extracted course row.**

---

## Data Science — UC Berkeley

Program:

```text
Data Science B.A.
```

Official program catalog:  
https://undergraduate.catalog.berkeley.edu/programs/A50AMU

Official major requirements:  
https://cdss.berkeley.edu/dsus/academics/majorrequirements

Examples of real required/foundational courses:

```text
DATA C8 / STAT 20
MATH 51 / calculus equivalent
DATA 89 / MATH 52
MATH 54 / MATH 56 / approved linear algebra alternatives
COMPSCI 61A or DATA C88C
COMPSCI 61B
DATA / COMPSCI / STAT C100
```

Only courses that the official catalog marks as requirements may set:

```text
is_required = true
```

---

## Statistics — Penn State

Program:

```text
Statistics B.S.
```

Official bulletin:  
https://bulletins.psu.edu/undergraduate/colleges/eberly-science/statistics-bs/

Statistics curriculum resource:  
https://science.psu.edu/stat/undergraduate-programs/curriculum

Course descriptions:  
https://bulletins.psu.edu/university-course-descriptions/undergraduate/stat/

Antigravity must extract required courses from the official requirements table and keep the exact reference URL.

---

# 10. Curriculum Data Schema

```text
program_id
institution_name
official_program_name
domain
degree_level
course_code
course_name
credits
requirement_group
is_required
catalog_year
source_url
retrieved_at
```

Every curriculum record must have a non-null:

```text
source_url
```

---

# 11. Mapping Course → Skill

Create a canonical skills dictionary.

Example categories:

```text
Programming
Statistics & Mathematics
Machine Learning
Deep Learning
Data Engineering
Database
Cloud
Data Visualization
Experimentation
MLOps
NLP
Computer Vision
Generative AI / LLM
Research
Communication
Ethics
Business / Domain
Leadership
```

Mapping table:

```text
course_skill_map
----------------
program_id
course_code
skill_id
skill_name
skill_category
mapping_method
mapping_evidence
mapping_score
source_url
```

## Phase 1 rule

Use:

```text
manual + deterministic keyword dictionary
```

Not generative inference alone.

If AI/NLP is used to propose a mapping:

```text
mapping_method = "llm_proposed"
```

and it cannot become production-visible until:

```text
is_reviewed = true
```

---

# 12. Real Graduate Employment Outcomes

Use U.S. Census:

> **Post-Secondary Employment Outcomes (PSEO)**

Official documentation:  
https://www.census.gov/data/developers/data-sets/pseo.html

Earnings endpoint:  
https://api.census.gov/data/timeseries/pseo/earnings.html

Variables:  
https://api.census.gov/data/timeseries/pseo/earnings/variables.html

PSEO contains:

```text
Y1_GRADS_EARN
Y5_GRADS_EARN
Y10_GRADS_EARN
```

and earnings percentiles such as:

```text
Y1_P25_EARNINGS
Y1_P50_EARNINGS
Y1_P75_EARNINGS
```

## Example API query template

```text
https://api.census.gov/data/timeseries/pseo/earnings
?get=LABEL_INSTITUTION,LABEL_DEGREE_LEVEL,LABEL_CIPCODE,
Y1_GRADS_EARN,Y5_GRADS_EARN,Y10_GRADS_EARN,
Y1_P25_EARNINGS,Y1_P50_EARNINGS,Y1_P75_EARNINGS,
INSTITUTION,CIPCODE
&for=us:1
&key=YOUR_CENSUS_API_KEY
```

CSV output can be requested with:

```text
&outputFormat=csv
```

Census API key is free; Antigravity should read it from:

```text
.env
CENSUS_API_KEY=
```

Never commit the key.

---

# 13. PSEO Limitation

PSEO is not available for every U.S. institution/program.

Therefore:

```text
if no PSEO row:
    employment_outcome_status = "Not available in PSEO"
```

Do not replace missing PSEO outcomes with College Scorecard or estimated values unless a separate verified source is explicitly configured.

---

# 14. TAB 1 — Graduate Supply & Learned Skills

## Tab title

```text
ปริมาณคนที่จบและ Skills ที่เรียนมา
```

---

# 15. Tab 1 Filters

```text
Year
Domain
Institution
CIP Program
Degree Level
Program Registry
Skill
Tuition Residency Type
```

All charts in Tab 1 must update together.

---

# 16. Tab 1 KPI Cards

Real-data KPIs:

```text
Total Awards Reported
Institutions Producing Graduates
Programs/CIP Records
Required Courses
Skills Covered
Tuition / Fee
Employed Graduates — Year 1
Employed Graduates — Year 5
Employed Graduates — Year 10
```

Each card must contain:

```text
[Open source]
```

---

# 17. Tab 1 Graph A — Graduate Production by Program and Year

## Data

`IPEDS CYYYY_A + HDYYYY`

## Plotly

```text
Line / stacked bar toggle

x     = year
y     = CTOTALT
color = program_display_name
```

## User interaction

Click program:

```text
→ curriculum
→ skills taught
→ tuition
→ PSEO outcome
→ all KPI
```

## Required tooltip

```text
Institution
CIP title
CIP code
Degree level
Year
Awards
Source
```

Add link below chart:

```text
Open IPEDS source
```

---

# 18. Tab 1 Graph B — Required Courses and Learned Skills

## Data

Official program curricula only.

## Visualization

Primary:

```text
Course × Skill Heatmap
```

Rows:

```text
required courses
```

Columns:

```text
canonical skills
```

Cell:

```text
mapping_score
```

Alternative tab:

```text
Course table
```

with:

```text
Course Code
Course Name
Required?
Skills
Open Official Curriculum
```

---

# 19. Tab 1 Graph C — Graduate Employment Outcomes

## Data

U.S. Census PSEO.

## Production graph

```text
Grouped Bar
x = Year after graduation
    Year 1
    Year 5
    Year 10

y = employed graduate count
```

Toggle:

```text
Employment Count
Employment Coverage Rate
Median Earnings
```

Employment coverage if denominator exists:

```text
employment_coverage =
Y1_GRADS_EARN / Y1_IPEDS_COUNT
```

Label this carefully:

```text
Share of PSEO-covered graduates with earnings record
```

Do not automatically label it “employment rate” unless definition is confirmed for the selected PSEO measure.

---

# 20. Tab 1 Graph D — Tuition

Primary scalable data:

```text
IPEDS COST1_2024
```

For curated programs with official fee pages:

```text
official value overrides institution estimate
```

But both values must remain available:

```text
tuition_value
tuition_scope = institution | program
source_url
```

Recommended chart:

```text
Horizontal Bar
y = institution / program
x = tuition
```

Color / icon must identify:

```text
Program-specific
Institution-level
```

---

# 21. Real Labor-Market Job Dataset

Primary structured job posting dataset:

> **NextGig — Multi-ATS Job Postings Snapshot (June 2026)**

Dataset card:  
https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats

File page:  
https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats/blob/main/nextgig_jobs_2026-06.parquet

Direct Parquet:

```text
https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats/resolve/main/nextgig_jobs_2026-06.parquet
```

License:

```text
CC BY 4.0
```

Snapshot characteristics published by source:

```text
112,816 postings
13,412 companies
23 ATS platforms
~46% have structured salary
~71% have extracted skills
```

Relevant fields:

```text
title
normalized_title
company_name
industry
occupational_category
experience_level
job_level_normalized
years_experience_numeric
education_level
skills_required
minimum_qualifications
preferred_qualifications
responsibilities
salary_min
salary_max
salary_currency
salary_rate_unit
city
country
location_resolved
date_posted
closing_date
job_description
```

---

# 22. Real Job Dataset Caveat

NextGig is a **June 2026 snapshot**, not a live feed.

Therefore chart label must be:

```text
Open / collected job postings in June 2026 snapshot
```

not:

```text
Current jobs right now
```

The source notes that:
- date_posted is sparse
- country/city are derived
- skills and structured fields include automated extraction
- original apply URLs are not distributed in this snapshot

Show this limitation in `About data`.

---

# 23. Optional Traceable Live Job Feed

If Antigravity implements direct links to original vacancies, add:

> **Aramente — EU Tech Jobs**

Dataset:  
https://huggingface.co/datasets/Aramente/eu-tech-jobs

Direct latest jobs:

```text
https://huggingface.co/datasets/Aramente/eu-tech-jobs/resolve/main/latest/jobs.parquet
```

License:

```text
CC BY 4.0
```

Useful fields:

```text
company_slug
title
url
countries
seniority
role_family
salary_min
salary_max
salary_currency
salary_period
stack
posted_at
description_md
```

Important:

```text
This source is EU / remote-EU focused.
```

Do not silently mix it with U.S. metrics.

If used, add dataset selector:

```text
Market Dataset:
- US / Global June 2026 Snapshot — NextGig
- EU Live Feed — Aramente
```

---

# 24. Official Labor Baseline

Use BLS to provide official U.S. occupation-level baseline.

## Data Scientist

BLS OOH:  
https://www.bls.gov/ooh/math/data-scientists.htm

Current 2025 reference values for QA:

```text
Employment 2025 = 275,600
Annual openings 2025–35 = 24,800
Median annual wage 2025 = $120,230
Typical entry education = Bachelor's degree
```

---

## AI-related proxy

Occupation:

```text
15-1221
Computer and Information Research Scientists
```

BLS:  
https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm

Reference:

```text
Employment 2025 = 38,600
Annual openings = 2,900
Median annual wage = $140,300
Typical entry education = Master's degree
```

UI label:

```text
AI-related research occupation proxy
```

---

## Statistics

BLS:

https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm

Reference:

```text
Statistician median annual wage 2025 = $105,650
Mathematicians & Statisticians annual openings = ~2,000
Typical entry education = Master's degree
```

If exact occupation-level employment is required, use BLS OEWS tables rather than deriving it.

---

# 25. O*NET Skill Benchmark

Use O*NET 31.0 Database.

Download/database page:  
https://www.onetcenter.org/database.html

License:  
https://www.onetcenter.org/license_db.html

Software Skills CSV documentation:  
https://www.onetcenter.org/dictionary/31.0/csv/software_skills.html

---

# 26. O*NET Real Skill References — QA Checks

These values may be used as **validation benchmarks**, not as manually hard-coded final data.

## Data Scientists — 15-2051.00

O*NET Employer-Based In Demand Skills:  
https://www.onetonline.org/link/demand/15-2051.00

Published examples:

```text
Python 66%
SQL 51%
R 34%
Tableau 22%
Power BI 19%
AWS 17%
Azure 13%
TensorFlow 11%
PyTorch 10%
```

---

## Statisticians — 15-2041.00

https://www.onetonline.org/link/demand/15-2041.00

Examples:

```text
R 43%
SAS 40%
Python 28%
SQL 18%
Statistical software 18%
Excel 11%
Stata 8%
Tableau 8%
SPSS 7%
```

---

## AI-related research proxy — 15-1221.00

https://www.onetonline.org/link/demand/15-1221.00

Examples:

```text
Python 66%
AWS 35%
PyTorch 29%
Azure 25%
TensorFlow 25%
SQL 20%
Kubernetes 20%
Java 15%
Docker 15%
C++ 14%
```

These are excellent QA checks for the job-skills aggregation.

---

# 27. TAB 2 — Job Demand & Required Skills

## Tab title

```text
ปริมาณงานที่จ้างและ Skills ที่ต้องการ
```

---

# 28. Tab 2 Filters

```text
Market Dataset
Country
City
Domain
Job Title
Company
Industry
Career Level
Education Required
Skill
Salary Currency
```

All graphs in Tab 2 must react to all filters.

---

# 29. Job Domain Classification

Create deterministic keyword classification.

## AI

Title / category signals:

```text
artificial intelligence
AI engineer
machine learning
ML engineer
deep learning
NLP
computer vision
generative AI
LLM
research scientist
```

## Data Science

```text
data scientist
data science
analytics scientist
decision scientist
data analyst
data engineer
```

`Data Analyst` and `Data Engineer` should be optional toggles because they broaden the field.

## Statistics

```text
statistician
biostatistician
statistical programmer
statistical analyst
quantitative statistic*
```

Store:

```text
domain_rule_version
```

---

# 30. Tab 2 KPI Cards

```text
Job Posting Count
Unique Companies
Unique Job Titles
Median Salary
Salary Coverage %
Skills Coverage %
Entry Jobs
Intermediate Jobs
Expert Jobs
```

Add separate official baseline cards:

```text
BLS Employment
BLS Annual Openings
BLS Median Wage
```

Do not merge BLS values with posting count.

---

# 31. Tab 2 Graph A — Number of Vacancies / Postings

Primary data:

```text
NextGig snapshot
```

Plot:

```text
Bar:
x = domain
y = count(job rows)
color = career_level
```

Optional:

```text
Company / location drilldown
```

For BLS baseline show separate trace or reference card:

```text
Annual Openings
```

Never label snapshot job rows as annual openings.

---

# 32. Tab 2 Graph B — Skills Required

Primary:

```text
NextGig.skills_required
```

Parse JSON arrays.

Metric:

```text
skill_posting_count =
count distinct postings containing skill

skill_demand_pct =
skill_posting_count /
postings with non-null skills_required
```

Plot:

```text
Horizontal Bar
y = canonical_skill
x = skill_demand_pct
```

Toggle:

```text
Demand %
Posting Count
```

O*NET can be shown as benchmark/reference.

---

# 33. Tab 2 Graph C — Companies Hiring

Data:

```text
NextGig.company_name
```

Plot:

```text
Treemap or ranked bar
```

Metric:

```text
count(job rows)
```

Tooltip:

```text
Company
Job Count
Top Titles
Top Skills
Career Level Mix
Median Salary where available
Dataset Snapshot
```

Click company:

```text
→ vacancy chart updates
→ skill chart updates
→ salary chart updates
```

---

# 34. Tab 2 Graph D — Salary by Career Level

Primary:

```text
NextGig:
salary_min
salary_max
salary_currency
salary_rate_unit
job_level_normalized
```

Only use records with valid salary.

Normalize:

```text
salary_mid = (salary_min + salary_max) / 2
```

Store:

```text
salary_mid
salary_is_derived = true
```

Do not hide missing salary rows.

Show KPI:

```text
Salary Coverage %
```

---

# 35. Career Level Mapping

First inspect real values:

```sql
SELECT DISTINCT job_level_normalized
FROM jobs_raw
ORDER BY 1;
```

Then configure mapping.

Target dashboard levels:

```text
Entry
Intermediate
Expert
```

Suggested mapping after checking observed values:

```text
Entry:
Intern
Entry
Junior
Associate

Intermediate:
Mid
Senior

Expert:
Staff
Lead
Principal
Manager
Director
VP
Executive
Head
```

Preserve original field:

```text
career_level_raw
```

and add:

```text
career_level_3
```

---

# 36. Tab 2 Salary Graph

Use Plotly:

```text
Box Plot

x = career_level_3
y = annual_salary_normalized
color = domain
```

Show:

```text
n salary records
median
P25
P75
```

Add BLS median as dashed reference line for compatible occupation.

---

# 37. Salary Normalization

Keep original values:

```text
salary_min_original
salary_max_original
currency_original
period_original
```

Derived:

```text
annual_salary_min
annual_salary_max
annual_salary_mid
```

Annualization:

```text
hour  * 40 * 52
week  * 52
month * 12
year  * 1
```

Each derived record:

```text
annualization_method
```

For multi-currency comparisons, either:

1. keep one currency filter at a time, or
2. implement dated FX source

Do not convert currency without storing:

```text
fx_rate
fx_date
fx_source_url
```

---

# 38. TAB 3 — Skills Mismatch

## Question

> Skills ที่หลักสูตรสอนจริง สอดคล้องกับ skills ที่ job postings ต้องการจริงมากแค่ไหน?

---

# 39. Valid Scope for Mismatch

Mismatch may only be computed when:

```text
course curriculum is sourced
AND
job skill data is sourced
```

Example valid comparison:

```text
UC Berkeley Data Science BA required curriculum
vs
United States Data Science job postings
```

If comparing U.S. curriculum to EU jobs:

```text
display a visible geography warning
```

---

# 40. Canonical Skill Dictionary

Create:

```text
dim_skill
```

Fields:

```text
skill_id
canonical_name
category
aliases
onet_technology_name
```

Example aliases:

```yaml
python:
  - python
  - python3

sql:
  - sql
  - structured query language

machine_learning:
  - machine learning
  - ml
  - predictive modeling

pytorch:
  - pytorch
  - torch

power_bi:
  - power bi
  - microsoft power bi
```

---

# 41. Supply Skill Score

Based only on required courses.

For selected program:

```text
RequiredCourseCoverage(skill)
=
required courses mapped to skill
/
total required courses
```

Program-level:

```text
SupplySkillScore =
100 * normalized required-course coverage
```

Optional weighted form:

```text
credit-weighted supply score
```

Only if credits are available from official curriculum.

---

# 42. Demand Skill Score

From job postings:

```text
DemandSkillScore(skill)
=
100 *
number of filtered postings requiring skill
/
number of filtered postings with usable skill data
```

This must be computed from real posting records.

---

# 43. Mismatch Score

```text
MismatchScore =
DemandSkillScore - SupplySkillScore
```

Interpretation:

```text
> 0  market demand exceeds curriculum coverage
≈ 0  aligned
< 0  curriculum coverage exceeds measured market demand
```

Do not call negative scores “unnecessary skills.”

Use:

```text
Lower observed market demand
```

because the job dataset has coverage limits.

---

# 44. Tab 3 Graph A — Skill Gap Quadrant

```text
Scatter

x = SupplySkillScore
y = DemandSkillScore
size = skill_posting_count
color = skill_category
text = canonical_skill
```

Quadrants:

```text
High Demand / Low Supply → Priority Gap
High Demand / High Supply → Strong Alignment
Low Demand / High Supply → Education-Heavy
Low Demand / Low Supply → Low Observed Priority
```

---

# 45. Tab 3 Graph B — Top Mismatch Skills

```text
Diverging horizontal bar

x = MismatchScore
y = skill
```

Positive:

```text
Demand > Supply
```

Negative:

```text
Supply > Observed Demand
```

---

# 46. Tab 3 Graph C — Program × Market Skill Matrix

```text
rows = official programs
columns = canonical skills
value = curriculum coverage
```

Overlay / toggle:

```text
Demand %
Mismatch
```

---

# 47. Tab 3 Graph D — Career-Level Skill Gap

Use actual job level.

```text
rows = skill
columns =
Entry
Intermediate
Expert

value =
DemandSkillScore(level) - SupplySkillScore(program)
```

---

# 48. Cross-Filtering Requirements

Every Plotly chart inside each tab must be linked.

Architecture:

```text
Global Filter Store
        ↓
Current Tab Store
        ↓
Selected Program / Skill / Company
        ↓
Filtered DuckDB query
        ↓
All charts + KPI cards update
```

Dash stores:

```python
dcc.Store(id="global-filter-store")
dcc.Store(id="tab1-selection-store")
dcc.Store(id="tab2-selection-store")
dcc.Store(id="mismatch-context-store")
```

---

# 49. Required Interaction Example — Tab 1

User:

```text
Domain = Data Science
Year = 2025
```

then clicks:

```text
University / CIP program
```

System must update:

```text
Graduate Count
Required Courses
Skills Learned
Tuition
PSEO Outcomes
KPI cards
```

No page reload.

---

# 50. Required Interaction Example — Tab 2

User clicks:

```text
Python
```

System must update:

```text
Job Count
Companies Hiring
Salary Distribution
Career Level Mix
Education Requirement
```

---

# 51. Required Interaction — Tab 3

User comes from:

```text
Tab 1:
Program = Data Science B.A.

Tab 2:
Career Level = Entry
Country = United States
```

Tab 3 must compare:

```text
skills taught in selected official curriculum

VS

skills required in filtered Entry-level U.S. job postings
```

---

# 52. Mandatory “Open Ref” Feature

Every chart must have a visible:

```text
Open source
```

or:

```text
View data reference
```

button.

Required metadata object:

```json
{
  "source_id": "SRC08",
  "source_name": "NextGig Multi-ATS Job Postings Snapshot",
  "source_url": "https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats",
  "source_date": "2026-06",
  "license": "CC BY 4.0"
}
```

For curriculum table, every row should have:

```text
Open official curriculum
```

For optional Aramente jobs, each job row can expose its original:

```text
url
```

---

# 53. Source Drawer

Add right-side drawer:

```text
About this chart
```

Contents:

```text
Metric definition
Filters applied
Source
Data year / snapshot
License
Rows used
Rows excluded
Missing-value rate
Transformation
Open source
```

---

# 54. Data Lineage

Every analytics table must include:

```text
source_id
source_record_key
source_url
source_snapshot
retrieved_at
transform_version
```

No source metadata = record must not enter production fact tables.

---

# 55. Real Data Model

## `fact_graduates`

```text
unitid
institution_name
cipcode
cip_title
award_level
year
major_num
graduate_awards
source_id
source_url
```

## `dim_official_program`

```text
program_id
unitid
institution_name
official_program_name
domain
degree_level
cipcode_if_verified
curriculum_url
tuition_url
mapping_status
```

`mapping_status`:

```text
verified
unverified
aggregate-only
```

## `fact_course`

```text
program_id
course_code
course_name
credits
is_required
requirement_group
catalog_year
source_url
```

## `bridge_course_skill`

```text
program_id
course_code
skill_id
mapping_method
mapping_score
is_reviewed
source_url
```

## `fact_graduate_outcome`

```text
institution
degree_level
cipcode
graduation_cohort
year_after_graduation
employed_graduates
covered_graduates
p25_earnings
median_earnings
p75_earnings
source_url
```

## `fact_jobs`

```text
job_key
snapshot
title
normalized_title
company_name
domain
industry
career_level_raw
career_level_3
education_level
country
city
salary_min
salary_max
salary_currency
salary_rate_unit
annual_salary_mid
source_id
source_url
```

## `bridge_job_skill`

```text
job_key
skill_id
skill_raw
source_id
source_url
```

---

# 56. Important Join Rule

Do **not** automatically assume:

```text
official degree title
=
IPEDS CIP row
```

A university may have multiple actual programs under one CIP.

Only connect exact curriculum to IPEDS graduate count when:

```text
unitid verified
AND
cipcode verified
AND
award_level verified
AND
the interpretation is documented
```

Otherwise display:

```text
IPEDS program-classification aggregate
```

---

# 57. ETL — IPEDS

Expected module:

```text
etl/ipeds.py
```

Pseudo-code:

```python
for year in range(2020, 2026):
    download(f"C{year}_A.zip")
    read_csv()
    filter MAJORNUM == 1
    filter CIPCODE in configured CIP list
    keep safe award levels
    join HD{year} on UNITID
    write parquet
```

Required QA:

```text
no duplicate UNITID+CIPCODE+MAJORNUM+AWLEVEL+YEAR
CTOTALT >= 0
CIP code in configured taxonomy
```

---

# 58. ETL — Curriculum

Expected module:

```text
etl/curriculum.py
```

Production strategy:

```text
official registry
→ fetch official HTML
→ extract course table
→ manual review
→ curated CSV/Parquet
```

Do not crawl the entire web.

Only ingest domains listed in:

```text
program_source_registry.csv
```

---

# 59. ETL — PSEO

Expected:

```text
etl/pseo.py
```

Use Census API.

Environment:

```text
CENSUS_API_KEY
```

Cache raw responses:

```text
data/raw/pseo/
```

Never issue API calls from every chart callback.

ETL:

```text
Census API
→ raw JSON/CSV
→ validate status flags
→ normalized Parquet
→ DuckDB
```

---

# 60. ETL — Jobs

Primary:

```python
import pandas as pd

url = (
    "https://huggingface.co/datasets/"
    "NextGig-Rocks/global-job-postings-multi-ats/"
    "resolve/main/nextgig_jobs_2026-06.parquet"
)

jobs = pd.read_parquet(url)
```

Store the original Parquet in:

```text
data/raw/jobs/
```

and keep SHA / retrieval timestamp if possible.

---

# 61. Parsing `skills_required`

NextGig stores list-type columns as JSON strings.

Example:

```python
import json

def parse_json_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else []
    except Exception:
        return []
```

Do not treat failed parsing as an empty confirmed skill list.

Store:

```text
skill_parse_status
```

---

# 62. ETL — O*NET

Expected:

```text
etl/onet.py
```

Use O*NET 31.0 downloads.

Source:  
https://www.onetcenter.org/database.html

Filter:

```text
15-2051.00 Data Scientists
15-2041.00 Statisticians
15-1221.00 Computer and Information Research Scientists
```

Use as:
- canonical skill taxonomy aid
- occupational skill benchmark
- QA comparison

---

# 63. ETL — BLS

Expected:

```text
etl/bls.py
```

Use official BLS pages / downloadable tables for:

```text
Employment
Projected Employment
Annual Openings
Median Wage
Typical Entry Education
```

Do not scrape chart pixels.

Prefer downloadable BLS tables when available.

---

# 64. No Mock Data Setting

Config:

```yaml
environment: production
allow_mock_data: false
```

Code rule:

```python
if settings.environment == "production" and source_type == "mock":
    raise RuntimeError("Mock data prohibited in production")
```

Tests may use fixtures only under:

```text
tests/fixtures/
```

---

# 65. Data Availability UI

Each visual must support:

```text
Available
Partial
Unavailable
```

Example:

```text
Graduate count: Available
Curriculum: Available for curated programs
Year 5 employment: Partial — PSEO participating institutions only
Program-specific tuition: Partial
Salary: Partial — employer disclosure only
```

---

# 66. Tab 1 Scope Badge

Always show:

```text
Graduate counts:
U.S. IPEDS

Employment outcomes:
U.S. Census PSEO

Curriculum:
Official program catalogs

Tuition:
IPEDS + official program pages
```

---

# 67. Tab 2 Scope Badge

Show:

```text
Job postings:
NextGig June 2026 Multi-ATS snapshot

Official labor baseline:
BLS 2025 / 2025–35 projections

Skill benchmark:
O*NET 31.0
```

---

# 68. Tab 3 Scope Badge

Example:

```text
Education:
Selected U.S. official curriculum

Labor demand:
Filtered U.S. records from June 2026 job snapshot

Skill benchmark:
O*NET
```

If geography differs, show warning.

---

# 69. Plotly Requirements

Use Plotly as primary visual layer.

Every graph:

```text
hover
click selection
box/lasso where useful
responsive
download image
filter-aware title
source footer
no-data state
```

Do not hard-code displayed values into figure functions.

Every number must come from:

```text
filtered dataframe / DuckDB query
```

---

# 70. Recommended App Architecture

```text
project/
├── app/
│   ├── main.py
│   ├── layout.py
│   ├── callbacks/
│   │   ├── global_filters.py
│   │   ├── tab1.py
│   │   ├── tab2.py
│   │   └── tab3.py
│   ├── charts/
│   │   ├── graduates.py
│   │   ├── curriculum.py
│   │   ├── jobs.py
│   │   ├── salaries.py
│   │   └── mismatch.py
│   ├── services/
│   └── data/
├── etl/
│   ├── ipeds.py
│   ├── curriculum.py
│   ├── pseo.py
│   ├── nextgig.py
│   ├── onet.py
│   └── bls.py
├── config/
│   ├── sources.yaml
│   ├── cip_mapping.yaml
│   ├── career_levels.yaml
│   ├── skill_taxonomy.yaml
│   └── program_source_registry.csv
├── data/
│   ├── raw/
│   ├── processed/
│   └── analytics.duckdb
├── tests/
├── requirements.txt
└── README.md
```

---

# 71. `sources.yaml`

Seed exactly with real refs:

```yaml
sources:

  ipeds_completions:
    source_id: SRC01
    name: NCES IPEDS Completions
    url: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7
    geography: US
    source_type: official

  pseo:
    source_id: SRC04
    name: US Census Post-Secondary Employment Outcomes
    url: https://www.census.gov/data/developers/data-sets/pseo.html
    geography: US
    source_type: official

  nextgig_2026_06:
    source_id: SRC08
    name: NextGig Multi-ATS Job Postings Snapshot
    url: https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats
    direct_file: https://huggingface.co/datasets/NextGig-Rocks/global-job-postings-multi-ats/resolve/main/nextgig_jobs_2026-06.parquet
    snapshot: 2026-06
    license: CC-BY-4.0

  onet_31:
    source_id: SRC09
    name: O*NET 31.0 Database
    url: https://www.onetcenter.org/database.html
    license: CC-BY-4.0

  bls:
    source_id: SRC10
    name: U.S. Bureau of Labor Statistics
    url: https://www.bls.gov/ooh/
    geography: US
```

---

# 72. Data Refresh Strategy

## IPEDS

```text
Annual
```

## PSEO

```text
Refresh when Census release changes
```

## NextGig

```text
Fixed June 2026 research snapshot
```

Do not pretend it refreshes.

## O*NET

```text
Track release version
Current BRD reference: O*NET 31.0
```

## BLS

```text
Annual OEWS / annual employment projections cycle
```

---

# 73. Acceptance Criteria — Real Data

Dashboard is accepted only if:

```text
[ ] no production chart loads mock data
[ ] every chart has a source URL
[ ] every curriculum row has official URL
[ ] graduate values come from IPEDS
[ ] PSEO values come from Census API
[ ] jobs come from configured open job dataset
[ ] salary coverage is disclosed
[ ] skill coverage is disclosed
[ ] BLS values are separated from posting counts
[ ] missing data are N/A
[ ] Year 2/3 graduate employment is not fabricated
```

---

# 74. Acceptance Test — Tab 1

Scenario:

```text
Select:
Domain = Data Science
Degree = Bachelor's
Year = 2025
```

Expected:

1. Graduate graph queries actual IPEDS rows.
2. Clicking an institution/CIP record updates all Tab 1 views.
3. Curriculum appears only if an official program ref exists.
4. Tuition shows institution/program scope.
5. PSEO shows only available official outcomes.
6. User can click the source link.

---

# 75. Acceptance Test — Tab 2

Scenario:

```text
Country = United States
Domain = Data Science
Career Level = Entry
Skill = Python
```

Expected:

```text
Job count = filtered real rows
Companies = filtered real rows
Salary = only salary-disclosing filtered rows
Salary coverage = visible
Skill demand = real skills_required records
BLS annual openings = separate reference metric
```

---

# 76. Acceptance Test — Tab 3

Scenario:

```text
Official Curriculum = UC Berkeley Data Science B.A.
Market = United States
Career Level = Entry
```

Expected:

```text
Supply skills =
official required curriculum mappings

Demand skills =
real filtered job posting skill records

Mismatch =
Demand - Supply
```

Clicking a skill must show:

```text
Courses teaching it
+
job count requiring it
+
companies requiring it
+
salary where available
+
source refs
```

---

# 77. Quality Warnings to Show in Dashboard

Use short visible notices.

### IPEDS

```text
Counts are awards/degrees conferred.
They are not guaranteed to equal unique persons.
```

### Curriculum

```text
Curriculum coverage is available only for programs
with verified official catalog sources.
```

### PSEO

```text
PSEO covers participating institutions/programs
and reports outcomes at Years 1, 5 and 10.
```

### NextGig

```text
Job data are a June 2026 research snapshot.
Salary and skills are not present for every posting.
```

### BLS AI

```text
15-1221 is used only as an AI-related occupation proxy.
```

---

# 78. Recommended First Production Release

To avoid pretending there is complete curriculum coverage for every U.S. program:

## Graduate count view

Use all IPEDS records matching configured CIP codes.

## Curriculum/skill view

Start with the verified official program registry:

```text
AI:
CMU M.S. Artificial Intelligence Engineering – Information Security

Data Science:
UC Berkeley Data Science B.A.

Statistics:
Penn State Statistics B.S.
```

Then expand registry one program at a time.

Each added program requires:

```text
official curriculum URL
official program name
degree level
verified CIP mapping or aggregate-only flag
reviewed course list
```

---

# 79. Development Order for Antigravity

```text
1. Create repo/project
2. Implement source registry
3. Implement DuckDB schema
4. Build IPEDS ETL with real C2020_A–C2025_A data
5. Build official curriculum registry
6. Build PSEO ETL
7. Load NextGig real Parquet
8. Load O*NET
9. Load BLS baseline
10. Build Tab 1
11. Build Tab 2
12. Implement shared skill taxonomy
13. Build Tab 3 mismatch
14. Add source drawer and Open Ref buttons
15. Add QA + tests
```

Do not build final visuals on mock data first and forget to switch them.

---

# 80. Antigravity Handoff Prompt

Copy this prompt together with this BRD:

```text
Build the dashboard specified in this BRD using REAL DATA ONLY.

Core stack:
- Python
- Dash
- Plotly
- DuckDB
- Pandas/Polars
- Parquet

Do not use mock, synthetic, random, or placeholder production data.

Use the exact sources and source URLs defined in the BRD:
- NCES IPEDS for graduate counts and institution-level tuition
- official university catalog pages for required curricula
- U.S. Census PSEO for graduate employment/earnings outcomes
- NextGig June 2026 CC BY 4.0 job-posting snapshot for jobs, companies,
  seniority, required skills, education requirements and salary
- O*NET 31.0 for occupational skill benchmarks
- BLS for official employment/openings/wage baselines

Critical corrections:
- PSEO provides Year 1 / Year 5 / Year 10 outcomes, not Year 1 / 2 / 3.
  Never fabricate Year 2 or Year 3.
- IPEDS CIP title is a program classification, not necessarily the exact
  university marketing degree name.
- Do not automatically map official curriculum to an IPEDS program unless
  UNITID + CIP + degree level mapping is verified.
- Do not mix job posting counts with BLS annual openings.
- SOC 15-1221 must be labeled AI-related proxy.

Every Plotly graph must:
1. participate in cross-filtering,
2. update based on user selection,
3. show data year/snapshot,
4. have an Open Source / View Reference action,
5. expose missing-data coverage,
6. be generated from queried real records.

All source metadata must be stored in the data model.
If source data are unavailable, display N/A rather than generating values.
```

---

# 81. Definition of Done

Production dashboard is done when a user can perform this flow:

```text
Open Tab 1
→ choose Data Science
→ see real IPEDS graduate counts by year
→ choose an institution/program record
→ see verified official required courses if available
→ see learned skills
→ see sourced tuition
→ see available PSEO Year 1 / 5 / 10 outcomes
→ open every source ref

Open Tab 2
→ choose U.S. Data Science jobs
→ see real June 2026 posting count
→ click Python
→ see real companies and salary-bearing postings
→ compare Entry / Intermediate / Expert
→ open dataset ref

Open Tab 3
→ choose a verified curriculum
→ compare its real taught skills against real job-demand skills
→ inspect mismatch
→ click a skill
→ trace both education-side and labor-side references
```

No production value may exist without a traceable source.
