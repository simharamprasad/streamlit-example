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

pip install streamlit psycopg2
import streamlit as st
import psycopg2

# Function to run SQL queries
def run_query(query):
    connection = psycopg2.connect(
        host='localhost',
        port='5433',
        database='postgres',
        user='postgres',
        password='SVR-2000'
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

# Streamlit App
def main():
    st.title("SQL Query Runner")

    # Input SQL query
    user_query = st.text_area("Enter your SQL query:", height=200)

    # Execute query on button click
    if st.button("Run Query"):
        if user_query:
            result = run_query(user_query)

            # Display results
            if result:
                st.success("Query executed successfully!")
                st.table(result)
            else:
                st.warning("No results to display.")
        else:
            st.warning("Please enter a SQL query.")

if __name__ == "__main__":
    main()
