{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "366b721a-1049-4b27-8def-d84594da1460",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Team name Wins Losses Draws Points\n",
      "1     United   20      0     0     60\n",
      "2    Chelsea   17      1     2     51\n",
      "3    Arsenal    9      2     1     27\n",
      "4  Liverpool    8      3     3     24\n"
     ]
    }
   ],
   "source": [
    "#Task: Create a DataFrame for a football league with columns for Team Name, Wins, Losses, Draws, and Points.\n",
    "\n",
    "import pandas as pd\n",
    "team_names = ['United', 'Chelsea', 'Arsenal', 'Liverpool']\n",
    "wins = ['20', '17', '9', '8']\n",
    "losses = ['0', '1', '2', '3']\n",
    "draws = ['0', '2', '1', '3']\n",
    "points = ['60', '51', '27', '24']\n",
    "\n",
    "football_league =pd.DataFrame({\n",
    "    'Team name': team_names,\n",
    "    'Wins': wins,\n",
    "    'Losses': losses,\n",
    "    'Draws': draws,\n",
    "    'Points': points\n",
    "}, index = range(1, len(team_names) +1))\n",
    "\n",
    "print(football_league)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5f14914a-088c-4570-a814-8183ef4ec145",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Team name Wins Losses Draws Points Goal Difference\n",
      "1     United   20      0     0     60              35\n",
      "2    Chelsea   17      1     2     51              20\n",
      "3    Arsenal    9      2     1     27               5\n",
      "4  Liverpool    8      3     3     24             -10\n"
     ]
    }
   ],
   "source": [
    "#Add a column Goal Difference based on mock data.\n",
    "\n",
    "# Create a list with mock data for Goal Difference\n",
    "goal_difference = ['35', '20', '5', '-10']\n",
    "\n",
    "# Add the new column to the DataFrame\n",
    "football_league['Goal Difference'] = goal_difference\n",
    "\n",
    "print(football_league)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "413947a6-3158-4169-9099-53dee04262b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Team name Wins Losses Draws  Points  Goal Difference\n",
      "1    United   20      0     0      60               35\n",
      "2   Chelsea   17      1     2      51               20\n"
     ]
    }
   ],
   "source": [
    "#filter teams with more than 30 points and a positive goal difference\n",
    "#convert the points and goal difference columns to numeric types first in order to avoid the TypeError\n",
    "\n",
    "football_league['Points'] = pd.to_numeric(football_league['Points'])\n",
    "football_league['Goal Difference'] = pd.to_numeric(football_league['Goal Difference'])\n",
    "\n",
    "#filter teams with more than 30 points and a positive goal difference\n",
    "filtered_teams = football_league[\n",
    "(football_league['Points'] > 30) & \n",
    "(football_league['Goal Difference'] > 0)\n",
    "]\n",
    "\n",
    "print(filtered_teams)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c794e617-580f-409f-8081-178efd690260",
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
