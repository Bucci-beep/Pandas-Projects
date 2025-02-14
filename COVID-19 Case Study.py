import pandas as pd

#create a dataframe with mock COVID-19 data(date, new cases, total cases, recovered and country)
# Load the data

date = ['2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31']
new_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_cases = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
recovered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
country = ['China', 'America', 'Italy', 'Brazil', 'Argentina', 'France', 'USA', 'Portugal', 'South Africa', 'Germany']

case_study = pd.DataFrame({
    'Date': date,
    'New_cases': new_cases,
    'Total_cases': total_cases,
    'Recovered': recovered,
    'Country': country
})

print(case_study)

# Create a new column 'Active' which is the difference between 'Total_cases' and 'Recovered'
case_study['Active'] = case_study['Total_cases'] - case_study['Recovered']

# Filter for countries with more than 15 active cases
active_cases = case_study[case_study['Active'] > 15]
active_cases = active_cases.reset_index(drop=True)
active_cases.index += 1
print(active_cases)

# Delete the 'Recovered' column and save it to a new dataframe
recovered_df = case_study.pop('Recovered').to_frame()
print(recovered_df)