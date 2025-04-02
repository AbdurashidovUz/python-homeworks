'''import sqlite3
import pandas as pd


conn = sqlite3.connect('chinook.db')


query = """
SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) as TotalInvoices
FROM customers
INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
GROUP BY customers.CustomerId
"""
result = pd.read_sql_query(query, conn)
print(result) '''

import pandas as pd


movie_df = pd.read_csv('movie.csv')

df1 = movie_df[['director_name', 'color']]
df2 = movie_df[['director_name', 'num_critic_for_reviews']]

left_join_df = pd.merge(df1, df2, on='director_name', how='left')
print(f"Left Join Result: {left_join_df.shape[0]} rows")

outer_join_df = pd.merge(df1, df2, on='director_name', how='outer')
print(f"Full Outer Join Result: {outer_join_df.shape[0]} rows")