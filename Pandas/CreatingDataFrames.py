import pandas as pd 

#From Python Lists
data1 = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]
b = pd.DataFrame(data1, columns=["Name", "Age"])
print(b)

#From Dictionary of Lists
data2 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

a = pd.DataFrame(data2)
print(a)

#From NumPy Arrays
import numpy as np
arr = np.array([[1, 2], [3, 4]])
c = pd.DataFrame(arr, columns=["A", "B"])
print(c)

# #From CSV Files
# f=pd.read_csv("data.csv", usecols=["Name", "Age"])
# print(f)

# # From Excel Files
# g = pd.read_excel("data.xlsx")
# print(g)

# # From JSON
# h = pd.read_json("data.json")
# print(h)

# # From SQL Databases
# import sqlite3

# conn = sqlite3.connect("mydb.sqlite")
# i = pd.read_sql("SELECT * FROM users", conn)
# print(i)


# # From the Web (Example: CSV from URL)
# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
# df = pd.read_csv(url)
# print(j)

# # EDA (Exploratory Data Analysis)
# df.head()         # First 5 rows
# df.tail()         # Last 5 rows
# df.info()         # Column info: types, non-nulls
# df.describe()     # Stats for numeric columns
# df.columns        # List of column names
# df.shape          # (rows, columns)