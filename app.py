from dotenv import load_dotenv 
import os 
import google.generativeai as genai 
import streamlit as st

# Load environment variables
load_dotenv()  # Load all env vars, including GOOGLE_API_KEY

# Configure the Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide query responses
def get_gemini_response(question, prompt): 
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question]) 
    return response.text.strip()  # Ensure no extra spaces/newlines

# Define the prompt for the AI model
prompt = [
    """You are an expert in converting English questions to SQL queries. The user will input a query in natural language. Your task is to convert that natural language query into a valid SQL query. Remember these points:
    1. If the user has not given sufficient information in the query, respond with "Please enter a more detailed query."
    2. Else, generate the corresponding SQL query
    3. No preamble
    4. The SQL code should not include ``` or the word 'sql' in the output.
    
    Example 1- "How many entries of records are present in the student table?" 
    The SQL command will be: select count(*) from STUDENT; 
    
    Example 2- "Tell me all the students studying in Data Science class?" 
    The SQL command will be: select * from STUDENT where Class="Data Science";

    Example 2- "How many students are there?" 
    In this example we don't have enough information, so the response can be "Please enter a more detailed query."

    """
]

# Streamlit App
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App To Retrieve Any SQL Data")
st.markdown("""
- ##### This tool allows users to ask natural language questions, and the system will generate and execute the corresponding SQL query.  
- ##### The goal is to make it easier for non-technical users to interact with databases without needing to know SQL.
""")
# Input from the user
question = st.text_input("Input: ", key="input")
submit = st.button("Generate SQL Query")

# If the submit button is clicked
if submit: 
    if question:  # Ensure the user input is not empty
        # Get the SQL query from the AI model
        response = get_gemini_response(question, prompt)
        if not response or response=="Please enter a more detailed query.":
            st.warning("Insufficient info. Please enter a more detailed query.")
        else:
            st.success(response)
    else:
        st.warning("Please enter a question to retrieve data.")
