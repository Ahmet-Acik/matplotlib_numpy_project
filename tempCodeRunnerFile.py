# Example 6: Heatmap of Visa-Free Access by Region (assuming 'Region' column exists)
if 'Region' in df.columns:
    region_access = df.groupby('Region')['Visa-Free Access'].mean().reset_index()
    region_access_pivot = region_access.pivot(index='Region', columns='Visa-Free Access', values='Visa-Free Access')
    plt.figure(figsize=(12, 8))
    sns.heatmap(region_access_pivot, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Heatmap of Visa-Free Access by Region')
    plt.show()