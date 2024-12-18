import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the dataset
dataset_path = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1/countries_visa_free_access.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Display the first few rows of the DataFrame
print(df.head())

# Example visualization: Bar chart of Visa-Free Access by Country
df_sorted = df.sort_values(by='Visa-Free Access', ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.bar(df_sorted['Country'], df_sorted['Visa-Free Access'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Visa-Free Access')
plt.title('Top 10 Countries by Visa-Free Access')
plt.xticks(rotation=45)
plt.show()

# Example 1: Pie chart of Visa-Free Access distribution
plt.figure(figsize=(8, 8))
df['Visa-Free Access'].value_counts().head(10).plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Distribution of Visa-Free Access (Top 10)')
plt.ylabel('')
plt.show()

# Example 2: Scatter plot of Visa-Free Access by Rank
df['Rank'] = df['Rank'].str.extract('(\d+)').astype(int)
plt.figure(figsize=(10, 6))
plt.scatter(df['Rank'], df['Visa-Free Access'], alpha=0.5)
plt.xlabel('Rank')
plt.ylabel('Visa-Free Access')
plt.title('Visa-Free Access by Rank')
plt.show()

# Example 3: Histogram of Visa-Free Access
plt.figure(figsize=(10, 6))
plt.hist(df['Visa-Free Access'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Visa-Free Access')
plt.ylabel('Frequency')
plt.title('Histogram of Visa-Free Access')
plt.show()

# Example 4: Box plot of Visa-Free Access
plt.figure(figsize=(10, 6))
plt.boxplot(df['Visa-Free Access'], vert=True, patch_artist=True)
plt.xlabel('Visa-Free Access')
plt.title('Box Plot of Visa-Free Access')
plt.show()

# Example 5: Line plot of Visa-Free Access by Rank
df_sorted_by_rank = df.sort_values(by='Rank')
plt.figure(figsize=(10, 6))
plt.plot(df_sorted_by_rank['Rank'], df_sorted_by_rank['Visa-Free Access'], marker='o', linestyle='-', color='green')
plt.xlabel('Rank')
plt.ylabel('Visa-Free Access')
plt.title('Line Plot of Visa-Free Access by Rank')
plt.show()