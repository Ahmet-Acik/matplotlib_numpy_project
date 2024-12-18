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