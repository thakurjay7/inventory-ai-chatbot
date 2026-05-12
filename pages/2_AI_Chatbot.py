import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")

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

    Give a short and clear business answer.
    """

    try:
        response = model.generate_content(prompt)

        st.success(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
