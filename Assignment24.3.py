import pandas as pd
import matplotlib.pyplot as plt

data = {"Name": ["Amit", "Sagar", "Puja"],"Math": [85, 90, 78],"Science": [92, 88, 80],"English": [75, 85, 82]}
df = pd.DataFrame(data)
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

df['Math_Normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
print("Q1 - Normalized Math:\n", df[['Name', 'Math', 'Math_Normalized']])

df['Gender'] = ['Male', 'Male', 'Female']
df_encoded = pd.get_dummies(df, columns=['Gender'])
print("\nQ2 - One-hot Encoded Gender:\n", df_encoded)

grouped = df.groupby('Gender')[['Math', 'Science', 'English', 'Total']].mean()
print("\nQ3 - Grouped by Gender (Average Marks):\n", grouped)