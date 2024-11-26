import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the dataset
dataset_path = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1/visa_free_countries.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Display the first few rows of the DataFrame
df.head()

# Get basic information about the dataset
df.info()

# Get summary statistics of the dataset
df.describe()

# Group the data by region and count the number of visa-free countries
region_counts = df['Region'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
region_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Region')
plt.ylabel('Number of Visa-Free Countries')
plt.title('Number of Visa-Free Countries by Region')
plt.xticks(rotation=45)
plt.show()

# Create a pie chart
plt.figure(figsize=(8, 8))
region_counts.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Visa-Free Countries by Region')
plt.ylabel('')
plt.show()

# Assuming the dataset has columns 'GDP' and 'Population'
plt.figure(figsize=(10, 6))
plt.scatter(df['GDP'], df['Population'], alpha=0.5)
plt.xlabel('GDP')
plt.ylabel('Population')
plt.title('Visa-Free Countries by GDP and Population')
plt.show()

