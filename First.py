import streamlit as st

st.text('some random text')


"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""

st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("📊 Data Analysis Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.write(df)

    # Basic info
    st.subheader("Dataset Info")
    st.write(df.describe())

    # Column selection
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    if len(numeric_cols) > 0:
        col1 = st.selectbox("Select X-axis", numeric_cols)
        col2 = st.selectbox("Select Y-axis", numeric_cols)

        # Scatter plot
        st.subheader("Scatter Plot")
        fig, ax = plt.subplots()
        ax.scatter(df[col1], df[col2])
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        st.pyplot(fig)

        # Heatmap
        st.subheader("Correlation Heatmap")
        fig2, ax2 = plt.subplots()
        sns.heatmap(df.corr(), annot=True, ax=ax2)
        st.pyplot(fig2)

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write(df)
else:
    st.info("Please upload a CSV file to continue.")

    
