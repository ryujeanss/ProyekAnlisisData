import streamlit as st
import pandas as pd
import plotly.express as px
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Load data
df_day = pd.read_csv("D:/Submission/data/day.csv")
df_hour = pd.read_csv("D:/Submission/data/hour.csv")

# Title of the Streamlit app
st.title("Bike Rental Data Analysis Dashboard")

# Display the first few rows of the loaded dataframes
st.subheader("Preview of DataFrame day:")
st.dataframe(df_day.head())

st.subheader("Preview of DataFrame hour:")
st.dataframe(df_hour.head())

# Check for non-numeric columns in DataFrame day
non_numeric_cols_day = df_day.select_dtypes(exclude=['number']).columns
st.write("Non-numeric columns in DataFrame day:", non_numeric_cols_day)

# Visualize the correlation matrix only for numeric columns
st.subheader("Correlation Matrix for DataFrame day:")
correlation_matrix_day = df_day.select_dtypes(include=['number']).corr()
fig_day = px.imshow(correlation_matrix_day)
st.plotly_chart(fig_day)

# Visualize a scatter plot between temperature and total rentals
st.subheader("Scatter Plot for DataFrame day - Temperature vs. Total Rentals:")
scatter_plot_temperature = px.scatter(df_day, x='temp', y='cnt', title='Temperature vs. Total Rentals')
st.plotly_chart(scatter_plot_temperature)

# Box plot to analyze the relationship between season and rental count
st.subheader("Box Plot for DataFrame day - Relationship between Season and Rental Count:")
box_plot_season = px.box(df_day, x='season', y='cnt', title='Relationship between Season and Rental Count')
st.plotly_chart(box_plot_season)

# Box plot to analyze the relationship between weather and rental count
st.subheader("Box Plot for DataFrame day - Relationship between Weather and Rental Count:")
box_plot_weather = px.box(df_day, x='weathersit', y='cnt', title='Relationship between Weather and Rental Count')
st.plotly_chart(box_plot_weather)