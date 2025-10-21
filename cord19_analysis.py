import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('metadata.csv', low_memory=False)

# Basic exploration
print("Shape:", df.shape)
print(df.info())
print("Missing values:\n", df.isnull().sum())

# Data cleaning
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))
df_clean = df.dropna(subset=['title', 'publish_time'])

# Publications by year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.tight_layout()
plt.savefig('publications_by_year.png')
plt.close()

# Top journals
top_journals = df_clean['journal'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title('Top Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.tight_layout()
plt.savefig('top_journals.png')
plt.close()
