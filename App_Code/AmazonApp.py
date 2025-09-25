# Importing Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/amazon.csv")
df_clean = pd.read_csv("data/Amazon_Cleaned.csv")

st.title("Amazon Sales Analysis")
st.sidebar.header("Navigator")
st.sidebar.markdown(
    "Created by [Zyead Hassan](https://www.linkedin.com/in/zyead-hassan-99a850194/)"
)
sidebar_option = st.sidebar.radio(
    "choose an option",
    ["About the creator", "Data overview",
        "Data Analytics", "Insights & Recommendations"],
)

if sidebar_option == "About the creator":
    st.header("About the creator")
    st.image("images/profile.jpeg")

    st.markdown("""
    ## 🌟 About Me
        Hi there! I'm Zyead Hassan Eid.Results-driven Industrial Engineer with a strong
        foundation in process optimization,problem-solving, and analytical thinking.
        Currently transitioning into the field of Data Analysis and Data Engineering,
        leveraging solid experience in using structured approaches to improve efficiency and decision-making.
        Skilled in Python, SQL, and data visualization tools, with a passion for extracting insights from data
        to support business growth.Highly adaptable, eager to learn, and motivated to apply engineering rigor to data-driven solutions.
                
    ---
    💡 *Thanks for visiting my app!*
    """)

    st.markdown("""
🔗 **Connect with me:**  
- [GitHub](https://github.com/ZyeadHassan)  
- [LinkedIn](https://www.linkedin.com/in/zyead-hassan-99a850194/)  
- Phone : 01202959149
    """)

elif sidebar_option == "Data overview":
    st.markdown("""
    ### 📌 About the Dataset  
    This dataset contains raw product listings from **Amazon**, including product details, categories, prices, discounts, ratings, and reviews. 

---

### 📌 Description of the Raw Dataset

The raw dataset contains product listings from **Amazon**, with multiple attributes describing each item.

* **Product Details**: Product name, category, sub-categories (combined in a single column separated by `|`), and product links.  
* **Pricing Information**: Actual price and discounted price, but stored as strings (e.g., `"₹1,999"`) and mixed formats that require cleaning.  
* **Discount Information**: Discount percentage provided as strings with `%` signs.  
* **Customer Feedback**: Ratings are present but mixed with invalid symbols (e.g., `"|"`) or stored as text instead of numeric.  
* **Reviews**: Contains textual review content, which is not directly useful for quantitative business insights.  
* **Images and Links**: Each record also includes an image link and product link.  

---

### ⚠️ Key Issues Before Cleaning

* Prices and discounts stored as **strings** with symbols like "%".  
* Ratings column contains **non-numeric values**.  
* Categories stored as long **hierarchical strings**.  
* Duplicate records for the same products.  
* Presence of irrelevant columns (like `img_link`, `product_link`, and `review_content`).  

---
    """)

    if st.sidebar.checkbox("Show Raw Data Sample"):
        st.write(df.sample(10))
    elif st.sidebar.checkbox("Show Clean Data Sample"):
        st.write(df_clean.sample(10))

    st.markdown("""
    ## 🔹 Data Cleaning Plan  

    We applied several cleaning operations using **pandas** to prepare the raw Amazon dataset for analysis:  

    1. **Remove unwanted symbols**  
    - Cleaned currency symbols (`₹`) and percentage signs (`%`) from numeric columns.  
    - Converted `actual_price`, `discounted_price`, and `discount_percentage` to proper numeric types.  

    2. **Handle missing values**  
    - Filled missing values (e.g., in `rating_count`) with mean.  

    3. **Extract main categories**  
    - From the `category` column (split hierarchical categories by `|` and kept the top-level category).  

    4. **Remove duplicates**  
    - Dropped duplicate product records to ensure unique product entries.  

    5. **Drop irrelevant columns**  
    - Removed `img_link`, `product_link`, and `review_content` since they are not useful for business insights.  
    """)

elif sidebar_option == "Data Analytics":

    st.title("📊 Amazon Dataset Analysis")

    # --- KPIs Section ---
    st.subheader("📌 Key Metrics")
    st.markdown(f"""
    - **Total Sales:** ₹{7976911.28:,.2f}  
    - **Total Discount Given:** ₹{4578580.43:,.2f}  
    - **Average Discount:** {47.69:.2f}%  
    - **Median Price:** ₹{1762.5:,.2f}  
    - **High-rated Affordable Products (≤ ₹1000):** 562  
    - **Total Unique Products:** 1337  
    - **Affordable Products  (% of total):** {40.76:.2f}%
    """)

    st.markdown("---")

    # --- Charts Section ---
    st.subheader("📊 Visual Insights")

    st.markdown("### 🔹 Top Categories By Products Count")
    st.image("images/cat_by_prod.jpg",
             caption="Top Categories by Product Count")

    st.markdown("### 🔹 Price Distribution")
    st.image("images/price_dist.jpg", caption="Distribution of Prices")

    st.markdown("### 🔹 Rating Distribution")
    st.image("images/rating_dist.jpg", caption="Distribution of Ratings")

    st.markdown("### 🔹 Discount By Category")
    st.image("images/disc_by_cat.jpg", caption="Discount by Category")

    st.markdown("### 🔹 Discount By Products")
    st.image("images/disc_by_prod.jpg", caption="Top Discounted Products")

    st.markdown("### 🔹 Top Rated Categories")
    st.image("images/top_rated_cat.jpg", caption="Top Rated Categories")

elif sidebar_option == "Insights & Recommendations":

    st.title("💡 Insights & Recommendations")

    with st.expander("📌 Key Insights from the Analysis", expanded=True):
        st.markdown("""
        1. **Pricing Strategy**: Most products fall in the  range  (>₹500:<₹2000) with significant discounts  
        2. **Quality Perception**: High percentage of products have good ratings (≥4.0)  
        3. **Category Performance**: Electronics and Computers/Accessories dominate the product portfolio  
        4. **Customer Engagement**: Products receive substantial number of ratings indicating good customer interaction  
        5. **Discount Effectiveness**: No strong correlation between discount percentage and product ratings  
        6. **Value Proposition**: Several high-rated products available at affordable prices  
        """)

    # --- Recommendations Section ---
    with st.expander("✅ Recommendations", expanded=True):
        st.markdown("""
        1. **Focus on High-Rated Categories**: Invest more in categories showing consistently high ratings  
        2. **Optimize Pricing**: Consider competitive pricing for products in the ₹500-1000 range  
        3. **Leverage Customer Reviews**: Use high rating counts as social proof in marketing  
        4. **Category Expansion**: Explore opportunities in underrepresented but high-performing categories  
        5. **Discount Strategy**: Analyze if deeper discounts actually drive better ratings or just reduce margins  
        """)
