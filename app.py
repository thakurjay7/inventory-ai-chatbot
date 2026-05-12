import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="StockPilot AI",
    layout="wide"
)

# -----------------------------------
# HOME PAGE
# -----------------------------------

st.title("Welcome to StockPilot AI")

st.subheader("AI-Powered Retail Inventory Intelligence Platform")

st.write("""
Retail store managers often struggle with inventory stockouts, overstocking,
and delayed replenishment decisions due to fragmented inventory data and
lack of predictive insights.

StockPilot AI solves this problem by combining inventory analytics,
forecasting, reorder intelligence, and AI-powered recommendations
into a single interactive platform.
""")

# -----------------------------------
# PROBLEM STATEMENT
# -----------------------------------

st.subheader("⚠️ Problem Statement")

st.write("""
Traditional inventory systems provide only basic stock monitoring and
require manual analysis for replenishment planning.

This creates multiple challenges:

- Stockouts causing lost sales
- Overstocking increasing carrying costs
- Delayed supplier coordination
- Lack of predictive inventory visibility
- Complex inventory analysis for managers
- Poor real-time decision support
""")

# -----------------------------------
# OUR SOLUTION
# -----------------------------------

st.subheader("🚀 Our Solution")

st.write("""
StockPilot AI is an intelligent inventory assistant that helps retail
managers make faster and smarter inventory decisions.

The platform provides:

✅ Real-time inventory monitoring  
✅ AI-driven stock risk analysis  
✅ Predictive inventory forecasting  
✅ Smart reorder recommendations  
✅ Supplier lead-time intelligence  
✅ AI-generated business insights  
✅ Conversational inventory assistant  
✅ Interactive analytics dashboard  
""")

# -----------------------------------
# AVAILABLE MODULES
# -----------------------------------

st.subheader("📂 Available Modules")

st.write("""
### 📊 Dashboard
Visual inventory analytics with KPI metrics, forecasting,
reorder intelligence, and stock health monitoring.

### 🤖 AI Chatbot
Conversational AI assistant for inventory-related queries,
risk analysis, and business recommendations.

### ⚠️ Alerts
Smart alert system for critical stock levels,
future stockout prediction, and reorder urgency.
""")

# -----------------------------------
# FUTURE ENHANCEMENTS
# -----------------------------------

st.subheader("🔮 Future Enhancements")

st.write("""
Potential future upgrades for enterprise-scale deployment:

- Real-time supplier API integration
- Advanced ML demand forecasting
- Automated purchase order generation
- Multi-store inventory optimization
- Role-based access management
- Real-time notification system
- ERP / SAP integration
- Cloud database integration
""")

# -----------------------------------
# FOOTER
# -----------------------------------

st.success(
    "✅ Built for AI-driven retail inventory optimization and decision intelligence."
)
