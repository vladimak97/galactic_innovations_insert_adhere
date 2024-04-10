# Import the pandas library
import pandas as pd

# Read the Excel file, specifying the sheet names to read
xls = pd.read_excel("/kaggle/input/galactic-innovations-insert-adhere/galactic_innovations_insert_adhere.xlsx", sheet_name=['Galactic Inn Stock Price', 'Books', 'Company'])

# Assign each DataFrame corresponding to each sheet to a variable
sheet1_df = xls['Galactic Inn Stock Price']
sheet2_df = xls['Books']
sheet3_df = xls['Company']

# Print the contents
print(sheet1_df)
print(sheet2_df)
print(sheet3_df)