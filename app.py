import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Inventory Demand EDA", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("inventory_demand.csv")

df = load_data()
st.title("📦 Inventory Demand EDA Dashboard")

# Sidebar filters
warehouse = st.sidebar.multiselect("Select Warehouse(s):", options=df['Warehouse'].unique(), default=df['Warehouse'].unique())
product_code = st.sidebar.multiselect("Select Product(s):", options=df['Product_Code'].unique(), default=df['Product_Code'].unique())

# Filter data
filtered_df = df[(df['Warehouse'].isin(warehouse)) & (df['Product_Code'].isin(product_code))]

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(50))

# Plot 1 - Demand distribution
st.subheader("Demand Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df['Demand'], bins=30, kde=True, ax=ax1)
st.pyplot(fig1)

# Plot 2 - Average demand per product
st.subheader("Average Demand per Product")
avg_demand = filtered_df.groupby("Product_Code")['Demand'].mean().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots()
avg_demand.plot(kind='bar', ax=ax2)
plt.ylabel("Average Demand")
st.pyplot(fig2)

# Plot 3 - Demand by Warehouse
st.subheader("Total Demand by Warehouse")
total_warehouse = filtered_df.groupby("Warehouse")['Demand'].sum()
fig3, ax3 = plt.subplots()
total_warehouse.plot(kind='barh', ax=ax3, color='skyblue')
st.pyplot(fig3)
