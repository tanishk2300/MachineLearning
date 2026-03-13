import pandas as pd 

# this is series which is 1d array.
s = pd.Series([10, 20, 30, 40])
print(s)

# You can also define custom index:
a = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(a)

# A DataFrame is like a dictionary of Series — multiple columns with labels.
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
c=df.index  # Row labels 
d=df.columns# Column labels
print(c)
print(d)
