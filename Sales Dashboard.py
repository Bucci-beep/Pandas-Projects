import pandas as pd
# Create a sample sales data set
data = {
    'Date' : pd.date_range(start= '2025-02-01', periods=4, freq='D'),
    'Product': ['Desktop Computer','Tablet','iPhone','Laptop'],
    'Quantity': [100,200,50,70],
    'Revenue': [70000,50000,40000,84000]
}

sales = pd.DataFrame(data)
print("\nSample Sales Data:")
print(sales)

# Sort the data by Date
sales = sales.sort_values('Date')
print("\nSorted Sales Data:")
print(sales)

# Calculate cumulative revenue
sales['Cumulative Revenue'] = sales['Revenue'].cumsum()
print("\nSales Data with Cumulative Revenue:")
print(sales)

#setting the index to 'Product'
sales_indexed =sales.set_index('Product')
print("\nDataframe Indexed by Product")
print(sales_indexed)
