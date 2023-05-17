import pandas as pd

# Read the three CSV files
file1 = pd.read_csv(r'C:\Users\Divin\PycharmProjects\quantium-starter-repo\data\daily_sales_data_0.csv')
print(file1)
file2 = pd.read_csv(r'C:\Users\Divin\PycharmProjects\quantium-starter-repo\data\daily_sales_data_1.csv')
file3 = pd.read_csv(r'C:\Users\Divin\PycharmProjects\quantium-starter-repo\data\daily_sales_data_2.csv')

# Filter rows to keep only Pink Morsels
file1 = file1[file1['product'] == 'pink morsels']
file2 = file2[file2['product'] == 'pink morsels']
file3 = file3[file3['product'] == 'pink morsels']

# Combine quantity and price into a single sales column
file1['sales'] = file1['quantity'] * file1['price']
file2['sales'] = file2['quantity'] * file2['price']
file3['sales'] = file3['quantity'] * file3['price']

# Select the desired fields: sales, date, and region
file1 = file1[['sales', 'date', 'region']]
file2 = file2[['sales', 'date', 'region']]
file3 = file3[['sales', 'date', 'region']]

# Concatenate the three files into a single DataFrame
combined_data = pd.concat([file1, file2, file3])

# Write the combined data to a new CSV file
combined_data.to_csv('output.csv', index=False)
