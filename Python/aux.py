import numpy as np

# Numpy introduction
# The core library for scientific computing in Python
# Mathematical operations with arrays

# Numpy use case
# Array/Matrix operations
# Dot product
# Matrix multiplications
# Linear algebra

# Basics
# Creating an array

a = np.array([1, 2, 3])
print(a)
# This returns a tuple
print(a.shape)
# Returns type of data
print(a.dtype)
# Number of dimensions
print(a.ndim)
# Size returns the total number of elements
print(a.size)
# This returns the size in bites of the data types
print(a.itemsize)
# This prints the first element
print(a[0])
# To reassign elements to an index
a[0] = 1
print(a[0])

# Mathematical operations that work element wise
# This multiplies element by element
b = a * np.array([2, 0, 2])
print(b)


# Difference between arrays and lists
# Basically arrays are vectors

l = [1, 2, 3]
print(l)
l.append(4)
print(l)
l = l + [5]
print(l)
a = a + np.array([4])
print(a)

l = l * 2
print(l)
a = a * 2
print(a)

c = np.sqrt(a)
print(c)

# Dot product
# With lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
dot = 0

for i in range(len(l1)):
    dot += l1[i] * l2[i]

print(dot)
dot = 0
print(dot)
a1 = np.array(l1)
a2 = np.array(l2)

# All of these ways work
dot = np.dot(a1, a2)
print(dot)
dot = (a1 * a2).sum()
print(dot)
dot = a1 @ a2
print(dot)


# Arrays are way quicker than lists, like 200 hundred times faster


# Multidimensional arrays
# You need to send a list of lists
a = np.array([[1, 2, 3], [3, 4, 5]])
print(a)
# The first number is number of rows, and the second one is number of columns
print(a.shape)
# To access rows
print(a[0])
# To access a specific number
print(a[0][0])
print(a[0, 0])
# Print all the rows in column 3 (index 2)
print(a[:, 2])
# Transpose an array
print(a.T)
# Inverse of a matrix
# We make another matrix because it needs to be a square
b = np.array([[1,2],[3,4]])
print(np.linalg.inv(b))
# Calculate the determinant of a matrix
print(np.linalg.det(b))
# Calculate the diagonal matrix
# If you give the function a matrix, it returns an array with the elements in the diagonal
# If you give the function a vector, it returns a matrix with zeros except in the diagonal
c = np.diag(b)
print(c)
print(np.diag(c))

# More stuff
bool_idx = a > 2
# This returns a matrix with booleans where the criteria are met
print(bool_idx)
# This returns the numbers that satisfy the criteria. This will return a one dimension array
print(a[bool_idx])
print(a[a > 2])

# To get a matrix with the same shap, but it puts a minus one where it is false
b = np.where(a > 2, a, -1)
print(b)

# Fancy indexing
a = np.array([10,20,30,4,5,6,7,8])
b = [1,2,3]
print(a[b])


# Reshaping array
a = np.arange(1,7)
print(a)
print(a.shape)
b = a.reshape((2,3))
print(b)
print(b.shape)


# Concatenation
a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6]])
# By default, it is zero, this puts b under a
c = np.concatenate((a,b), axis=0)
print(c)
# This puts b next to a
c = np.concatenate((a,b.T), axis=1)
print(c)
# This makes it like a list
c = np.concatenate((a,b), axis=None)
print(c)

# We can also use stacking
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.hstack((a,b))
print(c)
c = np.vstack((a,b))
print(c)


# Broadcasting
# Allows numpy to work with arrays of different shape when making operations
x = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
a = np.array([1,0,1])
# What this does are that it applies it to all of it iven when the dimensions are not the same
y = x + a
print(y)


# Operations with matrix
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)
# By default, it is none
print(a.sum(axis=None))
# Esto lo suma por columnas
print(a.sum(axis=0))
# Esto lo suma por renglones
print(a.sum(axis=1))

# This works exactly the same if we use mean
# We can also use variance with var
# We can use it with standard deviation std
# Also min, and max
# Another way of doing it is like this
print(np.std(a, axis=1))


# Different data types
x = np.array([1.0,2])
print(x)
print(x.dtype)

y = np.array([1,3], dtype=np.float32)
print(y.dtype)


# Making different matrix
a = np.zeros((2,3))
print(a)

b = np.ones((2,3))
print(b)

c = np.full((2,3), 5)
print(c)

d = np.eye(3)
print(d)

e = np.arange(20)
print(e)

# Esto regresa 5 valores entre 0 y 10 con la misma distancia entre ellos
f = np.linspace(0,10,5)
print(f)

#################################################
