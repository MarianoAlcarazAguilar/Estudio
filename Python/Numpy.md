# Numpy

This is the core library for scientific computing in Python. You can also use mathematical operations with arrays.  

Array/Matrix operations  
Dot product  
Matrix multiplications  
Linear algebra  

## Basics

### Lists vs Arrays
Basically arrays are vectors. Which means you can treat them as one.  
```py
lista = [1,2,3,4]
array = np.array([1,2,3,4])

# To add an element to a list you do it like this
lista.append(5) or lista = lista + [5]
# This would return something like this: [1,2,3,4,5]

# If you do something like that in an array it would do this
array = array + np.array([5])
# Which would return this: [6,7,8,9]
```

### Creating an array

```py
a = np.array([1,2,3])
```
To get its properties you can use the next commands.  
```py
# This returns a tuple with the dimensions
# (number of rows, number of columns)
a.shape

# This returns the type of data
a.dtype

# This returns the number of dimensions
a.ndim

# This returns the total number of elements
a.size

# This returns the size in bites of the data types
a.itemsize
```

### Mathematical Operations
The next sintax is the same for the next functions:  
  - sum
  - mean
  - var
  - std
  - min
  - max
  - sqrt
  
```py
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Por default axis es None
a.sum(axis=None)

# Esto suma por columnas
a.sum(axis=0)

# Esto suma por renglones
a.sum(axis=1)

# La otra sintaxis es de esta forma
np.sum(a, axis=None)
```

To do a dot product you can use the next sintax
```py
a1 = np.array([[1,2,3]])
a2 = np.array([[4,5,6]])

# All of the next ways are correct
np.dot(a1,a2)
(a1 * a2).sum()
a1 @ a2
```

### Concatenation and Stacking
These bascically do the same, but they are different functions.
```py
a = np.array([[1,2,3]])
b = np.array([[4,5,6]])

# By default axis is zero, which means it will put b under a
c = np.concatenate((a,b), axis=0)

# c would look something like this
# [1,2,3]
# [4,5,6]

# If you use axis one it will put it to the right
d = np.array([[7],[8]])
e = np.concatenate((c,d), axis=1)

# e would look something like this
# [1,2,3,7]
# [4,5,6,8]
```

If you use stacking you don't have to specify the axis
```py
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.hstack((a,b))
# c would look something like this:
# [1,2,5,6]
# [3,4,7,8]

d = np.vstack
# d would look something like this:
# [1,2]
# [3,4]
# [5,6]
# [7,8]
```

## Multidimensional Arrays
The only difference is that you have to input a list of lists.  
```py
a = np.array([[1,2,3],[4,5,6]])

# To access rows you put the index of the row you want
a[0]

# To access a specific number
a[1][2]
a[1,2]

# To access all the rows in column index 2
a[:, 2]
```

### Matrix we can make
```py
ceros = np.zeros((2,3))
# This returns something like this:
# [0,0,0]
# [0,0,0]

unos = np.ones((2,3))
# This returns something like this:
# [1,1,1]
# [1,1,1]

cincos = np.full((2,3), 5)
# This returns something like this:
# [5,5,5]
# [5,5,5]

identity = np.eye(3)
# This returns something like this:
# [1,0,0]
# [0,1,0]
# [0,0,1]

numbers = np.arange(5)
# This returns something like this:
# [0,1,2,3,4]

spaced_numbers = np.linspace(0,10,5)
# This returns an array with five values between 0 and 10 (included) equally spaced with each other.
# [0, 2.5, 5, 7.5, 10]

```

### Reshaping an Array
```py
a = np.array([[1,2,3],[4,5,6]])

# a is something like this:
# [1,2,3]
# [4,5,6]

# Now we want to reshape it
a.reshape((3,2))

# a is now something like this:
# [1,2]
# [3,4]
# [5,6]
```

### Linear Algebra
```py
# Transposing an array
a.T

# Finding the inverse of an array
# Remember it must be a square matrix
np.linalg.inv(b)

# Determinant of a matrix
np.linalg.det(b)

# Diagonal matrix
# If you input a matrix, it returns an array with the elements in the diagonal.
np.diag(a)

# If you input an array with numbers, it returns a diagonal matrix with those numbers.
np.diag([1,2,3])
```

## Broadcasting
This allows numpy to work with arrays of different shape when making operations.

```py
a = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
b = np.array([[1,0,2]])

c = a + b
# What it would normally happen is that this addition can't be made
# because both matrix must be the same time; but numpy knows how to handle it.

# It treats b as if were something like this:
# [1,0,2]
# [1,0,2]
# [1,0,2]
# [1,0,2]

# So that at the end c looks like this:
# [2,2,5]
# [5,5,8]
# [2,2,5]
# [5,5,8]
```
