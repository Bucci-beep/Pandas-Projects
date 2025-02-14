import pandas as pd

# 1. Create a DataFrame
dates = ['2025-01-01', '2025-01-05', '2025-01-07', '2025-01-10']
categories = ['groceries', 'entertainment', 'bills', 'groceries']
amounts = [50, 100, 60, 40]
notes = ['bought produce', 'movie night', 'electricity bill', 'milk and bread']

monthly_expenses = pd.DataFrame({
    'Date': dates,
    'Category': categories,
    'Amount': amounts,
    'Notes': notes
})

print("Initial DataFrame:\n", monthly_expenses, "\n")

# 2. Add a "Cumulative Amount" column
monthly_expenses['Amount'] = pd.to_numeric(monthly_expenses['Amount'])
monthly_expenses['Cumulative Amount'] = monthly_expenses['Amount'].cumsum()

print("After adding 'Cumulative Amount':\n", monthly_expenses, "\n")

# 3. Index by Category & calculate total
monthly_expenses.set_index('Category', inplace=True)
total_by_category = monthly_expenses.groupby(level=0)['Amount'].sum()

print("DataFrame indexed by Category:\n", monthly_expenses, "\n")
print("Total amount for each category:\n", total_by_category, "\n")

# 4. Filter out non-essential categories
essential_categories = ['groceries', 'bills']
monthly_expenses = monthly_expenses[monthly_expenses.index.isin(essential_categories)]

print("After filtering non-essential categories:\n", monthly_expenses, "\n")

# 5. Delete the Notes column
monthly_expenses.drop(columns=['Notes'], inplace=True)

print("Final DataFrame after dropping 'Notes' column:\n", monthly_expenses)

# Display final results
print("Filtered & Updated DataFrame:\n", monthly_expenses, "\n")
print("Total by Category:\n", total_by_category)
