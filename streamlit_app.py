import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import psycopg2

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
# Streamlit App Title
st.title("PostgreSQL Query App")

# Function to establish a database connection
@st.cache(allow_output_mutation=True)
def init_connection():
    return psycopg2.connect(
        host="your_database_host",
        user="your_database_user",
        password="your_database_password",
        database="your_database_name",
    )

# Function to execute a query and return results as a DataFrame
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=columns)
        return df

# Connect to the database
conn = init_connection()

# Display a text input for the user to enter a SQL query
query = st.text_area("Enter your SQL query here:")

# Check if a query is provided
if query:
    # Execute the query and display the results
    st.write("Query Results:")
    try:
        result_df = run_query(query)
        st.dataframe(result_df)
    except Exception as e:
        st.error(f"Error executing the query: {str(e)}")

# Display a list of tables in the database
st.header("Tables in the Database")
with conn.cursor() as cur:
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    table_names = [name[0] for name in cur.fetchall()]

selected_table = st.selectbox("Select a table:", table_names)

# Display the table content if a table is selected
if selected_table:
    st.write(f"Displaying data from table: {selected_table}")
    table_query = f"SELECT * FROM {selected_table} LIMIT 10;"
    try:
        table_df = run_query(table_query)
        st.dataframe(table_df)
    except Exception as e:
        st.error(f"Error retrieving data from the table: {str(e)}")
