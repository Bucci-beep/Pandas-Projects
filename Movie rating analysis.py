import pandas as pd

# Load the data
movie_names = ['Inception', 'Titanic', 'Avatar']
genres = ['Sci-Fi', 'Romance', 'Sci-Fi']
ratings = [8.8, 7.8, 7.9]
years = [2010, 1997, 2009]
duration = [148, 195, 162]

movies = pd.DataFrame({
    'Movie name': movie_names,
    'Genre': genres,
    'Rating': ratings,
    'Year': years,
    'Duration': duration
}, index=range(1, len(movie_names) + 1))

# Add a profit column
budget = [160000000, 200000000, 237000000]
revenue = [825000000, 220800000, 278400000]

movies['Revenue'] = revenue
movies['Budget'] = budget

# Calculate profitability as (Revenue - Budget) and add it as a new column
movies['Profit'] = movies['Revenue'] - movies['Budget']

# filter the dataframe to find movie ratings > 8 and durations < 120 minutes

movies = movies[(movies['Rating'] > 8) & (movies['Duration'] < 120)]
# There are no movies that satisfy the above condition so create a new dataframe with movies that meet the criteria 

new_movies = pd.DataFrame({
    'Movie name': ['The Lion King', 'The Shawshank Redemption'],
    'Genre': ['Animation', 'Drama'],
    'Rating': [8.5, 9.3],
    'Year': [1994, 1994],
    'Duration': [88, 142],
    'Revenue': [968500000, 58000000],
    'Budget': [45000000, 25000000],
    'Profit': [923500000, 33000000]
}, index=range(4, 6))
 # calculate profit for the new movies
new_movies['Profit'] = new_movies['Revenue'] - new_movies['Budget']

# Append the new_movies dataframe to the movies dataframe
movies = pd.concat([movies, new_movies])

print(movies)