import numpy as np

# 1D
a = np.array([1, 2, 3])
print(a)

# 2D
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)


# Get Dimension
print(b.ndim)

# Ge t Shape
print(a.shape)
print(b.shape)

# GetDtype
print(a.dtype)

# SIZE
print(a.itemsize)

# Total Size
print(b.size*b.itemsize)
