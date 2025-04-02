import pandas as pd

iris_df = pd.read_json('iris.json')

print(iris_df.shape)
print(iris_df.columns)

titanic_df = pd.read_excel('titanic.xlsx')
print(titanic_df.head())

flights_df = pd.read_parquet('flight')
print(flights_df.info())

movie_df = pd.read_csv('movie.csv')
print(movie_df.sample(10))
