import pandas as pd

# Create a dataframe with columns 'Car Model', 'Mileage', 'Condition','Price' and 'Year'
# Load the data

car_model = ['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes', 'Audi', 'Chevrolet']
mileage = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
condition = ['New', 'Used', 'Used', 'New', 'Used', 'New', 'Used']
price = [30000, 25000, 20000, 40000, 35000, 45000, 15000]
year = [2019, 2018, 2017, 2016, 2015, 2014, 2013]

car_sales = pd.DataFrame({
    'Car Model': car_model,
    'Mileage': mileage,
    'Condition': condition,
    'Price': price,
    'Year': year
})

# Reset the index of the dataframe to start from 1
car_sales.index += 1

print(car_sales)