
# Numpy documentation: https://numpy.org/doc/stable/index.html

import numpy as np

# Numpy array (ndarray OR array)
# different from python.array
#   : numpy array끼리 연산 가능, 그러나 pythoon list는 덧셈만 가능
#   : 넘파이는 어레이 전체 연산이 되지만 파이썬은 곱셈(반복)만 가능

# 넘파이는 모든 배열의 값이 기본적으로 같은 타입(e.g. 정수, 실수)
# 각 차원(dimension)을 축(axis)이라고 표현함
# 1D, 2D, 3D array - shape(_, _, _)
# For example...
# 1) [[1, 0, 0], [0, 1, 2]] 에서 축은 2개 (2D) / 첫번째 축은 길이 2, 두 번째 축은 길이 3
#    -> [[1, 0, 0]
#       [0, 1, 2]]
# 2) [1, 2, 1] 에서 축은 1개(1D) / 축 길이는 3
#    -> [1, 2, 1]

# Numpy 배열 대표 속성값
# ndarray.shape: 배열의 각 축(axis)의 크기
# ndarray.ndim: 축의 개수(dimension)
# ndarray.dtype: 각 요소(element)의 타입
# ndarray.itemsize: 각 요소의 타입의  bytes 크기
# ndarray.size: 전체 요소의 개수

# Create a 2D array with a size of (3,4)
a = np.arange(12).reshape(3, 4)
print(a)

# ndarray.shape : Tuple of array dimensions.
print(a.shape) #(3.4)

# ndarray.dtype : data-type of the array’s elements.
print(a.dtype) #int64

# ndarray.itemsize : length of one array element in bytes.
print(a.itemsize)

# ndarray.size : Number of elements in the array.
print(a.size) #12


# How to create a numpy array (ndarray).
# np.array : will convert a tuple or any array-like object into an ndarray.
# np.zeros(shape) : returns a new array of given shape and type, filled with zeros.
# np.ones(shape) : returns a new array of given shape and type, filled with ones.
# np.empty(shape): returns a new array of given shape and type, without initializing entries.

b = np.array([2, 3, 4])
print(b)
print(b.dtype)

c = np.array([1.2, 3.5, 4,1])
print(c)
print(c.dtype)


# Create a 2-D array with 3 rows and 4 columns filled with zeros.
print(np.zeros((3,4)))

# Create a 3-D array with a shape of (2,3,4) filled with ones.
print(np.ones((2,3,4)))

# Create a 2D array with a shape of (2,3) without initializing entries
print(np.empty((2, 3)))


# numpy.arange & numpy.linspace
# np.arange([start, ]stop, [step])
#   : Return evenly spaced values within a given interval.
#   * The interval doesn't include the 'stop' value
# np.linspace(start, stop, num=n)
#   : Return evenly spaced numbers over a specified interval.
#   * The endpoint of the interval is included, but can optionally be excluded.

# Create an array with values from 10(inclusive) to 30(exclusive) increasing by 5.
print(np.arange(10, 30, 5))

# Create an array with values from 0 (inclusive) to 2 (exclusive) increasing by 0.3
print(np.arange(0,2,0.3))

# Create a numpy array with 100 evenly spaced values from 0 to 99 (inclusive)
x = np.linspace(0, 99, 100)
print(x)

# To make it clear, you could try this...
print(np.arange(0, 1+0.25, 0.25))

print(np.linspace(0, 1, 5))

# A little bit more about 3D numpy array...
c = np.arange(24).reshape(2,3,4)
print(c)

# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]


# Element wise operations on numpy arrays
array1 = np.array([20,30,40,50])
array2 = np.arange(4)
print(array1) #[20 30 40 50]
print(array2) #[0 1 2 3]

minusarrays = array1 - array2
print(minusarrays) #[20 29 38 47]

print(array2**2) #[0 1 4 9]

print(10*array1) #[200 300 400 500]

print(array1 < 35) # [ True  True False False]

# * : element wise multiplication
# @ : matrix multiplication

arrayA = np.array([[1,1],
                   [0,1]])
arrayB = np.array([[2,0],
                   [3, 4]])
print(arrayA)
print(arrayB)

print(arrayA * arrayB)
print(arrayA @ arrayB)

# data type & upcasting
# data type size: int < float < complex

A = np.ones(3, dtype=np.int32)
B = np.linspace(0, np.pi,  3)

print(A) #[1 1 1]
print(B) #[0.         1.57079633 3.14159265]
print(A.dtype) #int32
print(B.dtype) #float64

C = A + B
print(C)
print(C.dtype) #float64

D  = np.exp(c*1j)
print(D)
print(D.dtype) #complex128


# Mathematical functions
#  https://numpy.org/doc/stable/reference/routines.math.html
# .sum : sum of array elements over a given axis.
# .min : returns the minimum of an array or minimum along an axis
# .max : returns the maximum of an array or maximum along an axis
# .argmax: the indices of the maximum values along an axis
# .cumsum: the cumulative sum of the elements along a given axis

aa = np.arange(8).reshape(2,4)**2
print(aa)

print(aa.sum())

print(aa.min())
print(aa.max())

print(aa.argmax())

print(aa.cumsum())

# a sum could be performed on specific axes
#   https://numpy.org/doc/stable/reference/generated/numpy.sum.html
# row - axis 0, column - axis 1

bb = np.arange(12).reshape(3,4)
print(bb)

print(bb.sum(axis=0))
print(bb.sum(axis=1))


# Universal functions
#  https://numpy.org/doc/stable/reference/ufuncs.html

# add(x1, x2, /[, out, where, casting, order, ...]) : Add arguments element-wise.
# subtract(x1, x2, /[, out, where, casting, ...]) : Subtract arguments, element-wise.
# multiply(x1, x2, /[, out, where, casting, ...]) : Multiply arguments element-wise.
# divide(x1, x2, /[, out, where, casting, ...]) : Divide arguments element-wise.
# log(x, /[, out, where, casting, order, ...]) : Natural logarithm, element-wise.
# sin(x, /[, out, where, casting, order, ...]) : Trigonometric sine, element-wise.
# cos(x, /[, out, where, casting, order, ...]) : Cosine element-wise.
# tan(x, /[, out, where, casting, order, ...]) : Compute tangent element-wise.

cc = np.array([1, 4, 9])
print(cc)

# y = sqrt(x)
print(np.sqrt(8))
print(np.sqrt(64))


# Indexing & Slicing
aaa = np.arange(8)**2 # 0 1 4 9 15 25 36 49

i = np.array([1, 1, 3, 5])
print(aaa[i]) # 1 1 9 25

j = np.array([[3,4],[2,5]])
print(aaa[j])
# 9 16
# 4 25

# Practice

bbb = np.arange(8)**2
print(bbb) # [ 0  1  4  9 16 25 36 49]

ii = np.array([1, 1, 3, 5])
print(bbb[ii]) # 1, 1, 9, 25


ddd = np.arange(10)**2
print(ddd)
#  [ 0  1  4  9 16 25 36 49 64 81]

print(ddd[2]) # 4

print(ddd[2:5]) # 4 9 16

print([ddd[ : : -1]])

print(ddd[0:6:2])
ddd[0:6:2] = 1000
print(ddd)


# Numpy Boolean Indexing
#   :https://numpy.org/doc/2.2/user/basics.indexing.html#boolean-array-indexing
# useful when you want to extract only data you want (e.g. b = a>4 (True))

Aa = np.arange(12).reshape(3,4)
print(Aa)

Bb= Aa > 4

print(Aa[Bb]) # [5 6 7 8 9 10 11]

print(Aa[Bb].shape) # (7,)

Aa[Bb] = 0

print(Aa)


# How to change the shape of a numpy array
# .ravel: flattens an input array into a contiguous 1D array ( == .reshape(-1))
#        https://numpy.org/doc/stable/reference/generated/numpy.ravel.html
# .reshape: gives a new shape to an array without changing its data.
#        https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
# .T: returns an array with axes transposed.
#        https://numpy.org/doc/stable/reference/generated/numpy.transpose.html

g = np.arange(12).reshape(3,4)
print(g)
print(g.shape)

print(g.ravel())
# print(g.reshape(-1))

print(g.reshape(2,6))

print(g.T)
print(g.T.shape) # (4,3)


# Stack the arrays!
# np.vstack(): Stack arrays in sequence vertically (row wise).
#              https://numpy.org/doc/stable/reference/generated/numpy.vstack.html
# np.hstack(): Stack arrays in sequence horizontally (column wise).
#              https://numpy.org/doc/stable/reference/generated/numpy.hstack.html


v = np.array([1, 2, 3, 4]).reshape(2,2)
print("This is array V")
print(v)

h = np.array([5, 6, 7, 8]).reshape(2,2)
print("This is array H")
print(h)

print("vstack")
print(np.vstack((v, h)))
print("hstack")
print(np.hstack((v, h)))


# You can also split an array!
# np.hsplit(): split an array into multiple sub-arrays horizontally (along the columns)
#             https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html

H = np.arange(12).reshape(2,6)
print(H)

# using np.hsplit, split the array into three equal parts.
print("Practicing np.hsplit")
print(np.hsplit(H, 3))


# Using np.hsplit, split the array into three parts at colum indices 3 and 4
print("Practicing np.hsplit 2")
print(np.hsplit(H, (3,4)))



#END