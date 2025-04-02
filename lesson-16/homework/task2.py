import pandas as pd


titanic_df = pd.read_excel('titanic.xlsx')


age_above_30_df = titanic_df[titanic_df['Age'] > 30]
print(age_above_30_df.head())


gender_counts = titanic_df['Sex'].value_counts()
print(gender_counts)



flights_df = pd.read_parquet('flight')

flights_subset_df = flights_df[['origin', 'dest', 'carrier']]
print(flights_subset_df.head())


unique_destinations = flights_df['dest'].nunique()
print(f"Number of unique destinations: {unique_destinations}")


movie_df = pd.read_csv('movie.csv')
filtered_df = movie_df[movie_df['duration'] > 120]
sorted_df = filtered_df.sort_values(by='director_facebook_likes', ascending=False)
print(sorted_df.head())