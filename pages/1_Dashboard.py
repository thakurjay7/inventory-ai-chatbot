import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("🚀 StockPilot AI Dashboard")
st.subheader("AI-Powered Retail Inventory Assistant")

# -----------------------------------
# LOAD INVENTORY DATA
# -----------------------------------

df = pd.read_csv("inventory.csv")

# -----------------------------------
# KPI CALCULATIONS
# -----------------------------------

# Calculate Days Remaining
df["Days Remaining"] = df["Stock"] / df["Daily_Sales"]

# Low Stock Detection
low_stock = df[df["Stock"] < 30]

# Critical Stock Detection
critical_stock = df[df["Days Remaining"] < 2]

# Pending Reorder Detection
pending_reorders = df[df["Days Remaining"] < df["Lead_Time"]]

# -----------------------------------
# STOCK HEALTH STATUS
# -----------------------------------

def stock_status(stock):

    if stock < 20:
        return "🔴 Critical"

    elif stock < 50:
        return "🟡 Medium"

    else:
        return "🟢 Healthy"

df["Stock_Status"] = df["Stock"].apply(stock_status)

# -----------------------------------
# INVENTORY HEALTH SUMMARY
# -----------------------------------

critical_count = len(
    df[df["Stock_Status"] == "🔴 Critical"]
)

medium_count = len(
    df[df["Stock_Status"] == "🟡 Medium"]
)

healthy_count = len(
    df[df["Stock_Status"] == "🟢 Healthy"]
)

# -----------------------------------
# AI REORDER RECOMMENDATION ENGINE
# -----------------------------------

# Safety Stock
safety_stock = 20

# Reorder Quantity Formula
df["Recommended_Reorder"] = (
    (df["Daily_Sales"] * df["Lead_Time"])
    + safety_stock
    - df["Stock"]
)

# Show Only Needed Reorders
reorder_df = df[df["Recommended_Reorder"] > 0]

# -----------------------------------
# KPI CARDS
# -----------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Products",
        len(df)
    )

with col2:
    st.metric(
        "Low Stock Items",
        len(low_stock)
    )

with col3:
    st.metric(
        "Critical Items",
        len(critical_stock)
    )

with col4:
    st.metric(
        "Pending Reorders",
        len(pending_reorders)
    )

# -----------------------------------
# AI INVENTORY RISK SUMMARY
# -----------------------------------

st.subheader("🧠 AI Inventory Risk Summary")

risk_col1, risk_col2, risk_col3 = st.columns(3)

with risk_col1:
    st.error(
        f"🔴 Critical Products: {critical_count}"
    )

with risk_col2:
    st.warning(
        f"🟡 Medium Risk Products: {medium_count}"
    )

with risk_col3:
    st.success(
        f"🟢 Healthy Products: {healthy_count}"
    )

# -----------------------------------
# INVENTORY TABLE
# -----------------------------------

st.subheader("📦 Inventory Table")

st.dataframe(
    df[
        [
            "Product",
            "Stock",
            "Daily_Sales",
            "Lead_Time",
            "Supplier",
            "Stock_Status"
        ]
    ],
    use_container_width=True
)

# -----------------------------------
# INVENTORY CHART
# -----------------------------------

st.subheader("📊 Inventory Stock Levels")

fig = px.bar(
    df,
    x="Product",
    y="Stock",
    color="Product",
    title="Current Inventory Stock"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------
# AI REORDER RECOMMENDATIONS
# -----------------------------------

st.subheader("🧠 AI Reorder Recommendations")

if len(reorder_df) > 0:

    st.dataframe(
        reorder_df[
            [
                "Product",
                "Stock",
                "Daily_Sales",
                "Lead_Time",
                "Recommended_Reorder"
            ]
        ],
        use_container_width=True
    )

else:

    st.success(
        "✅ No products require reorder."
    )

# -----------------------------------
# SMART AI ALERTS
# -----------------------------------

st.subheader("🚨 Smart Inventory Alerts")

# Store alerts
critical_alerts = []
medium_alerts = []
high_demand_alerts = []
reorder_alerts = []

# Generate alerts
for index, row in df.iterrows():

    # Critical Alerts
    if row["Stock"] < 20:
        critical_alerts.append(
            f"• {row['Product']} stock is critically low."
        )

    # Medium Alerts
    elif row["Stock"] < 50:
        medium_alerts.append(
            f"• {row['Product']} stock is getting low."
        )

    # High Demand Alerts
    if row["Daily_Sales"] > 15:
        high_demand_alerts.append(
            f"• {row['Product']} has high customer demand."
        )

    # Reorder Alerts
    if row["Recommended_Reorder"] > 0:
        reorder_alerts.append(
            f"• Recommended reorder for "
            f"{row['Product']}: "
            f"{int(row['Recommended_Reorder'])} units."
        )

# -------------------------------
# DISPLAY ALERT SECTIONS
# -------------------------------

# Critical Alerts
if critical_alerts:

    st.error(
        "🔴 CRITICAL ALERTS\n\n"
        + "\n".join(critical_alerts)
    )

# Medium Alerts
if medium_alerts:

    st.warning(
        "🟡 MEDIUM RISK ALERTS\n\n"
        + "\n".join(medium_alerts)
    )

# High Demand Alerts
if high_demand_alerts:

    st.info(
        "📈 HIGH DEMAND PRODUCTS\n\n"
        + "\n".join(high_demand_alerts)
    )

# Reorder Recommendations
if reorder_alerts:

    st.success(
        "✅ REORDER RECOMMENDATIONS\n\n"
        + "\n".join(reorder_alerts)
    )



# -----------------------------------
# INVENTORY FORECASTING
# -----------------------------------

st.subheader("📉 Inventory Forecasting")

# Forecast Days
forecast_days = 7

# Predicted Future Stock
df["Forecast_Stock"] = (
    df["Stock"]
    - (df["Daily_Sales"] * forecast_days)
)

# Forecast Status
def forecast_status(stock):

    if stock < 0:
        return "🔴 Stockout Risk"

    elif stock < 20:
        return "🟡 Low Future Stock"

    else:
        return "🟢 Stable"

df["Forecast_Status"] = (
    df["Forecast_Stock"]
    .apply(forecast_status)
)

# Forecast Table
st.dataframe(
    df[
        [
            "Product",
            "Stock",
            "Daily_Sales",
            "Forecast_Stock",
            "Forecast_Status"
        ]
    ],
    use_container_width=True
)

# -----------------------------------
# FORECAST TREND CHART
# -----------------------------------

st.subheader("📈 Forecast Inventory Trend")

# Create Forecast Comparison Data
forecast_chart_df = pd.DataFrame({
    "Product": df["Product"],
    "Current Stock": df["Stock"],
    "Forecast Stock": df["Forecast_Stock"]
})

# Convert for Plotly
forecast_melted = forecast_chart_df.melt(
    id_vars="Product",
    value_vars=["Current Stock", "Forecast Stock"],
    var_name="Stock Type",
    value_name="Units"
)

# Forecast Trend Chart
forecast_fig = px.bar(
    forecast_melted,
    x="Product",
    y="Units",
    color="Stock Type",
    barmode="group",
    title="Current vs Forecast Inventory"
)

st.plotly_chart(
    forecast_fig,
    use_container_width=True
)