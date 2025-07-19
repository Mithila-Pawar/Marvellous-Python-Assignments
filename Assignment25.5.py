import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

salary = pd.Series([25000, 27000, 29000, 31000, 50000, 1000001])
Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = salary[(salary < lower_bound) | (salary > upper_bound)]
print("Q1: Outliers in Salary column:", outliers.tolist())

df_age = pd.DataFrame({'Name': ['A', 'C'], 'Age': [21.0, 22.0]})
print("\nQ2: Before converting Age:", df_age.dtypes)
df_age['Age'] = df_age['Age'].astype(int)
print("After converting Age:", df_age.dtypes)

df_city = pd.DataFrame({'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']})
le = LabelEncoder()
df_city['City_encoded'] = le.fit_transform(df_city['City'])
print("\nQ3: Label Encoded City:\n", df_city)

df_dept = pd.DataFrame({'Department': ['HR', 'IT', 'Trance', 'HR']})
df_dept_encoded = pd.get_dummies(df_dept, columns=['Department'])
print("\nQ4: One-Hot Encoded Department:\n", df_dept_encoded)

df_purchased = pd.DataFrame({'Age': [22, 25, 47, 52, 46, 56],'Purchased': [0, 1, 1, 0, 1, 0]})
X_train, X_test, y_train, y_test = train_test_split(df_purchased[['Age']], df_purchased['Purchased'], test_size=0.3, random_state=42)
print("\nQ5: Train Set:\n", X_train)
print("Q5: Test Set:\n", X_test)
