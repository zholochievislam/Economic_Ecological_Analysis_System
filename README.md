# Economic & Ecological Analysis System
> **A SQL-based relational database exploring the link between economic growth and ecological impact worldwide (2014–2024)**

![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557c?style=flat)
![Countries](https://img.shields.io/badge/Coverage-88_Countries-2E8B57?style=flat)
![Years](https://img.shields.io/badge/Years-2014--2024-orange?style=flat)

---

## 📌 Overview

This project integrates multiple global datasets — **GDP per capita, population, inflation, CO₂ emissions, safe water access, and forest loss** — into a single relational database. It supports complex analytical SQL queries and visualizations that reveal patterns of sustainable vs. harmful economic growth, regional disparities, and long-term trends across nearly a decade of global data.

The system is designed to provide clear, reliable insights for policymakers, analysts, and researchers working on sustainability studies, risk assessment, and global development monitoring.

**Scope at a glance:**

| | |
|---|---|
| 🗓 **Time range** | 2014 – 2024 |
| 🌐 **Countries covered** | 88 |
| 🗺 **Regions** | 6 |
| 🗄 **Database entities** | 5 (normalized relational schema) |
| 📈 **Indicators tracked** | GDP per capita, Population, Inflation, CO₂ emissions, Safe Water Access, Tree/Forest Loss |

---

## 🛠 Tech Stack

* **Database:** MySQL (relational schema, analytical SQL queries)
* **Data Processing:** Python (Pandas — cleaning, merging, normalization)
* **Visualization:** Matplotlib (scatter, bar, line, pie, column charts)

---

## 📂 Repository Structure

```text
PythonProject/
│
├── data/                    # Raw source CSV datasets (World Bank, Our World in Data)
├── data_cleaning/           # Python scripts: inspection, cleaning, merging, normalization
├── ER_Model/                # Entity-Relationship diagrams (conceptual + relational model)
├── sql/                     # Database schema (DDL) + analytical SQL queries
├── plots/                   # Generated visualizations (PNG)
├── project_presentation/    # Slide deck summarizing the project
└── Report.docx              # Full written report (abstract → conclusion)
```

---

## 🗄 Database Design

The database follows a normalized relational schema built around **5 core entities**:

| Entity | Description |
|---|---|
| **Country** | List of all countries and their region |
| **Economic_Indicator** | Defines each economic indicator and its unit of measurement |
| **Ecologic_Indicator** | Defines each ecological indicator and its unit of measurement |
| **Econ_Data** | Yearly economic values, linked to a country + indicator |
| **Ecol_Data** | Yearly ecological values, linked to a country + indicator |

**Relationships:**
- Each country → many economic and ecological records (one-to-many)
- Each indicator → many data points across time (one-to-many)
- Every fact table joins on **both** `CountryID` and `Year`, ensuring accurate one-to-one matching across datasets

<p align="center">
  <img src="./ER_Model/er_diagram.png" width="700" alt="ER Diagram">
  <br><em>Conceptual ER Model — 5 entities linked via CountryID and Year</em>
</p>

---

## 🔍 Analytical Queries

Queries are organized into four categories:

* **Comparative Analysis** — GDP growth vs. CO₂ growth ("green growth" vs. harmful growth), "Green Paradox" countries (high GDP *and* high CO₂), the effect of forest fire loss on population
* **Top-N Rankings** — highest inflation rates, best safe water access, top GDP per capita (with percentage share)
* **Regional Distribution** — global forest fire loss by region, population distribution by region
* **Time-Series Analysis** — GDP trend of a single country over time, side-by-side country comparisons

All analytical queries rely on explicit `CAST()` operations (values were stored as `VARCHAR` in source files), multi-key joins (`CountryID` + `Year`), and conditional aggregation (`SUM(CASE WHEN ...)`) to pivot multi-country comparisons into single rows.

---

## 📊 Visualizations & Key Findings

| Visualization | Insight |
|---|---|
| 🟢 **Green Countries** (High GDP, Low CO₂) | Identifies countries achieving strong economic output while keeping emissions low — evidence of sustainable growth |
| 🔴 **Dirty Countries** (Low GDP, High CO₂) | Highlights countries where growth is inefficient and environmentally costly |
| 💧 **Water Access** | Countries with the least access to safe water — frequently overlapping with lower-GDP nations |
| 🔥 **Forest Fire Loss by Region** | Reveals that **Asia** and **North America** bear the largest regional forest-fire losses |
| 📈 **GDP Trends: Italy vs. France** | Shows how two structurally similar European economies diverge over a decade |
| 📊 **Top 10 Inflation Rates (2021)** | Surfaces the countries hit hardest by price instability in a single year |

**Key takeaways:**
- Some countries achieve GDP growth **alongside** low CO₂ emissions — evidence that sustainable development is achievable, not just theoretical.
- Others show the inverse: weak GDP growth paired with rising CO₂ — a pattern of inefficient, environmentally costly development.
- Safe water access varies sharply, with lower-GDP nations disproportionately represented among those with the least access.
- Forest fire losses are heavily concentrated in specific regions (Asia, North America) rather than evenly distributed globally.
- Comparing structurally similar economies (Italy vs. France) shows that GDP trajectories can diverge significantly even between neighboring, developed nations.

---

## 🧩 Engineering Challenges & Solutions

| Problem | Root Cause | Solution |
|---|---|---|
| **Duplicated / incorrect JOIN results** | Queries joined only on `Year`, not `CountryID` — every country matched every other country in the same year | Added compound join conditions (`ON ed.CountryID = el.CountryID AND ed.Year = el.Year`) |
| **Wrong numeric calculations** | The `Value` column was stored as `VARCHAR`, breaking arithmetic operations | Applied `CAST(Value AS DECIMAL(20,4))` inside every analytical query |
| **`ONLY_FULL_GROUP_BY` errors** | Non-aggregated columns included in `SELECT` alongside `GROUP BY` | Rewrote queries with proper aggregation (`SUM`, `COUNT`, `CASE WHEN`) and complete `GROUP BY` clauses |
| **Foreign key mismatches** | Country IDs inconsistent between CSVs and the `Country` table; PK/FK data types mismatched (`INT` vs `VARCHAR`) | Standardized country names and IDs; aligned PK/FK types via `ALTER TABLE` |
| **"0 rows imported" in MySQL Wizard** | Silent failures from missing values, mismatched types, and unlisted countries | Cleaned files, standardized to UTF-8, and re-imported in small batches to isolate bad rows |
| **Overlapping/unreadable chart labels** | Every data point labeled on scatter plots with many countries | Filtered to a labeled subset, applied `tight_layout()`, adjusted font size and label placement |

---

## 📄 Documentation

- 📄 **[Full Project Report](project_presentation/Report.docx)** — Abstract, data description, cleaning pipeline, database design, queries, visualizations, discussion & conclusion
- 📊 **[Project Presentation](project_presentation/Economic-Data-and-Ecological-Impact.pptx)** — Slide deck summarizing the full workflow

---

## 🚀 How to Reproduce

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

2. **Set up a Python environment and install dependencies:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Clean & prepare the raw data:**
```bash
python data_cleaning/clean_and_merge.py
```

4. **Build the schema and load data into MySQL:**
```bash
mysql -u root -p < sql/schema.sql
# then import the five generated CSVs (Countries, Economic_Indicator,
# Ecologic_Indicator, Econ_Data, Ecol_Data) via MySQL Workbench Import Wizard
```

5. **Run the analytical queries:**
```bash
mysql -u root -p your_database_name < sql/analytical_queries.sql
```

6. **Generate the visualizations:**
```bash
python plots/generate_visualizations.py
```

---

*Developed as a data engineering & analytics portfolio project — combining relational database design, SQL analytics, and data visualization to study global sustainability trends.*
