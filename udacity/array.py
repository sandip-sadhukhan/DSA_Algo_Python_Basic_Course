"""
Using native array & numpy array
"""
from array import array
import numpy as np

# Native Array
a = array("i", [4, 2])
a.append(3)
print("Native Array: ", a.tolist())
print("Type of Native Array: ", type(a))

print("-------------")

# Numpy Array
arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)
print("Type of Numpy Array: ", type(arr))
