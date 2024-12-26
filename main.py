import numpy as np
import matplotlib.pyplot as plt

import os

# Step 1: Check the Directory Contents : Let's first check the contents of the directory to ensure the correct file name and path.

# Define the path to the dataset directory
dataset_dir = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1"

# List all files in the directory
files = os.listdir(dataset_dir)
print("Files in directory:", files)


# Step 1: Update the File Path to Step 2: Load the Correct File
import pandas as pd
import matplotlib.pyplot as plt

# Define the correct path to the dataset file
dataset_path = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1/countries_visa_free_access.csv"



# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Display the first few rows of the DataFrame
print(df.head())

# Get basic information about the dataset
df.info()

# Get summary statistics of the dataset
df.describe()




# Example 1: Bar Chart of Visa-Free Access by Country
import pandas as pd
import matplotlib.pyplot as plt

# Define the correct path to the dataset file
dataset_path = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1/countries_visa_free_access.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Sort the data by Visa-Free Access
df_sorted = df.sort_values(by='Visa-Free Access', ascending=False).head(10)

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(df_sorted['Country'], df_sorted['Visa-Free Access'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Visa-Free Access')
plt.title('Top 10 Countries by Visa-Free Access')
plt.xticks(rotation=45)
plt.show()



# Example 2: Pie Chart of Visa-Free Access Distribution
import pandas as pd
import matplotlib.pyplot as plt

# Define the correct path to the dataset file
dataset_path = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1/countries_visa_free_access.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Group the data by Visa-Free Access and count the number of countries
access_counts = df['Visa-Free Access'].value_counts().head(10)

# Create a pie chart
plt.figure(figsize=(8, 8))
access_counts.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Distribution of Visa-Free Access (Top 10)')
plt.ylabel('')
plt.show()


# Example 3: Scatter Plot of Visa-Free Access by Rank
import pandas as pd
import matplotlib.pyplot as plt

# Define the correct path to the dataset file
dataset_path = "/Users/drahmetacik/.cache/kagglehub/datasets/bhadramohit/visa-free-countries-dataset2024/versions/1/countries_visa_free_access.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Convert Rank to numeric for plotting
df['Rank'] = df['Rank'].str.extract('(\d+)').astype(int)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Rank'], df['Visa-Free Access'], alpha=0.5)
plt.xlabel('Rank')
plt.ylabel('Visa-Free Access')
plt.title('Visa-Free Access by Rank')
plt.show()






# x_data = np.random.rand(50) * 100
# y_data = np.random.rand(50) * 100

# plt.scatter(x_data, y_data, c="blue", alpha=0.5, marker='*', label="scatter point")
# plt.show()

# years =[2006 + i for i in range(18)]
# weights = [0.5, 0.6, 0.8, 1.4, 1.6, 1.8, 2.0, 2.2, 1.0, 1.2, 2.4, 3.0, 3.2, 3.4,  2.6, 2.8,3.6, 3.8]

# plt.plot(years, weights, color='b', marker='o', linestyle='--', linewidth=3, markersize=6)
# plt.show()

# x_pro =["C++", "Java", "Python", "JavaScript", "C#", "PHP"]
# y_pro =[20, 30, 25, 10, 15, 10]

# plt.bar(x_pro, y_pro, color='b', alpha=0.5)
# plt.show() 


# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("bhadramohit/visa-free-countries-dataset2024")

# print("Path to dataset files:", path)

# more examples
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


