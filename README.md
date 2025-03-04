
# 📊 AI-Powered CSV Chatbot

Welcome to the AI-Powered CSV Chatbot! This innovative tool seamlessly integrates advanced AI capabilities to analyze and extract insights from your CSV files in no time. Simply upload your CSV data and start interacting with the AI to get detailed analytical insights and answers to your data-related questions.

## Project Overview

The AI-Powered CSV Chatbot is designed for data analysts, researchers, and anyone who regularly works with CSV files. It brings the power of AI to your fingertips, making data analysis more intuitive and interactive. This project aims to enhance data comprehension by offering AI-generated insights and providing a conversational interface to engage with your data more deeply.

## Key Features

- **Streamlined CSV Upload**: Easily upload CSV files directly through the user-friendly interface.
- **AI-Generated Insights**: Leverage GPT-4o to gain quick and comprehensive summaries of your dataset.
- **Interactive Chat Interface**: Engage in real-time conversations with the AI to explore your dataset and ask follow-up questions.
- **Data Persistence**: Maintain chat history and insights throughout your session for a seamless experience.
- **Secure API Configuration**: Enter API keys securely in the sidebar ensuring your credentials remain confidential.

## Installation & Setup Guide

To set up the AI-Powered CSV Chatbot locally, follow these steps:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/ai-powered-csv-chatbot.git
   cd ai-powered-csv-chatbot
   ```

2. **Set Up a Virtual Environment**:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:  
   Ensure you have `pip` installed, then run:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your OpenAI API Key**:  
   Open the Streamlit sidebar to securely input your OpenAI API key, which is essential for the GPT-4o integration.

## Usage Instructions

After setting up the project, you can start the Streamlit application by running the following command:

```bash
streamlit run app.py
```

### Walkthrough of Major Functionalities

- **Upload CSV**: Once the application is running, upload a CSV file via the main interface.
- **View Data Preview**: See the top rows of your dataset displayed on the app.
- **Gain AI Insights**: Observe real-time AI-generated insights presented in a concise format.
- **Interact with AI**: Use the chat interface to ask questions about your dataset for in-depth analysis.

## Technology Stack

- **Programming Language**: Python
- **Web Framework**: Streamlit
- **AI/ML API**: OpenAI GPT-4o
- **Data Handling**: Pandas

## Additional Notes

- **Limitations**: The application requires a valid OpenAI API key, and API call limits depend on your plan with OpenAI.
- **Future Improvements**: Potential enhancements include support for additional data formats and more comprehensive insight retrieval mechanisms.

For additional support or inquiries, please refer to the project documentation or contact the developer team.

Enjoy data analysis like never before with the AI-Powered CSV Chatbot!
```
