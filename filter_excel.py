
import pandas as pd

# Load Excel file
df = pd.read_excel('input.xlsx')

# Example filter: Keep rows where 'Amount' > 1000
filtered_df = df[df['Amount'] > 1000]

# Write to new Excel file
filtered_df.to_excel('output.xlsx', index=False)

print("Filtered file created: output.xlsx")
