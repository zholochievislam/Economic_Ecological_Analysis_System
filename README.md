# Economic & Ecological Analysis System

A SQL-based analytical database system that explores the relationship between economic performance and ecological impact across countries worldwide, using real-world data from 2014–2024.

## Overview

This project integrates multiple global datasets — GDP per capita, population, inflation, CO₂ emissions, safe water access, and forest loss — into a single relational database. It supports complex analytical queries and visualizations that reveal patterns of sustainable vs. harmful economic growth, regional disparities, and long-term trends.

The system is designed to provide clear, reliable insights for policymakers, analysts, and researchers working on sustainability studies, risk assessment, and global development monitoring.

**Scope:**
- Data covering **2014–2024**
- **88 countries** across **6 regions**
- A relational database with **5 entities**
- Indicators: GDP per capita, Population, Inflation, CO₂ emissions, Safe Water Access, Tree/Forest Loss

## Features

- **Data cleaning & preparation** — multi-stage pipeline for inspecting, cleaning, filtering, and merging raw CSV datasets
- **Relational database design** — normalized schema with 5 core entities and clear one-to-many relationships
- **Analytical SQL queries** — comparative analysis, top-N rankings, regional distribution, and time-series trends
- **Data visualization** — scatter plots, bar charts, line plots, pie charts, and column charts built from query results

## Data Description

| Category | Indicators |
|---|---|
| **Economic** | GDP per capita, Population, Inflation |
| **Ecological** | CO₂ emissions, Safe Water Access, Tree/Forest Loss |

Each row represents a **country–indicator–year** combination, sourced from trusted global datasets (e.g. World Bank, Our World in Data).

## Database Design

The database consists of five main entities:

1. **Country** — list of all countries and their regions
2. **Economic_Indicator** — defines each economic indicator and its unit of measurement
3. **Ecologic_Indicator** — defines each ecological indicator and its unit of measurement
4. **Econ_Data** — yearly economic values linked to a country and indicator
5. **Ecol_Data** — yearly ecological values linked to a country and indicator

**Relationships:**
- Each country can have many economic and ecological records (one-to-many)
- Each indicator can have many data points across time (one-to-many)
- Years and values are stored consistently to simplify comparison and filtering

## Analytical Queries

The project includes queries across four main categories:

- **Comparative Analysis** — GDP growth vs. CO₂ growth, "Green Paradox" countries, effect of forest fire on population
- **Top-N Rankings** — highest inflation rates, best safe water access, top GDP per capita
- **Regional Distribution** — global forest fire loss by region, population distribution
- **Time-Series Analysis** — GDP trends of individual countries over time

## Visualizations

Query results were turned into the following visualizations:

- **Green Countries** — high GDP, low CO₂ emissions
- **Dirty Countries** — low GDP, high CO₂ emissions
- **Water Access** — countries with the least access to safe water
- **Forest Fire Loss** — global forest fire loss by region
- **GDP Trends** — GDP of Italy vs. France over time
- **Inflation Rates** — top 10 countries by inflation rate (2021)

## Key Findings

- Some countries achieved GDP growth alongside low CO₂ emissions, indicating **sustainable development**.
- Others showed low GDP growth paired with high CO₂ growth, suggesting **less efficient, more environmentally damaging development**.
- Access to safe water varies significantly, with lower-GDP nations often having the highest number of people without clean water.
- Forest fire data highlighted significant regional losses, particularly in **Asia** and **North America**.
- Comparing similar economies (e.g., Italy vs. France) revealed how countries can follow divergent economic paths.

## Tech Stack

- **Database:** MySQL (relational schema, SQL queries)
- **Data processing:** Python (data cleaning, merging, normalization)
- **Visualization:** Matplotlib

## Challenges & Solutions

Throughout the project, several challenges were encountered and resolved:

- **Data quality** — missing values, inconsistent formats, and merging conflicts across raw datasets were resolved through systematic cleaning and standardization.
- **Foreign key & data type errors** — mismatched ID formats and column types (e.g., values stored as `VARCHAR` instead of numeric types) caused import and query failures; resolved by aligning schema types and using `CAST()` in queries.
- **Join logic errors** — incomplete join conditions initially produced incorrect or duplicated results; fixed by joining on both country and year.
- **Visualization readability** — overlapping labels and messy plots were fixed with proper Matplotlib formatting (`tight_layout`, label filtering, sizing).

## Project Structure

This project's report and presentation walk through the full workflow:

1. Data description
2. Data cleaning
3. Database design
4. Data loading
5. Analytical queries
6. Visualization
7. Discussion & conclusion

## Documentation

- 📄 Full project report (Word document)
- 📊 Project presentation (slides)
