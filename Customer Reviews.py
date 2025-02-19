import pandas as pd
# Task 1: Create a dataset with customer reviews(date, product, review, text, rating)
dates = pd.date_range(start='2025-02-01', periods=5, freq='D')
products = ['Product A', 'Product B', 'Product A', 'Product C', 'Product B']
reviews = ['Review 1', 'Review 2', 'Review 3', 'Review 4', 'Review 5']
texts = ['Great product!', 'Not satisfied.', 'Highly recommended.', 'Average quality.', 'Excellent service.']
ratings = [5, 2, 4, 3, 5]

customer_reviews = pd.DataFrame({
    'Date': dates,
    'Product': products,
    'Review': reviews,
    'Text': texts,
    'Rating': ratings
}, index=range(1, len(dates) + 1))

print("\nCustomer Reviews:")
print(customer_reviews)

# Task 2: Use Pandas to clean text data, convert ratings to numeric values, and filter out low-rating entries
customer_reviews['Rating'] = pd.to_numeric(customer_reviews['Rating'])
filtered_reviews = customer_reviews[customer_reviews['Rating'] >= 4]
print("\nFiltered Customer Reviews:")
print(filtered_reviews)

# Task 3: Group by product and compute average sentiment scores; merge with product info for enriched analysis
avg_sentiment = filtered_reviews.groupby('Product', as_index=False)['Rating'].mean()
avg_sentiment.rename(columns={'Rating': 'Avg Rating'}, inplace=True)
print("\nAverage Sentiment Scores by Product:")
print(avg_sentiment)

# Task 4: Create a product information dataframe for enriched analysis
product_info = pd.DataFrame({
    'Product': ['Product A', 'Product B', 'Product C'],
    'Category': ['Electronics', 'Apparel', 'Home Goods'],
    'Price': [100, 50, 75]
},index=range(1, len(['Product A', 'Product B', 'Product C']) + 1))
print("\nProduct Information:")
print(product_info)

# Task 5: Merge average sentiment scores with product information for enriched analysis
enriched_analysis = pd.merge(avg_sentiment, product_info, on='Product', how='left')
enriched_analysis.index = range(1, len(enriched_analysis) + 1)
print("\nEnriched Analysis:")
print(enriched_analysis)