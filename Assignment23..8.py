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

sorted_df = df.sort_values(by='Total', ascending=False)
print("\nSorted by Total (Descending):\n", sorted_df)

plt.bar(df['Name'], df['Total'], color='skyblue')
plt.title("Total Marks of Students")
plt.xlabel("Name")
plt.ylabel("Total Marks")
plt.show()

amit_data = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].values.flatten()
subjects = ['Math', 'Science', 'English']

plt.plot(subjects, amit_data, marker='o', linestyle='-', color='green')
plt.title("Subject-wise Marks for Amit")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()