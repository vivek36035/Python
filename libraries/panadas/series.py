import pandas as pd

data = [10, 20, 30, 40, 50]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

print("Series:\n", s)

print("\nElement at index 'c':", s['c'])

print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Max:", s.max())
