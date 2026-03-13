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

#From CSV Files

