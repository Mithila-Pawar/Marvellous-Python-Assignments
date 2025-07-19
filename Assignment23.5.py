import pandas as pd
import matplotlib.pyplot as plt

data = {"Name": ["Amit", "Sagar", "Pooja"],"Math": [85, 90, 78],"Science": [92, 88, 80],"English": [75, 85, 82]}

df = pd.DataFrame(data)

print("Shape:\n", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\n Descriptive stacticstics: \n",df.describe())

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
print("\nDataFrame with Total:\n", df)

high_science = df[df['Science'] > 85]
print("\nStudents with Science > 85:\n", high_science)

df['Name'] = df['Name'].replace('Pooja', 'Puja')
print("\nUpdated Names:\n", df)