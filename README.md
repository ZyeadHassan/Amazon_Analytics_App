# 📊 Amazon Sales ETL & Analytics App  

This is an **ETL (Extract – Transform – Load) and Analytics project** built with **Streamlit**.  
The app works on Amazon product data to generate insights and recommendations for business decisions.  

---

## 🚀 Project Workflow  

- **ETL**  
  - Extract raw data.  
  - Transform (Clean & Prepare):  
    - Remove unwanted symbols (₹, %, ,).  
    - Convert columns to numeric values.  
    - Handle missing values.  
    - Extract main categories from category column.  
    - Drop irrelevant columns (links, reviews).  
    - Remove duplicates.  
  - Load the cleaned dataset for analytics.  

- **Analytics (Streamlit App)**  
  - **Data Overview**: summary of the dataset after cleaning.  
  - **Data Analytics**: KPIs and charts, including:  
    - Top Categories by Products Count  
    - Price Distribution  
    - Rating Distribution  
    - Discount by Category  
    - Discount by Products  
    - Top Rated Categories  
  - **Insights & Recommendations**: highlights from the analysis and suggested actions.  

---


