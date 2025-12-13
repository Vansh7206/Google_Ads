<h1>🚀 Google Ads Performance Analysis (SQL + Python)</h1>

This project is an end-to-end analysis of Google Ads performance data, focused on understanding how ads perform across devices, keyword intent, cost, clicks, leads, conversions, and revenue.

The objective is to simulate how a real marketing/data analyst evaluates ad campaigns to identify what works, what doesn’t, and where optimization is needed.

<h1>📂 What This Project Includes</h1>

- Data cleaning & preprocessing using Python (Pandas)
- Business-logic-driven handling of missing values
- Feature engineering (CPC, Conversion Rate, Keyword Category)
- Loading cleaned data into PostgreSQL
- 20 SQL queries covering:
- Campaign performance
- Device-wise analysis
- Keyword intent analysis
- Funnel metrics (Clicks → Leads → Conversions)
- Cost, revenue, and ROI insights
- High-level analytical SQL (subqueries, views, window functions)

<h1>📊 Dataset Overview</h1>

Each row represents one Google Ad’s performance.
- Key Metrics
- Clicks, Impressions – Engagement metrics
- Leads, Conversions – Funnel metrics
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
- Funnel analysis queries
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

<h1>📈 Visualizations (Coming Soon)</h1>

Planned visual analysis using:
- Matplotlib
- Seaborn
- Power BI
- Upcoming visuals will include:
- Funnel performance charts
- Device-wise ROI dashboards
- Keyword intent effectiveness
- Cost vs sales trends

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