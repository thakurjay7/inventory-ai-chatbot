import streamlit as st
import pandas as pd
from google import genai

# Configure Client
client = genai.Client(
    api_key="AIzaSyAB0-MSJdahZ4cJCsuRJ3lYfCw_pS6XV3I"
)

# Page Title
st.title("🤖 AI Inventory Assistant")

st.write("Ask inventory-related questions using natural language.")

# Load Inventory Data
df = pd.read_csv("inventory.csv")

# Convert Inventory Data to Text
inventory_context = df.to_string(index=False)

# User Input
user_question = st.text_input("Ask your inventory question:")

# Generate AI Response
if user_question:

    prompt = f"""
    You are an AI-powered retail inventory assistant.

    Here is the inventory data:

    {inventory_context}

    User Question:
    {user_question}

    Give a short and clear answer.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        st.success(response.text)

    except Exception as e:
        st.error(f"Error: {e}")