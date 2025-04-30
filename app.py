import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Inventory Demand EDA", layout="wide")

DATA_PATH = "inventory_demand.csv"

@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        st.error(f"File '{DATA_PATH}' not found in your repo.")
        return None
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except pd.errors.EmptyDataError:
        st.error(f"File '{DATA_PATH}' is empty or improperly formatted.")
        return None

df = load_data()
if df is not None:
    st.title("📦 Inventory Demand EDA Dashboard")

    # Sidebar filters
    if 'Warehouse' in df.columns and 'Product_Code' in df.columns:
        warehouse = st.sidebar.multiselect("Select Warehouse(s):", df['Warehouse'].unique(), default=df['Warehouse'].unique())
        product_code = st.sidebar.multiselect("Select Product(s):", df['Product_Code'].unique(), default=df['Product_Code'].unique())
        filtered_df = df[(df['Warehouse'].isin(warehouse)) & (df['Product_Code'].isin(product_code))]

        st.subheader("Filtered Data Preview")
        st.dataframe(filtered_df.head(50))

        st.subheader("Demand Distribution")
        fig1, ax1 = plt.subplots()
        sns.histplot(filtered_df['Demand'], bins=30, kde=True, ax=ax1)
        st.pyplot(fig1)

        st.subheader("Average Demand per Product")
        avg_demand = filtered_df.groupby("Product_Code")['Demand'].mean().sort_values(ascending=False).head(10)
        fig2, ax2 = plt.subplots()
        avg_demand.plot(kind='bar', ax=ax2)
        plt.ylabel("Average Demand")
        st.pyplot(fig2)

        st.subheader("Total Demand by Warehouse")
        total_warehouse = filtered_df.groupby("Warehouse")['Demand'].sum()
        fig3, ax3 = plt.subplots()
        total_warehouse.plot(kind='barh', ax=ax3, color='skyblue')
        st.pyplot(fig3)
    else:
        st.warning("Dataset does not contain expected columns like 'Warehouse' and 'Product_Code'.")
