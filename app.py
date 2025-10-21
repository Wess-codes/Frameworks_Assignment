import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load data
df = pd.read_csv('metadata.csv', low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Year range slider
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered_df = df[df['year'].between(year_range[0], year_range[1])]

# Show sample data
st.write("Sample Data", filtered_df[['title', 'journal', 'publish_time']].head())

# Publications by year
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title('Publications by Year')
st.pyplot(fig)
