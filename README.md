📊 Google Ads Performance Analysis (SQL + Python)
📌 Project Overview

This project focuses on analyzing Google Ads campaign performance using SQL and Python.
The goal is to extract meaningful business insights related to cost, clicks, conversions, revenue, devices, and keyword intent, similar to how a real marketing/data analyst works.

The dataset represents ad-level performance data for a Data Analytics Course campaign.

🗂 Dataset Description

Each row represents one ad’s performance with metrics related to user engagement and revenue.

Key Columns

Ad_ID – Unique ad identifier

Campaign_Name – Campaign associated with the ad

Clicks, Impressions, Leads, Conversions – Funnel metrics

Cost, Sale_Amount, CPC – Financial metrics

Conversion_Rate – Conversions per click

Ad_Date – Date when the ad ran

Device, Location – User context

Keyword, Keyword_Category – Search intent analysis

🧹 Data Cleaning & Feature Engineering

The dataset was cleaned and prepared using Python (Pandas):

Handled missing values using business-logic-driven imputation

Maintained relationships between interconnected columns (Clicks, Cost, CPC, Conversion Rate)

Standardized date formats

Created derived metrics:

CPC (Cost per Click)

Keyword_Category (intent-based grouping)

The cleaned dataset was then loaded into PostgreSQL for analysis.

🛢 SQL Analysis (PostgreSQL)

All analytical queries were executed in pgAdmin 4.

SQL Topics Covered

Aggregations (SUM, AVG, COUNT)

Grouping by device, campaign, keyword category

Funnel analysis (Clicks → Leads → Conversions)

Cost & revenue analysis

ROI-focused queries

Window functions (RANK)

Performance comparison against averages

View creation for reusable KPIs

Example Insights Generated

Total cost, sales, clicks, impressions

Device-wise CPC, sales, and conversion performance

Keyword category performance (avg & total clicks, leads, conversions)

Ads with high spend but low conversions

Best-performing devices and keyword intents

SQL queries and outputs are saved for reproducibility.