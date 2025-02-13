{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c0f2a724-0d5b-4fd2-ac2b-067548f649c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Date       Category Amount       Note\n",
      "1  15/01/25        grocery   5000        adg\n",
      "2  16/01/25          bills  13000      djfjg\n",
      "3  17/01/25  entertainment  10000  hgjngngng\n"
     ]
    }
   ],
   "source": [
    "# Task: Create a DataFrame for monthly expenses with columns for Date, Category, Amount, and Notes.\n",
    "\n",
    "import pandas as pd\n",
    "dates = ['15/01/25', '16/01/25', '17/01/25']\n",
    "category = ['grocery', 'bills', 'entertainment']\n",
    "amount = ['5000', '13000', '10000']\n",
    "notes = ['adg', 'djfjg', 'hgjngngng']\n",
    "\n",
    "monthly_expenses = pd.DataFrame({\n",
    "    'Date': dates,\n",
    "    'Category': category,\n",
    "    'Amount': amount,\n",
    "    'Note': notes\n",
    "}, index = range(1, len(monthly_expenses)+1))\n",
    "\n",
    "print(monthly_expenses)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b3ec0430-6f97-463e-aad2-322c7d9927ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Category\n",
      "bills            13000\n",
      "entertainment    10000\n",
      "grocery           5000\n",
      "Name: Amount, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Task 2: Index the DataFrame by category and calculate the total amount for each category.\n",
    "#conver the amount column to numeric(pd.to_numeric()) function.\n",
    "monthly_expenses['Amount'] = pd.to_numeric(monthly_expenses['Amount'])\n",
    "# index the data frame by category\n",
    "monthly_expenses.set_index('Category', inplace=True)\n",
    "# calculate the total amount for each category\n",
    "total_by_category = monthly_expenses.groupby(level=0)['Amount'].sum()\n",
    "\n",
    "print(total_by_category)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bb30183-98c8-47b5-9081-d72a895ced9b",
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
