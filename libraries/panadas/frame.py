import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Chennai']
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

print("\nName column:\n", df['Name'])

print("\nSecond row:\n", df.loc[1])

print("\nAverage Age:", df['Age'].mean())

df['Salary'] = [40000, 50000, 60000, 70000]
print("\nDataFrame after adding Salary column:\n", df)   