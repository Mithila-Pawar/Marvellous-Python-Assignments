import pandas as pd
import numpy as np

salary = pd.Series([25000, 27000, 29000, 31000, 50000, 1000001])
Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = salary[(salary < lower_bound) | (salary > upper_bound)]
print("Q1: Outliers in Salary column:", outliers.tolist())