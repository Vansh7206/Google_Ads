<h1>🚀 Google Ads Performance Analysis (SQL + Python)</h1>

This project delivers an end-to-end analytical pipeline for Google Ads performance evaluation, examining campaign behavior across device types, keyword intent categories, cost metrics, user engagement (clicks & leads), conversion outcomes, and revenue generation.

The objective is to mirror a production-level data analyst workflow, including data cleaning, feature engineering, SQL-based analysis, statistical exploration, and visualization. The analysis focuses on performance attribution, efficiency measurement (CPC, conversion rate, ROI), and identifying optimization opportunities to improve campaign profitability and decision-making.

<h1>📂 What This Project Includes</h1>

- Data cleaning & preprocessing using Python (Pandas)
- Business-logic-driven handling of missing values
- Feature engineering (CPC, Conversion Rate, Keyword Category)
- Loading cleaned data into PostgreSQL
- 20 SQL queries covering:
- Campaign performance
- Device-wise analysis
- Keyword intent analysis
- Cost, revenue, and ROI insights
- High-level analytical SQL (subqueries, views, window functions)

<h1>📊 Dataset Overview</h1>

Each row represents one Google Ad’s performance.
- Key Metrics
- Clicks, Impressions – Engagement metrics
- Cost, Sale_Amount, CPC – Financial metrics
- Conversion_Rate – Conversions per click
- Contextual Attributes
- Campaign_Name
- Device (Desktop / Mobile / Tablet)
- Location
- Keyword & Keyword_Category (intent-based)
- Ad_Date

<h1>🧹 Data Cleaning & Feature Engineering</h1>

The dataset was cleaned and prepared using Python (Pandas) with a strong focus on preserving business logic.

<h4>Key steps:</h4>

1. Handled missing values without breaking relationships between columns
2. Cleaned interconnected metrics in the correct dependency order
(Clicks → Cost → CPC → Conversion Rate)
3. Standardized date formats
4. Created intent-based Keyword_Category
5. Recalculated derived metrics instead of blindly imputing them
6. Cleaned data was then loaded into PostgreSQL for analysis.

<h1>🛢 SQL Analysis (PostgreSQL)</h1>

All analysis was performed in pgAdmin 4.

<h4>SQL Concepts Used</h4>

- GROUP BY, HAVING
- Aggregate functions (SUM, AVG, COUNT)
- Subqueries & comparison against averages
- Window functions (RANK)
- Performance & ROI analysis

<h1>💡 Key Insights Generated</h1>

- Device-wise cost efficiency and conversion performance
- Keyword intent categories driving the highest revenue
- Ads with high spend but poor conversion (optimization opportunities)
- Funnel drop-offs between clicks, leads, and conversions
- Campaign-level cost vs revenue effectiveness
- CPC and conversion trends across devices

<h1>📊 Visualizations</h1>

The project includes comprehensive data visualizations created using Matplotlib and Seaborn to explore trends, performance, and relationships within Google Ads campaign data.

<h3>📌 Visual Analysis Implemented Using:</h3>

- Matplotlib
- Seaborn

<h4>📈 Visualizations Covered:</h4>

Funnel Performance Analysis
1. Visualizing the drop-off from impressions → clicks → leads → conversions to understand campaign efficiency.
2. Device-wise Performance Analysis
Comparing cost, clicks, conversions, and ROI across devices (Mobile, Desktop, Tablet).
3. Keyword Intent Effectiveness
Analyzing how different keyword intents (Informational, Commercial, Transactional) perform in terms of conversions and revenue.
4. Cost vs Sales / Revenue Trends
Scatter plots and trend analysis to evaluate how advertising spend impacts sales and revenue.
5. Distribution Analysis
Box plots and violin plots to understand spread and variability in cost, conversions, and revenue.
6. Correlation Heatmaps
Identifying relationships between impressions, clicks, cost, leads, conversions, conversion rate, and sales amount.

These visualizations help translate raw campaign data into actionable insights, similar to how a real-world data analyst evaluates marketing performance.

<h3>POWER BI Dashboard</h3>
![alt text](dashboards/image.png)


<h1>🛠 Tools & Technologies</h1>

- Python (Pandas)
- PostgreSQL
- pgAdmin 4
- SQL
- Power BI (planned)
- Matplotlib & Seaborn (planned)

<h1>🎯 Skills Demonstrated</h1>

- SQL for real-world data analysis
- Business-oriented thinking
- Data cleaning with dependency-aware logic
- Funnel and performance analysis
- KPI creation and interpretation
- Clean project structuring and documentation

<h1>📬 Author</h1>

Vansh Chandan

Aspiring Data Analyst

SQL | Python | Power BI