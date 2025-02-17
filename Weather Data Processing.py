import pandas as pd
# Simulate daily weather data with columns for Date, Temperature (°C), Humidity (%), and Precipitation (mm).
date = ['2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31']
temperature = [20, 22, 25, 23, 21, 24, 26, 30, 31, 32]
humidity = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
precipitation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

weather_data = pd.DataFrame({
    'Date': date,
    'Temperature': temperature,
    'Humidity': humidity,
    'Precipitation': precipitation
})

# print(weather_data)

# Add a new column for 'Feels_like' temperature, using a formula
weather_data['Feels_like'] = 0.5 * (weather_data['Temperature'] + weather_data['Humidity'])
# print(weather_data)

# Filter for days with temparatures above 30°C and no precipitation
hot_days = weather_data[(weather_data['Temperature'] > 30) & (weather_data['Precipitation'] == 0)]
hot_days = hot_days.reset_index(drop=True)
hot_days.index += 1
# print(hot_days)

# Delete the 'Precipitation' column and save it to a new dataframe
precipitation_df = weather_data.pop('Precipitation').to_frame()
print(precipitation_df)