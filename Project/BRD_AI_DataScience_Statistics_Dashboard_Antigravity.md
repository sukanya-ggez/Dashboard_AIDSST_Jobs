# Business Requirements Document (BRD)
## Dashboard: AI / Data Science / Statistics — Graduate Supply, Job Demand & Skills Mismatch

**Document purpose:** ส่งต่อให้ Antigravity ใช้เป็นข้อกำหนดสำหรับพัฒนา Dashboard  
**Backend:** Python  
**Primary visualization:** Plotly  
**Recommended framework:** Dash + Plotly หรือ FastAPI + Plotly/Dash frontend  
**Document version:** 1.0  
**Language:** Thai UI เป็นหลัก และคงชื่อ field / skill / occupation ภาษาอังกฤษตามแหล่งข้อมูล

---

# 1. Executive Summary

Dashboard นี้มีเป้าหมายเพื่อตอบคำถามหลัก 2 ข้อ และมีอีก 1 tab สำหรับวิเคราะห์เชื่อมโยงผลลัพธ์

1. **ปริมาณคนที่จบและ Skills ที่เรียนมา**
2. **ปริมาณงานที่จ้างและ Skills ที่ต้องการ**
3. **วิเคราะห์ Skills Mismatch** ระหว่างสิ่งที่มหาวิทยาลัยผลิตกับสิ่งที่ตลาดแรงงานต้องการ

Dashboard ต้องทำให้ผู้ใช้สามารถเลือกตัวกรอง เช่น ปี ประเทศ/พื้นที่ สาขา หลักสูตร ระดับงาน บริษัท และ skill แล้ว **ทุกกราฟภายใน tab เดียวกันต้องอัปเดตตาม selection เดียวกัน** รวมถึงสามารถส่ง filter state ไปยัง Tab 3 เพื่อวิเคราะห์ mismatch ได้

> หมายเหตุ: Tabs 1–2 ตอบ 2 คำถามหลักโดยตรง ส่วน Tab 3 เป็น analytical synthesis จากข้อมูลทั้งสองฝั่ง

---

# 2. Business Objectives

## 2.1 เป้าหมายทางธุรกิจ

Dashboard ต้องช่วยให้ผู้ใช้:

- เห็น “Supply” ของบัณฑิตด้าน **AI, Data Science และ Statistics**
- เห็น “Demand” ของตลาดแรงงานด้านเดียวกัน
- เข้าใจว่าหลักสูตรใดผลิตบัณฑิตจำนวนเท่าไรในแต่ละปี
- เห็นรายวิชาบังคับและ skill ที่หลักสูตรสอน
- เห็นจำนวนบัณฑิตที่ได้งานหลังจบในปีที่ 1, 2 และ 3
- เปรียบเทียบค่าเทอม/ต้นทุนการศึกษา
- เห็นจำนวนตำแหน่งงานว่างในตลาด
- เห็น skill ที่ถูกระบุในประกาศงาน
- เห็นบริษัทที่รับคนในสาย AI / Data Science / Statistics
- เห็นเงินเดือนในแต่ละระดับงาน
- วิเคราะห์ skill ที่ “เรียนมาแต่ตลาดไม่ค่อยต้องการ”, “ตลาดต้องการแต่หลักสูตรสอนไม่เพียงพอ” และ “ตรงกันดี”
- ใช้เป็น evidence สำหรับการนำเสนอด้าน Science Communication และการวิเคราะห์ workforce / curriculum planning

---

# 3. Target Users

## Primary users

- นักศึกษา
- อาจารย์
- นักวิจัย
- ผู้พัฒนาหลักสูตร
- Career advisor
- ผู้บริหารมหาวิทยาลัย
- ผู้สนใจตลาดแรงงานด้าน AI / Data Science / Statistics

## User questions

### Question A — Graduate Supply
> “แต่ละปีมีคนเรียนจบสาย AI / Data Science / Statistics เท่าไร เรียน skill อะไรมาบ้าง และหลังเรียนจบได้งานเร็วแค่ไหน?”

### Question B — Job Demand
> “ตลาดต้องการคนสาย AI / Data Science / Statistics เท่าไร บริษัทไหนรับ ต้องการ skill อะไร และให้เงินเดือนเท่าไร?”

### Question C — Skills Mismatch
> “สิ่งที่หลักสูตรกำลังสอน สอดคล้องกับสิ่งที่ตลาดต้องการมากแค่ไหน?”

---

# 4. Scope

## 4.1 In Scope

- Dashboard 3 tabs
- Python backend
- Plotly เป็น visualization library หลัก
- Connected/cross-filtering charts ภายในแต่ละ tab
- Shared global filters
- Data preprocessing pipeline
- Skill normalization
- Course-to-skill mapping
- Job-to-skill mapping
- Skills mismatch score
- Export filtered data เป็น CSV
- Export chart เป็น PNG/SVG ผ่าน Plotly
- Tooltip แสดง source/year/methodology
- Data freshness indicator
- Open Data / public-use sources เป็นหลัก
- รองรับการเพิ่มประเทศ/มหาวิทยาลัย/แหล่งข้อมูลในอนาคต

## 4.2 Out of Scope — Phase 1

- Machine learning เพื่อทำนายเงินเดือนรายบุคคล
- Recommendation ระบบเลือกมหาวิทยาลัยส่วนบุคคล
- Authentication / user accounts
- Paid proprietary job data
- Web scraping จากเว็บไซต์ที่ Terms of Service ไม่อนุญาต
- Real-time job feed แบบวินาทีต่อวินาที

---

# 5. Core Technology Requirements

## 5.1 Backend

ใช้ **Python**

Recommended stack:

```text
Python 3.11+
pandas
polars (optional)
numpy
plotly
dash
dash-bootstrap-components
fastapi (optional API layer)
pydantic
duckdb
sqlalchemy
pyarrow
scikit-learn (optional for text similarity)
rapidfuzz
sentence-transformers (optional for course-skill semantic mapping)
```

## 5.2 Frontend / Dashboard

Preferred:

```text
Dash + Plotly
```

Alternative:

```text
FastAPI backend
+ React frontend
+ Plotly.js
```

สำหรับงานนี้ให้ Antigravity **prefer Dash + Plotly** หากไม่มีข้อจำกัดอื่น เพราะทำ linked filtering และ Python-first development ได้เร็วกว่า

## 5.3 Data storage

Phase 1:

```text
Raw data      -> /data/raw/
Processed     -> /data/processed/
Analytics     -> DuckDB
Config        -> YAML / JSON
```

Recommended DB:

```text
DuckDB
```

เหตุผล:
- อ่าน CSV / Parquet ได้เร็ว
- ไม่ต้องมี database server
- เหมาะกับ analytical dashboard
- deploy ง่าย

---

# 6. Information Architecture

Dashboard มี 3 tabs:

```text
TAB 1
ปริมาณคนที่จบและ Skills ที่เรียนมา

TAB 2
ปริมาณงานที่จ้างและ Skills ที่ต้องการ

TAB 3
Skills Mismatch Analysis
```

Global header:

```text
Dashboard title
Last updated
Data sources
Methodology
Download filtered data
Reset filters
```

---

# 7. Global Filters

Global filters ต้อง persist ระหว่าง tabs เมื่อ field นั้นมีความหมายร่วมกัน

## Required filters

- Year / Graduation year / Job posting year
- Country
- Region / State / Province (ถ้ามี)
- Domain
  - AI
  - Data Science
  - Statistics
- Degree level
  - Bachelor
  - Master
  - Doctoral
- Institution / University
- Program
- Career level
  - Entry
  - Intermediate
  - Expert
- Company
- Skill category

## Interaction rule

เมื่อผู้ใช้เลือกค่า:

```text
Filter / point / bar / cell / program / skill
→ update all related charts in current tab
→ save filter state
→ Tab 3 can consume selected context
```

---

# 8. Domain Classification

ใช้ 3 domain หลัก:

| domain_id | Domain |
|---|---|
| AI | Artificial Intelligence |
| DS | Data Science |
| STAT | Statistics |

หลักสูตรหรืองานหนึ่งรายการสามารถอยู่มากกว่า 1 domain ได้

ตัวอย่าง:

```text
Machine Learning Engineer
→ AI + Data Science

Biostatistician
→ Statistics

Data Scientist
→ Data Science + Statistics
```

ต้องใช้ mapping table แยก ไม่ hard-code ใน chart

---

# 9. Career Level Taxonomy

ใช้ 3 ระดับสำหรับ visualization หลัก

## Entry

Mapping เช่น:

```text
Internship
Entry Level
Junior
Associate
0–2 years experience
```

ตัวอย่างตำแหน่ง:
- Junior Data Analyst
- Junior Data Scientist
- ML Intern
- Junior Statistician

## Intermediate

Mapping:

```text
Mid-Level
Mid-Senior
Senior
2–7 years
```

ตัวอย่าง:
- Data Scientist
- ML Engineer
- Applied Statistician
- Senior Data Analyst

## Expert

Mapping:

```text
Staff
Principal
Lead
Director
Head
VP
Executive
7+ years
```

ตัวอย่าง:
- Principal Data Scientist
- AI Research Scientist
- Lead Statistician
- Head of Data
- Head of AI

> เก็บ original seniority จาก source ไว้ด้วย และสร้าง `career_level_normalized` เพิ่ม

---

# 10. TAB 1 — ปริมาณคนที่จบและ Skills ที่เรียนมา

## 10.1 Business Question

> ในแต่ละปี หลักสูตรด้าน AI / Data Science / Statistics ผลิตบัณฑิตได้เท่าไร สอนอะไรบ้าง ค่าเทอมเท่าไร และบัณฑิตเข้าสู่ตลาดแรงงานได้เร็วแค่ไหน?

---

# 11. TAB 1 — KPI Cards

ด้านบนของ Tab 1 ต้องมี KPI อย่างน้อย:

```text
Total graduates
Number of programs
Number of institutions
Average tuition
Graduate employment Year 1
Graduate employment Year 2
Graduate employment Year 3
```

KPI ต้อง update ตาม filter selection

---

# 12. TAB 1 — Chart 1
## ชื่อหลักสูตร + จำนวนบัณฑิตที่ผลิตในแต่ละปี

### Business requirement

แสดง:
- ชื่อมหาวิทยาลัย
- ชื่อหลักสูตร
- Domain
- จำนวนผู้จบ/จำนวนวุฒิ
- ปี

### Recommended visualization

Primary:

```text
Plotly line chart
x = year
y = graduates
color = program_name
```

Alternative view:

```text
Stacked bar
```

User toggle:

```text
Line / Bar
```

### Required interactions

คลิกชื่อหลักสูตรหรือเส้น:

```text
Selected program
→ filter course chart
→ filter employment outcome
→ filter tuition
→ update KPI cards
```

### Tooltip

```text
University
Program
Domain
Year
Graduates
Degree Level
Country
Source
```

---

# 13. TAB 1 — Chart 2
## รายวิชาบังคับของแต่ละหลักสูตรที่ตรงกับการทำงาน

### Business requirement

แสดงรายวิชา **บังคับ** ของหลักสูตร และ skill ที่แต่ละรายวิชาครอบคลุม

ตัวอย่าง:

```text
Machine Learning
→ Python
→ scikit-learn
→ model evaluation
→ supervised learning

Statistical Inference
→ probability
→ hypothesis testing
→ regression
→ statistical modeling
```

### Visualization

Recommended:

```text
Heatmap
rows    = courses
columns = normalized skills
value   = mapping strength
```

หรือ:

```text
Horizontal bar
skill coverage count
```

พร้อม toggle:

```text
Course × Skill Heatmap
Skill Coverage
Course List
```

### Interaction

เลือก program จาก Chart 1:

```text
→ Chart 2 แสดงเฉพาะหลักสูตรนั้น
```

คลิก skill:

```text
→ highlight courses ที่สอน skill นั้น
→ ส่ง selected_skill เข้า Tab 3
```

---

# 14. Course-to-Skill Mapping

ต้องมี taxonomy กลาง

## Skill categories

```text
Programming
Statistics & Mathematics
Machine Learning
AI / Deep Learning
Data Engineering
Database
Cloud
Visualization / BI
Experimentation
MLOps
NLP
Computer Vision
Generative AI / LLM
Research
Communication
Business / Domain
Leadership
```

### Mapping schema

```text
course_id
course_name
course_description
skill_id
skill_name
skill_category
mapping_method
mapping_score
is_required_course
```

### mapping_method

```text
manual
keyword
semantic
hybrid
```

Phase 1:
prefer manual + keyword dictionary

Phase 2:
semantic embedding mapping

---

# 15. TAB 1 — Chart 3
## จำนวนบัณฑิตที่ได้งานทำ ปีที่ 1 / ปีที่ 2 / ปีที่ 3 หลังเรียนจบ

### Business requirement

แสดง outcome หลังเรียนจบ

Metrics:

```text
employed_year_1
employed_year_2
employed_year_3
employment_rate_year_1
employment_rate_year_2
employment_rate_year_3
```

### Preferred visualization

```text
Grouped bar
x = program
y = employment rate
color = Year after graduation
```

Alternative:

```text
Cohort survival-style line
x = years after graduation
y = cumulative employment %
```

### Required user toggle

```text
Count
Rate (%)
```

### Important

หาก source มีเพียง 1 ปีหลังเรียนจบ:
- ห้ามสร้าง Year 2 / Year 3 เอง
- แสดง N/A
- แสดง data availability flag

---

# 16. TAB 1 — Chart 4
## ค่าเทอม

### Metrics

```text
tuition_total
tuition_per_year
tuition_per_credit
currency
program_duration
```

### Visualization

Preferred:

```text
Horizontal bar
y = program
x = total tuition
```

Optional:

```text
Bubble:
x = tuition
y = graduate employment rate
size = graduate count
```

### Currency

ต้องเก็บ original currency

สร้าง:

```text
tuition_original
currency_original
tuition_usd_normalized
```

ถ้าแปลงค่าเงินต้องเก็บ:

```text
fx_date
fx_source
```

---

# 17. TAB 1 — Cross-filter Behavior

ตัวอย่าง interaction:

```text
User selects:
Domain = Data Science
Year = 2024

Chart 1:
เลือก Program A

Result:
Chart 2 → courses ของ Program A
Chart 3 → employment outcome Program A
Chart 4 → tuition Program A
KPI → Program A
```

หากเลือก skill ใน Chart 2:

```text
Chart 1
→ highlight programs ที่สอน skill

Chart 3
→ compare employment outcomes ของ programs เหล่านั้น

Chart 4
→ compare tuition
```

---

# 18. TAB 2 — ปริมาณงานที่จ้างและ Skills ที่ต้องการ

## 18.1 Business Question

> ตลาดมีตำแหน่งว่างเท่าไร ต้องการ skills อะไร บริษัทไหนรับ และเงินเดือนแตกต่างตามระดับงานอย่างไร?

---

# 19. TAB 2 — KPI Cards

```text
Total job postings / job openings
Unique companies
Unique job titles
Median salary
Entry median salary
Intermediate median salary
Expert median salary
Top demanded skill
```

---

# 20. TAB 2 — Chart 1
## ปริมาณตำแหน่งที่ว่าง

### Metrics

ต้องแยกประเภท metric ชัดเจน:

```text
job_posting_count
annual_openings
employment_stock
```

ห้ามนำ 3 ตัวนี้รวมกันโดยไม่มี label

### Preferred visualization

```text
Line chart
x = time
y = job_posting_count
color = domain
```

หรือ:

```text
Stacked bar by career level
```

### Filters

- Domain
- Job title
- Career level
- Country
- Company
- Year

### Tooltip

```text
Job title
Domain
Career level
Country
Count
Date / year
Source
```

---

# 21. TAB 2 — Chart 2
## Skills ที่ตลาดต้องการ

### Business requirement

แสดง skill ที่ถูกระบุใน job description / requirements

### Recommended visualization

Primary:

```text
Horizontal bar
y = skill
x = demand %
```

User toggle:

```text
Demand %
Posting Count
Required Count
```

Alternative advanced view:

```text
Skill × Career Level Heatmap
```

### Must support

```text
Entry
Intermediate
Expert
```

### Click interaction

คลิก skill:

```text
→ filter companies
→ filter job openings
→ filter salary
→ send selected skill to Tab 3
```

---

# 22. TAB 2 — Chart 3
## บริษัทที่รับ

### Visualization

Recommended:

```text
Treemap
company -> job count
```

Alternative:

```text
Ranked horizontal bar
```

Tooltip:

```text
Company
Number of postings
Top job titles
Top skills
Median salary
Country
```

Click company:

```text
→ update vacancy
→ update skills
→ update salary
```

---

# 23. TAB 2 — Chart 4
## เงินเดือนในแต่ละระดับการทำงาน

### Required levels

```text
Entry
Intermediate
Expert
```

### Preferred visualization

```text
Box plot
x = career_level
y = salary_annual_normalized
color = domain
```

Alternative:

```text
Bar:
Median + P25/P75
```

### Required salary metrics

```text
P10
P25
Median
P75
P90
```

ถ้ามีข้อมูลเพียง salary range:

```text
salary_min
salary_max
salary_midpoint
```

ต้อง label ว่า derived

---

# 24. TAB 2 — Cross-filter Behavior

ตัวอย่าง:

```text
User clicks skill = Python

Job Vacancy Chart
→ เหลือเฉพาะ jobs ที่ต้องการ Python

Company Chart
→ rank บริษัทที่ประกาศ Python jobs

Salary Chart
→ salary distribution ของ Python-demanding jobs

KPI
→ update ทั้งหมด
```

User clicks company:

```text
skill chart
→ skills ที่บริษัทนั้นต้องการ

vacancy
→ positions ของบริษัทนั้น

salary
→ salary distribution ของบริษัทนั้น
```

---

# 25. TAB 3 — Skills Mismatch Analysis

## 25.1 Business Question

> Skills ที่หลักสูตรสอน เทียบกับ Skills ที่ตลาดต้องการ มีช่องว่างตรงไหน?

---

# 26. Skill Mismatch Definitions

สร้าง normalized skill universe:

```text
skill_id
skill_name
skill_category
aliases
```

ตัวอย่าง:

```text
Python
aliases:
python programming
python3

SQL
aliases:
sql
structured query language

Machine Learning
aliases:
ml
machine learning
predictive modeling
```

---

# 27. Supply Skill Score

จาก Tab 1:

```text
SupplySkillScore(skill)
```

แนะนำสูตร Phase 1:

```text
SupplySkillScore
=
0.5 * ProgramCoverage
+
0.3 * RequiredCourseCoverage
+
0.2 * GraduateWeightedCoverage
```

Scale:

```text
0–100
```

Definitions:

```text
ProgramCoverage
= % programs ที่สอน skill

RequiredCourseCoverage
= % programs ที่มี skill ในวิชาบังคับ

GraduateWeightedCoverage
= % graduates ที่มาจาก programs ที่สอน skill
```

---

# 28. Demand Skill Score

จาก Tab 2:

```text
DemandSkillScore(skill)
```

Recommended:

```text
DemandSkillScore
=
0.6 * PostingDemand
+
0.2 * RequiredMention
+
0.2 * SalaryPremium
```

Scale:

```text
0–100
```

หาก salary premium ไม่มีข้อมูล:

```text
DemandSkillScore
=
0.75 * PostingDemand
+
0.25 * RequiredMention
```

---

# 29. Mismatch Score

Primary formula:

```text
MismatchScore
=
DemandSkillScore - SupplySkillScore
```

Interpretation:

```text
+30 to +100
High shortage
ตลาดต้องการมากกว่าหลักสูตรสอน

+10 to +29
Moderate shortage

-9 to +9
Balanced

-29 to -10
Possible oversupply

-100 to -30
High oversupply
```

ต้องให้ threshold configurable

---

# 30. TAB 3 — Main Visuals

## Chart A — Skill Gap Quadrant

Plotly scatter:

```text
x = Supply Skill Score
y = Demand Skill Score
size = job posting count
color = skill category
text = skill
```

Quadrants:

```text
High Demand / Low Supply
→ Priority Gap

High Demand / High Supply
→ Strong Alignment

Low Demand / High Supply
→ Possible Oversupply

Low Demand / Low Supply
→ Low Priority
```

---

## Chart B — Top Skill Gaps

```text
Horizontal diverging bar

x = MismatchScore
y = Skill
```

Positive:

```text
market shortage
```

Negative:

```text
education oversupply
```

---

## Chart C — Program vs Market Match

Matrix:

```text
rows = program
columns = demanded skills
value = coverage / match score
```

ตัวอย่าง:

```text
Program A
Python       100
SQL           75
Cloud         20
MLOps          0
Communication 60
```

---

## Chart D — Career Level Gap

Heatmap:

```text
rows = skills
columns =
Entry
Intermediate
Expert

value = Demand - Supply
```

---

## Chart E — Program Readiness Score

Program score:

```text
ReadinessScore =
weighted average of market-demand skills covered by program
```

แสดง:

```text
Program
Readiness Score
Graduate count
Tuition
Employment Year 1
```

Recommended Plotly:

```text
Bubble chart
x = tuition
y = readiness score
size = graduate count
color = year-1 employment rate
```

---

# 31. Tab 3 Cross-filtering

Tab 3 ต้องรับ filters จาก Tabs 1–2

ตัวอย่าง:

```text
Tab 1:
Program = MSc Data Science

Tab 2:
Career Level = Entry

Tab 3:
compare MSc Data Science curriculum
against Entry-level job skill demand
```

User clicks a mismatch skill:

```text
→ show courses teaching that skill
→ show companies demanding that skill
→ show salary distribution
```

---

# 32. Core Data Sources

Phase 1 ใช้ Open Data / public-use ที่ license/status ชัดเจน

## Education / Graduates

### NCES IPEDS

ใช้สำหรับ:
- degree/completion counts
- institution
- program classification
- year
- award level

Core CIP:

```text
11.0102 Artificial Intelligence
30.7001 Data Science, General
30.7099 Data Science, Other
27.0501 Statistics, General
```

---

# 33. Curriculum Data

จุดนี้ **IPEDS ไม่ได้ให้รายวิชารายหลักสูตร**

จึงต้องมี source เพิ่ม เช่น:

- official university curriculum pages
- open course catalogs
- university open data
- official downloadable curriculum PDFs/CSV

## Phase 1 requirement

Antigravity ต้องออกแบบ ingestion แบบ pluggable:

```text
curriculum_sources/
    institution_a.py
    institution_b.py
```

หรือ ingest จาก curated CSV:

```text
programs.csv
courses.csv
course_skills.csv
```

ถ้ายังไม่มี open machine-readable source:

```text
อนุญาตให้ใช้ manually curated dataset
แต่ต้องมี source_url
และ source_type = official curriculum
```

---

# 34. Graduate Employment Outcomes

IPEDS ไม่มี metric “ได้งานปีที่ 1/2/3” สำหรับทุกหลักสูตรโดยตรง

ดังนั้นระบบต้องรองรับหลาย source เช่น:

```text
graduate outcomes survey
government longitudinal education-employment data
university alumni outcomes
national graduate survey
```

Schema ต้องรองรับ:

```text
graduation_cohort
months_after_graduation
employment_count
employment_rate
source
```

ถ้าประเทศ/มหาวิทยาลัยไม่มีข้อมูล:

```text
display:
No public data available
```

ห้าม interpolate หรือ fabricate

---

# 35. Tuition Data

ใช้:

- official university tuition page
- public university fee tables
- government higher-education datasets

ต้องเก็บ:

```text
institution
program
academic_year
tuition_amount
currency
fee_type
source_url
```

---

# 36. Labor Demand Data

Recommended:

## BLS OEWS

ใช้:
- employment
- wage
- occupation

SOC:

```text
15-2051 Data Scientists
15-2041 Statisticians
15-1221 Computer and Information Research Scientists
```

15-1221 ต้อง label:

```text
AI-related proxy
```

ไม่ใช้คำว่า:

```text
total AI jobs
```

---

# 37. Open Job Posting Data

ใช้สำหรับ:

- job posting count
- company
- job title
- salary
- skills
- seniority

ระบบต้องรองรับอย่างน้อย:

```text
job_postings
companies
job_skills
salary
location
seniority
```

และเก็บ:

```text
snapshot_date
```

เพราะ job posting dataset มักเป็น snapshot

---

# 38. Skill Data

รองรับ:

- O*NET
- open job-skill datasets
- course-skill dictionary
- manually reviewed aliases

Skill normalization pipeline:

```text
raw skill
↓
lowercase / cleanup
↓
alias matching
↓
canonical skill
↓
skill category
```

---

# 39. Recommended Data Model

## dim_program

```text
program_id
institution_id
program_name
degree_level
domain
country
region
cip_code
program_url
```

## dim_institution

```text
institution_id
institution_name
country
region
institution_type
```

## fact_graduates

```text
program_id
year
graduates
award_level
source_id
```

## fact_tuition

```text
program_id
year
tuition_total
tuition_per_year
currency
tuition_usd
source_id
```

## fact_graduate_outcome

```text
program_id
graduation_year
months_after_graduation
employment_count
employment_rate
source_id
```

## dim_course

```text
course_id
program_id
course_code
course_name
is_required
credits
description
```

## bridge_course_skill

```text
course_id
skill_id
mapping_score
mapping_method
```

## dim_skill

```text
skill_id
skill_name
skill_category
aliases
```

## fact_jobs

```text
job_id
posting_date
company_id
job_title
domain
career_level
country
region
salary_min
salary_max
salary_mid
currency
salary_usd
source_id
```

## bridge_job_skill

```text
job_id
skill_id
is_required
mention_count
```

## dim_company

```text
company_id
company_name
industry
country
```

## dim_source

```text
source_id
source_name
source_url
license
retrieved_at
snapshot_date
```

---

# 40. API / Backend Requirements

หากใช้ Dash อย่างเดียว callbacks สามารถ query DuckDB ได้โดยตรง

แต่แนะนำ service layer แยก

Example endpoints:

```text
GET /api/filters
GET /api/programs
GET /api/graduates
GET /api/curriculum
GET /api/graduate-outcomes
GET /api/tuition

GET /api/jobs
GET /api/job-skills
GET /api/companies
GET /api/salaries

GET /api/mismatch
GET /api/program-readiness
```

Common query params:

```text
year
country
region
domain
degree_level
program_id
career_level
company_id
skill_id
```

---

# 41. Plotly / Dash Callback Architecture

ห้ามเขียน callback แบบซ้ำซ้อนทุก chart ถ้าหลีกเลี่ยงได้

Recommended architecture:

```text
Global Filter Store
        ↓
Tab Filter Store
        ↓
Filtered Data Service
        ↓
Chart callbacks
```

Dash components:

```text
dcc.Store(id="global-filter-store")
dcc.Store(id="tab1-selection-store")
dcc.Store(id="tab2-selection-store")
dcc.Store(id="mismatch-context-store")
```

---

# 42. Connected Charts Requirement

ทุก chart ต้องรองรับอย่างน้อย:

```text
clickData
selectedData
relayoutData
```

ตามความเหมาะสม

Crossfilter pattern:

```text
Graph A click
↓
update selection store
↓
query filtered dataframe
↓
Graph B, C, D update
↓
KPI update
```

ต้องมี:

```text
Clear selection
Reset tab filters
Reset all
```

---

# 43. URL State / Shareable View

Recommended:

เก็บ filter state ใน query string เช่น:

```text
?domain=DS&year=2025&level=entry&skill=python
```

เพื่อให้ user share dashboard state ได้

Phase 1 optional  
Phase 2 recommended

---

# 44. Data Validation Rules

## Graduate data

```text
graduates >= 0
year valid
program_id required
```

## Salary

```text
salary_min <= salary_max
currency not null
normalization date present
```

## Skill

```text
canonical skill_id required after normalization
```

## Employment outcome

```text
0 <= employment_rate <= 1
months_after_graduation >= 0
```

---

# 45. Missing Data Behavior

ห้ามแทน missing เป็น 0 โดยอัตโนมัติ

UI ต้องแยก:

```text
0
= มีข้อมูลและค่าเท่ากับศูนย์

N/A
= ไม่มีข้อมูล

Not reported
= source ไม่รายงาน
```

---

# 46. Data Provenance

ทุก chart ต้องสามารถ trace กลับ source ได้

Tooltip/footer:

```text
Source
Dataset year
Snapshot date
License
Last updated
```

มี modal:

```text
About this data
```

---

# 47. Salary Normalization

เก็บ salary ทั้ง original และ normalized

```text
salary_original
currency_original
salary_usd
fx_rate
fx_date
```

หาก hourly:

```text
annualized_salary =
hourly_rate * hours_per_week * weeks_per_year
```

defaults:

```text
hours_per_week = 40
weeks_per_year = 52
```

ต้องระบุว่าเป็น derived

---

# 48. Skill Match Methodology

## Exact matching

```text
Python = Python
SQL = SQL
```

## Alias matching

```text
PostgreSQL → SQL / Database
PyTorch → Deep Learning
TensorFlow → Deep Learning
Tableau → Data Visualization
Power BI → Data Visualization
```

## Semantic matching

ตัวอย่าง:

```text
Applied Predictive Modelling
≈ Machine Learning
```

Phase 1:
dictionary + manual review

Phase 2:
embedding similarity

---

# 49. Recommended Skill Taxonomy

## Programming

```text
Python
R
Java
C++
Scala
Julia
```

## Statistics & Mathematics

```text
Probability
Statistical Inference
Regression
Bayesian Statistics
Linear Algebra
Calculus
Experimental Design
Time Series
```

## Data

```text
SQL
Data Cleaning
Data Wrangling
ETL
Data Modeling
Data Warehousing
```

## AI / ML

```text
Machine Learning
Deep Learning
NLP
Computer Vision
Generative AI
LLM
Reinforcement Learning
```

## Engineering

```text
Git
Docker
Kubernetes
MLOps
CI/CD
APIs
```

## Cloud

```text
AWS
Azure
GCP
```

## BI / Visualization

```text
Tableau
Power BI
Plotly
Matplotlib
Dashboarding
```

## Professional

```text
Communication
Problem Solving
Business Acumen
Presentation
Teamwork
Leadership
Research
```

---

# 50. UI Layout

Desktop:

```text
------------------------------------------------
Header
------------------------------------------------
Global filters
------------------------------------------------
Tabs:
[ Graduate Supply ] [ Job Demand ] [ Mismatch ]
------------------------------------------------
KPI cards
------------------------------------------------
Main charts
------------------------------------------------
Supporting charts
------------------------------------------------
Data notes / source
------------------------------------------------
```

Responsive:
- Desktop first
- Tablet supported
- Mobile readable but not necessarily full analytical experience

---

# 51. Visual Design Requirements

Style:

```text
clean
academic
data-driven
minimal
```

Color logic:

```text
AI           = one consistent category color
Data Science = one consistent category color
Statistics   = one consistent category color
```

Mismatch:

```text
shortage     = warm side
balanced     = neutral
oversupply   = cool side
```

Antigravity สามารถเลือก exact colors ตาม accessibility

ต้องผ่าน:
- color contrast
- colorblind-friendly palettes
- ไม่ใช้สีอย่างเดียวเพื่อสื่อสถานะ

---

# 52. Chart Requirements

ทุก chart:

- responsive
- Plotly toolbar
- hover
- zoom ถ้าเหมาะสม
- filter-aware title
- no-data state
- source annotation
- download image
- consistent category order

---

# 53. Performance Requirements

Target:

```text
Initial load < 5 seconds
Filter update < 2 seconds
Typical chart callback < 1.5 seconds
```

Optimization:

```text
Parquet
DuckDB
pre-aggregation
memoization / cache
```

Do not load raw million-row job dataset into browser

---

# 54. Caching

Recommended:

```text
Flask-Caching
diskcache
Redis optional
```

Cache key:

```text
dataset_version
+
filter_state
+
metric
```

---

# 55. Data Refresh

สร้าง ETL command:

```bash
python -m app.etl.refresh
```

หรือ:

```bash
make refresh-data
```

Pipeline:

```text
download
→ validate
→ normalize
→ map skills
→ build parquet
→ load DuckDB
→ create aggregates
→ QA report
```

---

# 56. Project Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── layout.py
│   ├── callbacks/
│   │   ├── global_filters.py
│   │   ├── tab1.py
│   │   ├── tab2.py
│   │   └── tab3.py
│   │
│   ├── charts/
│   │   ├── supply.py
│   │   ├── demand.py
│   │   └── mismatch.py
│   │
│   ├── services/
│   │   ├── graduate_service.py
│   │   ├── curriculum_service.py
│   │   ├── labor_service.py
│   │   ├── skill_service.py
│   │   └── mismatch_service.py
│   │
│   ├── data/
│   │   ├── db.py
│   │   ├── queries.py
│   │   └── schemas.py
│   │
│   └── utils/
│       ├── salary.py
│       ├── filters.py
│       └── formatting.py
│
├── etl/
│   ├── ipeds.py
│   ├── curriculum.py
│   ├── graduate_outcomes.py
│   ├── jobs.py
│   ├── onet.py
│   ├── skills.py
│   └── build_db.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── analytics.duckdb
│
├── config/
│   ├── skill_taxonomy.yaml
│   ├── domain_mapping.yaml
│   ├── career_levels.yaml
│   └── sources.yaml
│
├── tests/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# 57. Minimum Viable Product (MVP)

## MVP 1

Tab 1:
- graduate counts
- program list
- curriculum skills
- tuition
- employment outcome ถ้ามี source

Tab 2:
- jobs
- skills
- company
- salary
- career level

Tab 3:
- skill supply score
- skill demand score
- mismatch score
- skill gap quadrant
- top skill gaps

---

# 58. Phase 2

- หลายประเทศ
- curriculum NLP extraction
- semantic skill matching
- historical trend
- forecast demand
- scenario analysis
- university benchmarking
- degree ROI
- recommendation engine

---

# 59. Acceptance Criteria — Global

ระบบถือว่าผ่านเมื่อ:

1. มี 3 tabs ตาม specification
2. Python เป็น backend
3. Plotly เป็น chart library หลัก
4. ทุกกราฟใน tab เชื่อมกันผ่าน filters/selections
5. Reset filters ทำงาน
6. Export filtered data ได้
7. ทุก chart ระบุ source
8. ไม่มีการสร้างค่าที่ source ไม่มี
9. Missing data แสดง N/A
10. Tab 3 ใช้ข้อมูลจาก Tab 1 + Tab 2 จริง

---

# 60. Acceptance Criteria — Tab 1

ต้องมี:

- Program × Graduate Trend
- Required Courses × Skills
- Employment Year 1 / 2 / 3
- Tuition
- KPI cards
- linked interaction

Example acceptance:

```text
Given:
user selects Program A

When:
selection is applied

Then:
course chart
employment chart
tuition chart
KPI cards

must all update to Program A
```

---

# 61. Acceptance Criteria — Tab 2

ต้องมี:

- Vacancy count
- Demand skills
- Companies
- Salary by career level
- KPI cards
- linked interaction

Example:

```text
Given:
skill = Python

Then:
jobs
companies
salary

must represent only jobs mapped to Python
```

---

# 62. Acceptance Criteria — Tab 3

ต้องมีอย่างน้อย:

```text
Skill Gap Quadrant
Top Mismatch Skills
Program × Skill Matrix
Career Level Gap
```

เลือก skill จาก Tab 3:

```text
ต้องสามารถเห็น
- program/course ที่สอน
- job/company ที่ต้องการ
```

---

# 63. Testing Requirements

## Unit tests

- skill normalization
- salary normalization
- career level mapping
- mismatch calculation
- filter query

## Data tests

- duplicate job IDs
- impossible salary
- missing program IDs
- skill mapping coverage
- source metadata present

## UI tests

- filter propagation
- reset
- tab change
- no data
- chart click
- export

---

# 64. Logging

Log:

```text
app startup
dataset loaded
ETL status
callback errors
query time
```

ห้าม log personal user data ที่ไม่จำเป็น

---

# 65. Error Handling

User-friendly states:

```text
No data for selected filters
Data source temporarily unavailable
Unable to calculate mismatch because education data is missing
Salary data unavailable
```

ห้ามแสดง raw Python exception ให้ user

---

# 66. Download / Export

User ต้องสามารถ:

```text
Download filtered table as CSV
Download chart image
```

Optional:

```text
Download summary report as HTML/PDF
```

---

# 67. Source Metadata Config

ตัวอย่าง:

```yaml
sources:

  ipeds:
    name: NCES IPEDS
    type: education
    license: public-use
    url: https://nces.ed.gov/ipeds/

  bls:
    name: US Bureau of Labor Statistics
    type: labor
    license: public-domain
    url: https://www.bls.gov/

  onet:
    name: O*NET
    type: skills
    license: CC-BY-4.0
    url: https://www.onetcenter.org/
```

---

# 68. Important Methodology Rules

## Rule 1

IPEDS completion:

```text
awards / degrees conferred
```

ไม่ควร label เป็น:

```text
unique people
```

จนกว่าจะยืนยัน source

UI default label:

```text
จำนวนวุฒิ/ผู้จบที่รายงาน
```

---

## Rule 2

ห้ามเทียบ:

```text
annual graduates
/
employment stock
```

แล้วเรียกเป็น:

```text
probability of employment
```

---

## Rule 3

แยก:

```text
employment stock
annual openings
job postings
hires
```

---

## Rule 4

BLS SOC 15-1221:

```text
AI-related occupation proxy
```

---

## Rule 5

P10 wage:

```text
entry salary proxy
```

ไม่ใช่ official graduate starting salary

---

# 69. Dashboard Story Flow

## Tab 1

Narrative:

```text
มหาวิทยาลัยผลิตคนออกมากี่คน
↓
เรียน skill อะไร
↓
ลงทุนค่าเทอมเท่าไร
↓
หลังจบได้งานเร็วแค่ไหน
```

## Tab 2

```text
ตลาดเปิดงานกี่ตำแหน่ง
↓
ต้องการ skill อะไร
↓
บริษัทใดรับ
↓
เงินเดือนเท่าไร
```

## Tab 3

```text
Supply Skill
VS
Demand Skill
↓
Gap
↓
หลักสูตรควรเสริมอะไร
```

---

# 70. Key Output Metrics

## Education Supply

```text
graduates
program count
graduate growth %
required-skill coverage
tuition
employment outcome
```

## Labor Demand

```text
job posting count
annual openings
demand %
company count
salary
```

## Mismatch

```text
supply skill score
demand skill score
mismatch score
program readiness score
```

---

# 71. Suggested Dashboard Labels

ใช้คำใน UI ให้เข้าใจง่าย:

```text
จำนวนผู้จบ
หลักสูตร
Skills ที่เรียน
รายวิชาบังคับ
ได้งานหลังจบ
ค่าเทอม

ตำแหน่งงาน
Skills ที่ตลาดต้องการ
บริษัทที่รับ
เงินเดือน

Skills Mismatch
ตลาดต้องการมากกว่าที่สอน
สอดคล้องกัน
หลักสูตรสอนมากกว่าความต้องการ
```

---

# 72. Antigravity Development Instructions

Antigravity ให้ทำงานตามลำดับดังนี้

## Step 1 — Setup

สร้าง Python project:

```text
Dash
Plotly
DuckDB
Pandas
```

---

## Step 2 — Build schemas

สร้าง schema ตาม section `Recommended Data Model`

---

## Step 3 — Mock data first

ก่อนต่อ real dataset ให้สร้าง mock data ที่มี:

```text
3 domains
5+ programs
3+ years
20+ skills
3 career levels
20+ companies
```

เพื่อทดสอบ linked interactions

---

## Step 4 — Build Global Filter Store

ต้องเสร็จก่อน chart callbacks

---

## Step 5 — Implement Tab 1

ลำดับ:

```text
KPI
Graduate trend
Curriculum skill heatmap
Employment outcome
Tuition
Cross-filter
```

---

## Step 6 — Implement Tab 2

```text
KPI
Job vacancy
Demand skills
Companies
Salary
Cross-filter
```

---

## Step 7 — Implement Tab 3

```text
Skill score engine
Mismatch engine
Quadrant
Gap bar
Program matrix
Career level heatmap
```

---

## Step 8 — Connect real data

เริ่มจาก:

```text
IPEDS
BLS/O*NET
Open job posting dataset
```

แล้วค่อยเพิ่ม:

```text
curriculum
tuition
graduate outcome
```

---

## Step 9 — QA

ตรวจ:

```text
filter propagation
missing values
methodology labels
source metadata
salary units
year alignment
```

---

# 73. Definition of Done

งานถือว่า Done เมื่อผู้ใช้สามารถทำ scenario นี้ได้:

```text
1. เปิด Dashboard

2. เลือก:
   Domain = Data Science
   Year = 2024

3. Tab 1 แสดง:
   หลักสูตร
   จำนวนผู้จบ
   skill ที่เรียน
   ค่าเทอม
   การได้งานหลังจบ

4. เลือก Skill = Python

5. Tab 2 แสดง:
   จำนวน jobs ที่ต้องการ Python
   บริษัทที่รับ
   เงินเดือนตาม career level

6. ไป Tab 3

7. Dashboard แสดง:
   Supply Python
   Demand Python
   Mismatch score
   programs ที่สอน
   companies ที่ต้องการ
```

ทั้งหมดต้องเกิดโดยไม่ต้อง reload page

---

# 74. Final Handoff Prompt for Antigravity

```text
Develop a production-structured interactive dashboard based strictly on this BRD.

Technical constraints:
- Python backend
- Plotly as the primary visualization library
- Prefer Dash + Plotly
- DuckDB for analytical storage
- All charts within each tab must be cross-filtered and react to user selections
- Preserve filter state across tabs where applicable
- Use a normalized skill taxonomy shared by curriculum and job-posting datasets
- Never fabricate unavailable Year 1/2/3 graduate outcomes
- Clearly distinguish graduates, employment stock, job openings and job postings
- Treat SOC 15-1221 only as an AI-related proxy
- Display source, snapshot/year and license metadata

Tabs:
1. Graduate Supply & Learned Skills
2. Job Demand & Required Skills
3. Skills Mismatch Analysis

Start by:
1. Creating the project architecture
2. Building mock data matching the final schema
3. Implementing all linked Plotly interactions
4. Creating the 3-tab UI
5. Adding data service and DuckDB layers
6. Then connecting real open datasets

Do not simplify the cross-filtering requirement.
Every major chart must participate in dashboard state updates.
```

---

# 75. Deliverables Expected from Antigravity

Antigravity ต้องส่งมอบ:

```text
1. Working Python project
2. requirements.txt
3. README.md
4. data schema
5. mock data
6. ETL modules
7. DuckDB database builder
8. Dash UI
9. linked callbacks
10. 3 tabs
11. source metadata
12. tests
13. run instructions
```

Run command ควรเป็นประมาณ:

```bash
pip install -r requirements.txt
python app/main.py
```

หรือ:

```bash
python -m app.main
```

จากนั้นเปิด:

```text
http://localhost:8050
```

---

# 76. Priority Matrix

## P0 — Must Have

- Python backend
- Plotly charts
- 3 tabs
- cross-filter
- graduate trend
- curriculum skill
- employment outcome
- tuition
- job count
- demand skill
- company
- salary
- skill mismatch
- source metadata

## P1 — Should Have

- Export CSV
- chart export
- shareable filter state
- caching
- source modal
- readiness score

## P2 — Nice to Have

- semantic skill mapping
- forecasts
- recommendation
- multi-country FX normalization
- automated curriculum NLP

---

# 77. Final Product Principle

Dashboard นี้ไม่ใช่เพียงการ “โชว์กราฟ”

แต่ต้องทำให้ user เดินเรื่องได้แบบ:

```text
Supply of Graduates
        ↓
Skills Taught
        ↓
Graduate Outcome

VS

Job Demand
        ↓
Skills Required
        ↓
Companies + Salary

        ↓

Skills Mismatch
```

ทุก tab ต้องเชื่อมกันเชิงข้อมูล และทุก visualization ต้องช่วยตอบคำถามหลักของโครงการอย่างชัดเจน
