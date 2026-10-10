import pandas as pd
import numpy as np

#loading datset
df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

#checking for null values in total charges column
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].isnull().sum()
df = df.dropna(subset=['TotalCharges'])

#Exploratory Data Analysis (EDA) & Data Cleaning Verification।
# how many customers have churned and how many have not churned
print(df['Churn'].value_counts(normalize=True) * 100)
#hom many duplicate rows are present in the dataset
print("Duplicate rows:", df.duplicated().sum())
#Hom many null values are present in the dataset
print("Null values:", df.isnull().sum().sum())


#after checking the value is ok then this value must be save as csv clean file 
df.to_csv('Telco_Customer_Churn_Cleaned.csv', index=False)
print("Cleaned file saved successfully!")

from sqlalchemy import create_engine

server = r'DESKTOP-8LOAKQG\SQLEXPRESS'
database = 'TelcoDB'
table_name = 'CustomerChurn'
# Windows Authentication using trusted_connection=yes
engine = create_engine(f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")
# datafrmae are save to table_name = 'CustomerChurn'

# ৪. এসকিউএল সার্ভারে ডেটা পাঠানো
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print(f"Data successfully loaded into {database} under table '{table_name}'!")