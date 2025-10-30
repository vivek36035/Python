import pandas as pd

data = {'Name': ['Vivek', 'Ravi', 'Priya', 'Anil'], 'Age': [21, 23, 22, 24], 'Marks': [85, 90, 88, 92]}
df = pd.DataFrame(data)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.sort_values('Marks'))
print(df['Name'])
print(df['Marks'].mean())
print(df['Marks'].max())
print(df.groupby('Age')['Marks'].mean())
print(df.drop(columns=['Age']))