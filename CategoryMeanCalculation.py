import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}
df = pd.DataFrame(data)

grouped_df = df.groupby('Category').mean().reset_index()
print("Grouped DataFrame:")
print(grouped_df)