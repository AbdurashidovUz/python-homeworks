import pandas as pd

titanic_df = pd.read_excel('titanic.xlsx')

def filter_survived(df):
    return df[df['Survived'] == 1]

def fill_missing_age(df):
    df.loc[:, 'Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df.loc[:, 'Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

titanic_df = (titanic_df.pipe(filter_survived)
                          .pipe(fill_missing_age)
                          .pipe(add_fare_per_age))

print(titanic_df.head())