import streamlit as st
import openai
import pandas as pd

# Streamlit Page Config
st.set_page_config(
    page_title="📊 AI-Powered CSV Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar: Page Selector
with st.sidebar:
    st.header("📌 Select a Page")
    page = st.radio(
        "Navigate:",
        ["About the App", "AI-Powered CSV Chatbot"],
        index=0  # Default to "About the App"
    )

# About the App Page
if page == "About the App":
    st.title("📊 About AI-Powered CSV Chatbot")

    st.markdown("""
# 📊 AI-Powered CSV Chatbot

## 🔍 About the App
The **AI-Powered CSV Chatbot** is designed to help users analyze and interact with CSV datasets using AI. Instead of manually examining spreadsheets, you can now upload a CSV file and **chat with AI** to extract key insights, trends, and patterns.

## 🚀 How It Works
1. **Upload a CSV file** 📤 – The app reads and processes the data.
2. **AI generates insights** 🤖 – It summarizes the dataset and extracts useful patterns.
3. **Chat with AI** 💬 – Ask follow-up questions about your data.
4. **Get AI-driven responses** 📊 – Understand trends, anomalies, and key statistics.

## 🔑 Features
✅ **Automated Data Summarization** – AI extracts key insights from the uploaded dataset.  
💡 **Conversational Data Analysis** – Ask questions about the dataset, and AI will analyze and respond.  
📊 **Interactive Data Preview** – View your dataset inside the app for better understanding.  
⚡ **Fast & Efficient** – No need for complex coding or manual analysis—just upload and chat!  

---

## 🛠 How to Use
1. **Enter Your OpenAI API Key** 🔑  
   - Go to the sidebar and enter your OpenAI API key.
   - This allows the AI chatbot to function properly.

2. **Upload Your CSV File** 📂  
   - Click on the **Upload CSV** button and select a `.csv` file.
   - The app will automatically analyze and summarize the dataset.

3. **Explore AI-Generated Insights** 🔍  
   - View the dataset’s statistics, trends, and summaries.
   - Get instant insights without manually calculating anything.

4. **Ask Questions About Your Data** 💬  
   - Use the chat input to ask questions like:  
     - "What is the average value in column X?"  
     - "Are there any missing values in the dataset?"  
     - "What are the key trends in this data?"  

5. **Receive AI-Powered Responses** ⚡  
   - The AI will analyze your query and provide an answer based on the dataset.  
   - You can ask multiple follow-up questions to explore deeper insights.  

---

## 🎯 Example Use Cases
🔹 **Business Analytics** – Analyze sales data, customer behavior, and market trends.  
🔹 **Data Science & Machine Learning** – Quickly understand datasets before applying models.  
🔹 **Financial Analysis** – Extract key trends from stock, revenue, or budget data.  
🔹 **Health & Research** – Summarize patient data, survey results, or research datasets.  
🔹 **Education & Learning** – Help students explore datasets interactively with AI assistance.  

---

## 🔒 Privacy & Security
- **Your data stays private** – The app processes CSV files locally in your browser session.  
- **Your API key is not stored** – It is only used during your session for AI queries.  
- **No data is shared** – The AI does not store or send data elsewhere after processing.  

---

## 🏆 Why Use AI-Powered CSV Chatbot?
💡 **Saves Time** – No need for manual data crunching.  
🛠 **Easy to Use** – Just upload and start analyzing.  
⚡ **Powerful AI Insights** – Get expert-level analysis instantly.  
📈 **Enhances Decision-Making** – Understand your data in seconds.  

---

### 🏗 Built With:
🔹 **Streamlit** – For the interactive web interface  
🔹 **OpenAI GPT-4o** – For AI-powered analysis and chat  
🔹 **Pandas** – For efficient CSV file processing  
🔹 **Python** – For backend logic and AI interaction  

---
🚀 **Get Started Now!** Upload your CSV file and chat with AI to uncover valuable insights! 🎯


    """)

# AI-Powered CSV Chatbot Page
else:
    st.title("💬 AI-Powered CSV Chatbot")
    st.write("Upload a CSV file, and chat with AI to analyze it.")

    # Sidebar: API Key Input
    with st.sidebar:
        st.header("🔑 API Configuration")
        openai_api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
        
        if not openai_api_key:
            st.warning("⚠️ Please enter your OpenAI API Key to proceed")
            st.stop()
        st.success("API Key accepted!")

    # Function to call GPT-4o API
    def call_gpt4o(api_key, messages):
        """Calls GPT-4o API with conversation history."""
        client = openai.Client(api_key=api_key)
        try:
            response = client.chat.completions.create(model="gpt-4o", messages=messages)
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ Error: {e}"

    # Function to process CSV file
    def process_csv(api_key, uploaded_file):
        """Reads CSV, summarizes it, and provides AI-based insights."""
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state["csv_data"] = df  # Store in session for persistence
            
            csv_summary = df.describe().to_string()
            prompt = f"""
            You are an expert data analyst. Provide a detailed summary of the following dataset.
            Data Preview:
            {csv_summary}
            """
            
            insights = call_gpt4o(api_key, [{"role": "system", "content": prompt}])
            st.session_state["csv_insights"] = insights
            st.session_state["messages"].append({"role": "assistant", "content": insights})
        except Exception as e:
            st.session_state["csv_insights"] = f"❌ Error: {e}"

    # Initialize session variables
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "csv_data" not in st.session_state:
        st.session_state["csv_data"] = None
    if "csv_insights" not in st.session_state:
        st.session_state["csv_insights"] = "No insights available yet. Upload a CSV file to begin."

    # Upload CSV File
    uploaded_file = st.file_uploader("📤 Upload a CSV file", type=["csv"])
    
    # Prevent chat before CSV is uploaded
    if not uploaded_file:
        st.warning("⚠️ Please upload a CSV file to enable AI analysis and chat.")
        st.stop()
    
    if st.session_state["csv_data"] is None:
        process_csv(openai_api_key, uploaded_file)
    
    # Show CSV Preview
    st.subheader("📊 CSV Data Preview")
    st.dataframe(st.session_state["csv_data"].head())  # Show first 5 rows
    
    # Show AI Insights
    st.subheader("💡 AI Insights")
    st.write(st.session_state["csv_insights"])

    # Display chat messages
    st.subheader("💬 Chat with AI")
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # User Input for Follow-up Questions
    user_input = st.chat_input("Ask a follow-up question about your data...")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                conversation = [
                    {"role": "system", "content": "You are an AI data analyst. Answer user questions based on the dataset and chat history."},
                    {"role": "system", "content": f"The dataset has the following summary:\n{st.session_state['csv_insights']}"},
                ] + st.session_state["messages"]

                ai_response = call_gpt4o(openai_api_key, conversation)
                st.write(ai_response)

                # Append AI response to chat history
                st.session_state["messages"].append({"role": "assistant", "content": ai_response})

