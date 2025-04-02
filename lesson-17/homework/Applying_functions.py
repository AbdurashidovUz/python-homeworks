import pandas as pd

titanic_df = pd.read_excel('titanic.xlsx')

def classify_age(age):
    return 'Child' if age < 18 else 'Adult'

titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age)
print(titanic_df[['Age', 'Age_Group']].head())

employee_df = pd.read_csv('employee.csv')
if 'Department' in employee_df.columns:
    employee_df['Normalized_Salary'] = employee_df.groupby('Department')['Salary'].transform(lambda x: (x - x.mean()) / x.std())
    print(employee_df[['Department', 'Salary', 'Normalized_Salary']].head())
else:
    print("The 'Department' column does not exist in the DataFrame.")

movie_df = pd.read_csv('movie.csv')

def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movie_df['Duration_Class'] = movie_df['duration'].apply(classify_duration)
print(movie_df[['duration', 'Duration_Class']].head())