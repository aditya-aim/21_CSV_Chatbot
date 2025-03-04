import streamlit as st
import openai
import pandas as pd

# Streamlit Page Config
st.set_page_config(
    page_title="📊 AI-Powered CSV Chatbot",
    page_icon="💬",
    layout="wide"
)

# Function to call GPT-4o API
def call_gpt4o(api_key, messages):
    """Calls GPT-4o API with conversation history."""
    client = openai.Client(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
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
        return f"❌ Error: {e}"

# Streamlit Chatbot Interface
def main():
    st.title("💬 AI-Powered CSV Chatbot")
    st.write("Upload a CSV file, and chat with AI to analyze it.")

    # Sidebar: API Key Input
    with st.sidebar:
        st.header("🔑 API Configuration")
        openai_api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")

        if not openai_api_key:
            st.warning("⚠️ Please enter your OpenAI API Key to proceed")
            return
        st.success("API Key accepted!")

    # Initialize session variables
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "csv_data" not in st.session_state:
        st.session_state["csv_data"] = None

    # Upload CSV File
    uploaded_file = st.file_uploader("📤 Upload a CSV file", type=["csv"])

    if uploaded_file:
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
                # Append system prompt + chat history
                conversation = [
                    {"role": "system", "content": "You are an AI data analyst. Answer user questions based on the dataset and chat history."},
                    {"role": "system", "content": f"The dataset has the following summary:\n{st.session_state['csv_insights']}"},
                ] + st.session_state["messages"]

                ai_response = call_gpt4o(openai_api_key, conversation)
                st.write(ai_response)

                # Append AI response to chat history
                st.session_state["messages"].append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    main()
