# Text to SQL using Gemini 2.0 Flash

This project is a Streamlit web application that converts natural language questions into SQL queries. It leverages the power of Google's Gemini 2.0 Flash model to understand the user's intent and generate the corresponding SQL code.

## Features

-   **Natural Language to SQL:** Ask questions in plain English and get the SQL query equivalent.
-   **User-Friendly Interface:** A simple and intuitive web interface built with Streamlit.
-   **Powered by Gemini 2.0 Flash:** Utilizes one of Google's state-of-the-art language models for accurate conversions.

## Tech Stack

-   **Python:** The core programming language.
-   **Streamlit:** For creating the web application interface.
-   **Google Gemini 2.0 Flash:** The language model used for the conversion.
-   **Dotenv:** To manage environment variables.

## Getting Started

### Prerequisites

-   Python 3.7+
-   An API key from Google AI Studio.

### Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/your-username/Project--Text-to-SQL.git
    cd Project--Text-to-SQL
    ```
2.  **Create a virtual environment:**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```
4.  **Set up your environment variables:**
    -   Create a file named `.env` in the root of the project.
    -   Add your Google API key to the `.env` file as follows:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY"
        ```

### Running the Application

1.  **Start the Streamlit server:**
    ```
    streamlit run app.py
    ```
2.  Open your browser and navigate to the URL provided by Streamlit
