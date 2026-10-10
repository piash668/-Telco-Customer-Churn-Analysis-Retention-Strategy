
---- To find which contract person re churn and another------

SELECT 
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    CAST(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS DECIMAL(5,2)) AS ChurnPercentage
FROM CustomerChurn
GROUP BY Contract
ORDER BY ChurnPercentage DESC;

---- churn rate by payment mathod------------

SELECT 
    PaymentMethod,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    CAST(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS DECIMAL(5,2)) AS ChurnPercentage
FROM CustomerChurn
GROUP BY PaymentMethod
ORDER BY ChurnPercentage DESC;

---  Average Monthly Charges------

SELECT 
    Churn,
    COUNT(*) AS TotalCustomers,
    CAST(AVG(MonthlyCharges) AS DECIMAL(10,2)) AS AvgMonthlyCharges,
    CAST(AVG(TotalCharges) AS DECIMAL(10,2)) AS AvgTotalCharges
FROM CustomerChurn
GROUP BY Churn;

