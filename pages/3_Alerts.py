import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Alerts",
    layout="wide"
)

# Title
st.title("⚠️ Smart Inventory Alerts")

# Load CSV
df = pd.read_csv("inventory.csv")

# Calculate Days Remaining
df["Days Remaining"] = df["Stock"] / df["Daily_Sales"]

# Critical Alerts
critical_items = df[df["Days Remaining"] < 2]

# Warning Alerts
warning_items = df[
    (df["Days Remaining"] >= 2) &
    (df["Days Remaining"] <= 5)
]

# Critical Section
st.subheader("🚨 Critical Stock Alerts")

if len(critical_items) > 0:
    for index, row in critical_items.iterrows():
        st.error(
            f"""
            {row['Product']} stock is critical.

            Only {row['Stock']} units left.

            Estimated stockout in {row['Days Remaining']:.1f} days.
            """
        )
else:
    st.success("No critical stock alerts.")

# Warning Section
st.subheader("⚠️ Warning Alerts")

if len(warning_items) > 0:
    for index, row in warning_items.iterrows():
        st.warning(
            f"""
            {row['Product']} may require reorder soon.

            Estimated stockout in {row['Days Remaining']:.1f} days.
            """
        )
else:
    st.success("No warning alerts.")

# Full Alert Table
st.subheader("📋 Alert Summary Table")

st.dataframe(
    df[["Product", "Stock", "Daily_Sales", "Days Remaining"]]
)