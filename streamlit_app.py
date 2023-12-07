import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.sidebar.write("Installing required dependencies...")
st.sidebar.code("!pip install psycopg2-binary")
import psycopg2  
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def get_data(query):
    with conn.cursor() as cur:
        cur.execute(query)
        data = cur.fetchall()
        # Convert the query results to a pandas DataFrame
        df = pd.DataFrame(data, columns=[desc[0] for desc in cur.description])
        return df
# Use Streamlit to display the retrieved data
st.header("Retail Database")
st.write("Enter a query to retrieve data from the database:")

query = st.text_input("Query:")
if query:
    df = get_data(query)
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No data found.")
# Retrieve all table names from the database
with conn.cursor() as cur:
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    table_names = [name[0] for name in cur.fetchall()]

# Display a dropdown menu with the table names
table_name = st.selectbox("Select the table Name:", table_names)

# If a table has been selected, display the data in a dataframe
if table_name:
    st.write(f"Displaying data from table: {table_name}")
    query = f"SELECT * FROM {table_name}"
    df = get_data(query)
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No data found.")
