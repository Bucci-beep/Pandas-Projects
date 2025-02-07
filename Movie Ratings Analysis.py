{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "84ad7654-6ad9-415c-9d3e-9981ea01caa7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f18bd219-95b0-4ad8-bf62-ad8eab3496fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pre define variables for each column\n",
    "\n",
    "movie_names = ['Inception', 'Titanic', 'Avatar']\n",
    "genres = ['Sci-Fi', 'Romance' , 'Sci-Fi']\n",
    "ratings = [8.8, 7.8, 7.9]\n",
    "years = [2010, 1997, 2009]\n",
    "durations = [148, 195, 162] #duration in minutes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "04f5e70c-d0e7-43f7-a84a-cf8c08d73542",
   "metadata": {},
   "outputs": [],
   "source": [
    "#now create a dataframe for each column\n",
    "\n",
    "movies = pd.DataFrame({\n",
    "    'Movie name': movie_names,\n",
    "    'Genre': genres,\n",
    "    'Rating': ratings,\n",
    "    'Year': years,\n",
    "    'Duration': durations\n",
    "}, index=range(1, len(movie_names) + 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6fccf32c-9f04-4924-ae8e-dbd6daa7b88e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Movie name    Genre  Rating  Year  Duration\n",
      "1  Inception   Sci-Fi     8.8  2010       148\n",
      "2    Titanic  Romance     7.8  1997       195\n",
      "3     Avatar   Sci-Fi     7.9  2009       162\n"
     ]
    }
   ],
   "source": [
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "50cd14ea-b6ca-4052-b5ad-3eda78da4690",
   "metadata": {},
   "outputs": [],
   "source": [
    "#step 1: Add a profitability column based on the revenue and budget"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "53646a2f-8cad-43b5-b4c1-f998a2d513df",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies['revenue'] = [829000000, 218700000, 287400000] #add revenue column\n",
    "movies['budget'] = [160000000, 200000000, 237000000] #add budget column\n",
    "\n",
    "# Calculate Profitability using the existing columns in the DataFrame\n",
    "movies['Profitability'] = movies['revenue'] - movies['budget']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "64c713ff-93ab-4f58-a057-dae6ff040e49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Movie name    Genre  Rating  Year  Duration    revenue     budget  \\\n",
      "1  Inception   Sci-Fi     8.8  2010       148  829000000  160000000   \n",
      "2    Titanic  Romance     7.8  1997       195  218700000  200000000   \n",
      "3     Avatar   Sci-Fi     7.9  2009       162  287400000  237000000   \n",
      "\n",
      "   Profitability  \n",
      "1      669000000  \n",
      "2       18700000  \n",
      "3       50400000  \n"
     ]
    }
   ],
   "source": [
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7987ac62-1f04-4977-b893-5e3a1b0887cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#step 2: filter the dataframe to find movie ratings above 8 and durations under 120 minutes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "855b661f-013e-40ac-989c-fc1d6b1b5a59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [Movie name, Genre, Rating, Year, Duration, revenue, budget, Profitability]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "filtered_movies = movies[(movies['Rating'] >8) & (movies['Duration'] < 120)]\n",
    "\n",
    "print(filtered_movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8b27618b-9a80-4f35-8e5f-e91dd4eee5a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#adding data that can be filtered"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "33ecab55-e259-4a75-b961-3d1b5b3cc18c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#creating an new dataframe with new movies that meet the criteria"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4bfc0949-c855-43a0-bfdc-97a5e3f59043",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_movies = pd.DataFrame({\n",
    "    'Movie Name': ['The Short Masterpiece', 'Quick Genius'],\n",
    "    'Genre': ['Drama', 'Comedy'],\n",
    "    'Rating': [8.5, 8.2],\n",
    "    'Year': [2021, 2020],\n",
    "    'Duration': [95,110],\n",
    "    'revenue': [100000000, 850000000],\n",
    "    'budget': [20000000, 15000000]\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e82ef94f-15fe-40ec-b9e0-669b7e94fdee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Movie name    Genre  Rating  Year  Duration    revenue     budget  \\\n",
      "0  Inception   Sci-Fi     8.8  2010       148  829000000  160000000   \n",
      "1    Titanic  Romance     7.8  1997       195  218700000  200000000   \n",
      "2     Avatar   Sci-Fi     7.9  2009       162  287400000  237000000   \n",
      "3        NaN    Drama     8.5  2021        95  100000000   20000000   \n",
      "4        NaN   Comedy     8.2  2020       110  850000000   15000000   \n",
      "\n",
      "   Profitability             Movie Name  \n",
      "0      669000000                    NaN  \n",
      "1       18700000                    NaN  \n",
      "2       50400000                    NaN  \n",
      "3       80000000  The Short Masterpiece  \n",
      "4      835000000           Quick Genius  \n"
     ]
    }
   ],
   "source": [
    "#calculate profitability for the new movies\n",
    "\n",
    "new_movies['Profitability'] = new_movies['revenue'] - new_movies['budget']\n",
    "\n",
    "#append the new movies to the original DataFrame\n",
    "movies = pd.concat([movies, new_movies], ignore_index = True)\n",
    "\n",
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0988203e-a1f6-4c67-a3dd-27bde06ae9a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [Movie name, Genre, Rating, Year, Duration, revenue, budget, Profitability]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "print(filtered_movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7140cc4b-9264-4f85-9e8f-1df7d987c4bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Step 3: Delete the duration (minutes) to duration (hours) column\n",
    "#convert duration from minutes to hours\n",
    "movies['Duration(hours)'] = movies['Duration']/60\n",
    "#drop the original duration(minutes) column\n",
    "movies = movies.drop(columns=['Duration'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0b5f4605-9899-4477-abd4-9737e725906e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Movie name    Genre  Rating  Year    revenue     budget  Profitability  \\\n",
      "0  Inception   Sci-Fi     8.8  2010  829000000  160000000      669000000   \n",
      "1    Titanic  Romance     7.8  1997  218700000  200000000       18700000   \n",
      "2     Avatar   Sci-Fi     7.9  2009  287400000  237000000       50400000   \n",
      "3        NaN    Drama     8.5  2021  100000000   20000000       80000000   \n",
      "4        NaN   Comedy     8.2  2020  850000000   15000000      835000000   \n",
      "\n",
      "              Movie Name  Duration(hours)  \n",
      "0                    NaN         2.466667  \n",
      "1                    NaN         3.250000  \n",
      "2                    NaN         2.700000  \n",
      "3  The Short Masterpiece         1.583333  \n",
      "4           Quick Genius         1.833333  \n"
     ]
    }
   ],
   "source": [
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b03b8f28-e634-4a9f-a63b-b1530147808b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
