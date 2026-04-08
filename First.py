import streamlit as st

st.text('some random text')


"""
EDA Workshop Script
Author: Converted from Jupyter Notebook
"""

# =========================
# Imports
# =========================
import pandas as pd

# Optional libraries (install before running):
# pip install ydata-profiling sweetviz
from ydata_profiling import ProfileReport
import sweetviz as sv


# =========================
# Load Dataset
# =========================
# Make sure the CSV file is in the same directory
df = pd.read_csv("DAtaSet.csv")


# =========================
# Basic Exploration
# =========================
print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.describe())

print("\n--- Last 5 Rows ---")
print(df.tail())
print("\n--- Missing Values ---")
print(df.isnull().sum())


# =========================
# YData Profiling Report
# =========================
profile = ProfileReport(df, title="EDA Report", explorative=True)

# Save report to HTML file
profile.to_file("eda_report.html")

# =========================
# Sweetviz Report
# =========================
report = sv.analyze(df)

# Save report to HTML file
report.show_html("sweetviz_report.html")


