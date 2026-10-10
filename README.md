📊 Telco Customer Churn Analysis & Retention Strategy
📑 Table of Contents
Project Overview

Business Problem

Tech Stack Used

Key Business Insights

Dashboard Preview

Project Workflow

How to Run This Project

🔍 Project Overview
The primary objective of this project is to analyze customer churn (customers discontinuing service) for a telecommunications provider. The raw dataset was cleaned and transformed using Python, loaded into MS SQL Server for database querying, and visualized in Power BI through an interactive executive dashboard to deliver actionable business insights.

💼 Business Problem
In the telecommunications industry, acquiring new customers is significantly more expensive than retaining existing ones. High customer churn directly impacts recurring revenue streams.

The key goals of this project are:

Identify critical risk factors and behavioral patterns driving customer churn.

Pinpoint high-risk customer segments based on contract terms, billing amounts, and service types[cite: 2, 5].

Formulate data-driven retention strategies to minimize revenue loss and improve customer loyalty.

🛠️ Tech Stack Used
Data Processing & Cleaning: Python (Pandas, NumPy)

Database Management & Querying: MS SQL Server (SSMS)

Data Visualization & Analytics: Power BI (DAX, Power Query)

Version Control: GitHub

💡 Key Business Insights
Key takeaways derived from SQL queries and Power BI visualizations:

Contract Type Impact: Customers on Month-to-month contracts exhibit the highest churn rate at 42.71%[cite: 2]. In contrast, Two-year contract holders demonstrate a churn rate of only 2.85%[cite: 2].

Payment Method Vulnerability: Customers utilizing Electronic Checks show a churn rate of 45.29%, making it the highest-risk payment channel compared to automated methods[cite: 2].

Monthly Charges Effect: The average monthly charge for churned customers is $74.44, whereas non-churned customers average $61.31[cite: 2]. Higher recurring costs directly correlate with customer loss.

Internet Service Type: Customers on Fiber optic internet services show a substantially higher churn rate compared to DSL users[cite: 5, 6].

Tech Support & Security Add-ons: Customers enrolled in value-added services such as Tech Support and Online Security exhibit significantly lower churn rates[cite: 5, 6].

🖼️ Dashboard Preview
(Upload your dashboard screenshot to the repository and update the image link below)

⚙️ Project Workflow
Data Cleaning (Python): Handled missing values, converted data types (such as casting TotalCharges to numeric), and exported the cleaned dataset to CSV.

Database Integration (SQL Server): Loaded cleaned data into MS SQL Server (TelcoDB) and authored analytical SQL queries for business aggregations[cite: 1, 2].

Data Modeling & DAX (Power BI): Created custom DAX measures including Total Customers, Total Churned, and Churn Rate %[cite: 3].

Interactive Dashboard Design: Implemented executive KPI cards, categorical bar charts, distribution charts, and interactive slicers (Gender, Payment Method, Internet Service)[cite: 3, 6].

🚀 How to Run This Project
Python Setup: Run the cleaning script in Python to generate Telco_Customer_Churn_Cleaned.csv.

Database Setup: Create a database named TelcoDB in MS SQL Server and import the cleaned dataset as a table (CustomerChurn) using Python SQLAlchemy or the SSMS Import Wizard[cite: 1].

Power BI Dashboard: Open the .pbix file in Power BI Desktop and update the database connection settings to match your SQL Server instance name.
