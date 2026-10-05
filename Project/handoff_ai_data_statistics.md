# AI / Data Science / Statistics — Handoff

1. Research objective
สร้างเรื่องเล่าที่ตอบว่า “ถ้าเรียน AI, Data Science หรือ Statistics แล้ว ตลาดแรงงานต้องการคนมากแค่ไหน เงินเดือนประมาณเท่าไร บริษัทไหนมีประกาศงาน และต้องมี skill อะไรเมื่อโตจาก Entry → Intermediate → Expert?”
ข้อจำกัดสำคัญ: BLS ไม่มี SOC ที่เท่ากับ “AI jobs ทั้งหมด” ดังนั้น 15-1221 ใช้เป็น AI-related research proxy และต้องเสริมด้วย open job-posting data.
2. Education supply
OPEN: NCES public-use

Dataset: IPEDS Completions C2024_A

Filter: AI 11.0102 · Data Science 30.7001/30.7099 · Statistics 27.0501

Output: completions by field × award level × year.

Download C2024_A.zip

IPEDS data page

3. Employment & salary
OPEN: BLS public domain

SOC: Data Scientist 15-2051 · Statistician 15-2041 · AI proxy 15-1221

2025 refs: DS employment 262,440; median $120,230; P10 <$67,240. Statistician employment 29,030; median $105,650; P10 <$64,000. Computer & Information Research Scientist median $140,300; P10 <$82,200.

Rule: P10 = entry-pay proxy, ไม่ใช่ official starting salary.

Download OEWS national ZIP

Download OEWS all-data ZIP

4. Open source registry
Source	License/status	Use	Direct download
NCES IPEDS C2024_A	Public-use	จำนวนวุฒิ/ผู้จบตาม CIP	C2024_A.zip
BLS OEWS May 2025	Public domain	employment + wage percentiles	National ZIP
O*NET 31.0	CC BY 4.0	occupation + software/essential skills	Software skills CSV
Qarera Skills 2026	CC BY 4.0	skills from 360k+ postings + seniority	Skills by role CSV
Datamata Skill Demand Index	CC BY 4.0	required skills in AI/data job listings	CSV
data_jobs	MIT	company + title + salary + skills	job_postings.csv
5. Company analysis

ใช้ data_jobs และ filter job title แล้ว group by company_name.

ตัวอย่างบริษัทที่ปรากฏใน corpus: Capital One, Oracle, Siemens, Pfizer, Adobe, TikTok, Thermo Fisher Scientific, PwC, Ford, Agoda.

คำค้น: AI / Artificial Intelligence / Machine Learning / Data Scientist / Statistician / Biostatistician / Statistical / Quantitative.

companies.csv · job_skills.csv · salaries.csv

6. Skills from job postings

Qarera: ใช้ `skills-2026-by-role.csv` แล้วเลือก role_family = Data Scientist / ML.

Datamata: เลือก category = data หรือ ai แล้ว sort `demand_pct` / `required_count`.

O*NET: ใช้ SOC 15-2051, 15-2041, 15-1221 เพื่ออธิบาย occupational skills และ software technologies.

Qarera skills by role

Datamata skill demand

7. Seniority mapping
Entry — Internship + Entry Level
Roles: Junior Data Analyst / Junior Data Scientist / ML Intern / Junior Statistician
Core: Python/R, SQL, descriptive & inferential statistics, visualization, communication.
Intermediate — Mid-Senior Level
Roles: Data Scientist / ML Engineer / Applied Statistician / Senior Analyst
Core: modeling, experimentation, pipelines, cloud, Git, deployment, stakeholder communication.
Expert — Principal + Director + VP + Executive
Roles: Principal/Staff Data Scientist / AI Research Scientist / Lead Statistician / Head of Data/AI
Core: architecture, advanced modeling, MLOps/LLMOps, research, governance, leadership.

Method note: การรวมเป็น 3 ระดับเป็น analyst-defined aggregation จาก seniority labels ใน open job-posting datasets ไม่ใช่มาตรฐาน BLS.

Download AI seniority CSV

8. Next AI — task checklist
Download + parse IPEDS C2024_A; aggregate CIP 11.0102, 30.7001/30.7099, 27.0501 by award level.
Download OEWS May 2025; extract SOC 15-2051, 15-2041, 15-1221 and wage percentiles.
Create table: employment, median, P10 entry proxy, typical education, country.
Extract Top 10 Data Scientist/ML skills from Qarera and AI/data required skills from Datamata.
Filter data_jobs by role keywords; rank employers and summarize salary/location.
Map seniority → Entry / Intermediate / Expert and compare skill mix.
Produce 4–5 presentation visuals with year, source, license and caveat on every chart.
9. Quality controls
อย่าเรียก completions ว่า unique graduates โดยไม่ตรวจ definition.
อย่าปะปน employment stock, openings, job postings และ hires.
AI 15-1221 = proxy; ห้ามกล่าวว่าเป็น AI jobs ทั้งหมด.
P10 = entry-pay proxy; ห้ามเรียกว่า official starting salary.
ทุกกราฟต้องมีปี/snapshot + country + source + license.
บริษัทจาก job-posting corpus = ปรากฏใน dataset ไม่ใช่หลักฐานว่ากำลังเปิดรับ “วันนี้”.
10. Notes for next AI / team
11. Suggested story for presentation
Opening: “คนเรียนสาย AI/Data เพิ่มขึ้น แต่คำถามสำคัญไม่ใช่แค่ว่าเรียนอะไร — ตลาดต้องการคนแบบไหน?”

Core: เทียบ supply (IPEDS graduates) → demand (BLS employment/openings) → pay → skills from real job postings → career ladder.

Ending: “ชื่อวุฒิเป็นเพียงจุดเริ่มต้น สิ่งที่เชื่อมผู้เรียนเข้ากับงานจริงคือ skill stack ที่เปลี่ยนตามระดับอาชีพ”