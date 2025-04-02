import pandas as pd

titanic_df = pd.read_excel('titanic.xlsx')

grouped_df = titanic_df.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'
}).rename(columns={'PassengerId': 'PassengerCount'})

print(grouped_df)

movie_df = pd.read_csv('movie.csv')

grouped_df = movie_df.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
})

print(grouped_df)