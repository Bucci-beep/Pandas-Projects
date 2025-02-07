{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9eae215b-1118-42bc-8063-9dc8c69752ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Product name   Category Price Stock Rating\n",
      "1        Sugar    Grocery   120    50    4.5\n",
      "2       Coffee    Cutlery   200   100    4.0\n",
      "3         Milk  Beverages    60   200    4.1\n",
      "4         Salt     Grains    90   300    3.4\n"
     ]
    }
   ],
   "source": [
    "# Task: Create a DataFrame for a store with columns like Product Name, Category, Price, Stock, and Rating.\n",
    "import pandas as pd\n",
    "\n",
    "product_name = ['Sugar', 'Coffee', 'Milk', 'Salt']\n",
    "category = ['Grocery', 'Cutlery', 'Beverages', 'Grains']\n",
    "price = ['120', '200', '60', '90']\n",
    "stock = ['50', '100', '200', '300']\n",
    "rating = ['4.5', '4.0', '4.1', '3.4']\n",
    "\n",
    "store = pd.DataFrame({\n",
    "    'Product name': product_name,\n",
    "    'Category': category,\n",
    "    'Price': price,\n",
    "    'Stock': stock,\n",
    "    'Rating': rating\n",
    "}, index = range(1, len(product_name) +1))\n",
    "\n",
    "print(store)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "96ff3779-974f-44ee-9342-d9b3f244e707",
   "metadata": {},
   "outputs": [],
   "source": [
    "# task 2, deleting the stock column and replacng it with units sold"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8cf71f08-ef3a-4e38-a511-8ea64d8bfe38",
   "metadata": {},
   "outputs": [],
   "source": [
    "store.drop(columns =['Stock'], inplace = True)\n",
    "\n",
    "#adding the 'units sold' column\n",
    "units_sold = [20,30,40,50]\n",
    "store['Units Sold'] = units_sold"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9c7a2760-549d-46e0-8a05-18dd572191a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Product name   Category Price Rating  Units Sold\n",
      "1        Sugar    Grocery   120    4.5          20\n",
      "2       Coffee    Cutlery   200    4.0          30\n",
      "3         Milk  Beverages    60    4.1          40\n",
      "4         Salt     Grains    90    3.4          50\n"
     ]
    }
   ],
   "source": [
    "print(store)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3d5ad881-6629-4b74-a996-a4ab40958259",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Product name  Price Rating\n",
      "Category                            \n",
      "Beverages         Milk     60    4.1\n",
      "Grains            Salt     90    3.4\n",
      "Grocery          Sugar    120    4.5\n",
      "Cutlery         Coffee    200    4.0\n"
     ]
    }
   ],
   "source": [
    "#task 3, index the products by category and sort by price\n",
    "\n",
    "#convert the price to a numeric type(from strings to integers) so as to sort numerically\n",
    "#use set_index() to make category the index of the dataframe \n",
    "#use sort_values() to sort the dataframe based on price column\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "product_name = ['Sugar', 'Coffee', 'Milk', 'Salt']\n",
    "category = ['Grocery', 'Cutlery', 'Beverages', 'Grains']\n",
    "price = ['120', '200', '60', '90']\n",
    "rating = ['4.5', '4.0', '4.1', '3.4']\n",
    "\n",
    "store = pd.DataFrame({\n",
    "    'Product name': product_name,\n",
    "    'Category': category,\n",
    "    'Price': price,\n",
    "    'Rating': rating\n",
    "}, index=range(1, len(product_name) + 1))\n",
    "\n",
    "#convert the price to a numeric type(from strings to integers) so as to sort numerically\n",
    "store['Price'] = pd.to_numeric(store['Price'])\n",
    "\n",
    "#use set_index() to make category the index of the dataframe \n",
    "store.set_index('Category', inplace=True)\n",
    "\n",
    "#use sort_values() to sort the dataframe based on price column\n",
    "store_sorted = store.sort_values(by='Price')\n",
    "\n",
    "print(store_sorted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07caa6d2-a762-457f-907e-301dafc312a0",
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
