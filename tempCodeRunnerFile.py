# Example 7: Stacked bar chart of Visa-Free Access by Region
if 'Region' in df.columns:
    region_access = df.groupby('Region')['Visa-Free Access'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    plt.bar(region_access['Region'], region_access['Visa-Free Access'], color='skyblue')
    plt.xlabel('Region')
    plt.ylabel('Visa-Free Access')
    plt.title('Visa-Free Access by Region')
    plt.xticks(rotation=45)
    plt.show()