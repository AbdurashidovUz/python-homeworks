import pandas as pd

iris_df = pd.read_json('iris.json')

numeric_cols = iris_df.select_dtypes(include='number')

mean_values = numeric_cols.mean()
median_values = numeric_cols.median()
std_values = numeric_cols.std()

print("Mean values:\n", mean_values)
print("Median values:\n", median_values)
print("Standard deviation values:\n", std_values)

titanic_df = pd.read_excel('titanic.xlsx')
min_age = titanic_df['Age'].min()
max_age = titanic_df['Age'].max()
sum_age = titanic_df['Age'].sum()

print(f"Minimum age: {min_age}")
print(f"Maximum age: {max_age}")
print(f"Sum of ages: {sum_age}")


movie_df = pd.read_csv('movie.csv')
director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()
top_director_likes = director_likes.max()

print(f"Director with the highest total Facebook likes: {top_director} ({top_director_likes} likes)")


longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'duration', 'director_name']]
print("5 longest movies and their directors:\n", longest_movies)
