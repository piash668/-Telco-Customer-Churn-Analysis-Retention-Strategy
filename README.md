# 📊 Telco Customer Churn Analysis & Retention Strategy

## 📑 Table of Contents
- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Tech Stack Used](#%EF%B8%8F-tech-stack-used)
- [Key Business Insights](#-key-business-insights)
- [Dashboard Preview](#%EF%B8%8F-dashboard-preview)
- [Project Workflow](#%EF%B8%8F-project-workflow)
- [How to Run This Project](#-how-to-run-this-project)

---

## 🔍 Project Overview
The primary objective of this project is to analyze customer churn (customers discontinuing service) for a telecommunications provider. The raw dataset was cleaned and transformed using Python, loaded into MS SQL Server for database querying, and visualized in Power BI through an interactive executive dashboard to deliver actionable business insights.

---

## 💼 Business Problem
In the telecommunications industry, acquiring new customers is significantly more expensive than retaining existing ones. High customer churn directly impacts recurring revenue streams.

The key goals of this project are:
- Identify critical risk factors and behavioral patterns driving customer churn.
- Pinpoint high-risk customer segments based on contract terms, billing amounts, and service types.
- Formulate data-driven retention strategies to minimize revenue loss and improve customer loyalty.

---

## 🛠️ Tech Stack Used
- **Data Processing & Cleaning:** Python (Pandas, NumPy)
- **Database Management & Querying:** MS SQL Server (SSMS)
- **Data Visualization & Analytics:** Power BI (DAX, Power Query)
- **Version Control:** GitHub

---

## 💡 Key Business Insights
Key takeaways derived from SQL queries and Power BI visualizations:
1. **Contract Type Impact:** Customers on Month-to-month contracts exhibit the highest churn rate at **42.71%**. In contrast, Two-year contract holders demonstrate a churn rate of only **2.85%**.
2. **Payment Method Vulnerability:** Customers utilizing Electronic Checks show a churn rate of **45.29%**, making it the highest-risk payment channel compared to automated methods.
3. **Monthly Charges Effect:** The average monthly charge for churned customers is **$74.44**, whereas non-churned customers average **$61.31**. Higher recurring costs directly correlate with customer loss.
4. **Internet Service Type:** Customers on Fiber optic internet services show a substantially higher churn rate compared to DSL users.
5. **Tech Support & Security Add-ons:** Customers enrolled in value-added services such as Tech Support and Online Security exhibit significantly lower churn rates.

---

## 🖼️ Dashboard Preview
<img width="907" height="506" alt="image" src="https://github.com/user-attachments/assets/130e1f6f-ecc1-4219-b31d-943b257b796d" />


---

## ⚙️ Project Workflow
1. **Data Cleaning (Python):** Handled missing values, converted data types (such as casting `TotalCharges` to numeric), and exported the cleaned dataset to CSV.
2. **Database Integration (SQL Server):** Loaded cleaned data into MS SQL Server (`TelcoDB`) and authored analytical SQL queries for business aggregations.
3. **Data Modeling & DAX (Power BI):** Created custom DAX measures including `Total Customers`, `Total Churned`, and `Churn Rate %`.
4. **Interactive Dashboard Design:** Implemented executive KPI cards, categorical bar charts, distribution charts, and interactive slicers (Gender, Payment Method, Internet Service).

---

## 🚀 How to Run This Project
1. **Python Setup:** Run the cleaning script in Python to generate `Telco_Customer_Churn_Cleaned.csv`.
2. **Database Setup:** Create a database named `TelcoDB` in MS SQL Server and import the cleaned dataset as a table (`CustomerChurn`) using Python SQLAlchemy or the SSMS Import Wizard.
3. **Power BI Dashboard:** Open the `.pbix` file in Power BI Desktop and update the database connection settings to match your SQL Server instance name.
