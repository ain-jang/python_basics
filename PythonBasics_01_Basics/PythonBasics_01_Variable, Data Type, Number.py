# CH02. Variable and Data Types
# CH02-01. Variable, Data Type, Number

# Variable: A storage box where a value is stored, and its symbolic name
# A = 1 << Put "1" in the box "A"
# All data types can be declared as a variable.
# Use print() function to check

# # Practice - Put "7" in a box "a" and "1" in a box "A"
a = 7
A = 1
print(a)
print(A)

# # Practice - Assign "1" to two variables
a = b = 1
print(a)
print(b)

# Things to know when naming a variable :
# 1. The name should show what the value means
# 2. Rules
#     1) Start with a lower case OR underscore(_)
#     2) Case-sensitive
#     3) Do not start with a number
#     4) Do not use special characters (i.e. +, _, %, &)
#     5) No space between the characters. Use an underscore to connect the words.
#     6) Do not use the reserved words (i.e. if, while, for)


# 2 categories of data types - Sequence & Non-sequence
# Sequence types
#     1) number: integer, float, operator
#     2) string
#     3) list
#     4) tuple
# Non-sequence types
#     1) dictionary
#     2) set
#     3) bool

# Use type() to see the data type of something

# # Practice - Find out what the data type using type() function.
print(type(3)) # int
print(type(-3.2)) # float

print(type("3")) # str

# Operators
#     1) addition(+), substraction(-), multiplication(*), division(/)
#     2) modulo remainder(%) 정수 나누기 연산자. 나누고 남은 수 구하기
#     3) trucated division(//) 나누기 연산자(몫)
#     4) power(**) 제곱

# Useful Functions
#     - int(): to convert a given number or a string to an integer number
#     - float(): to convert any value into a decimal or fractional number
#     - abs(): to return an absolute value of any numeric value input as an argument to the function
#     - pow(): computes the power of a number, accepting 2 or 3 arguments for exponentiation and optional modulus

# # Practice - Declare 3 variables (numbers) and use the operators
a = 6
b = 2
c = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a/c) # a/c = 1.5
print(a%c) # return = 2! (4*1 + "2")
print(a//c) # return = 1
print(a**b)

# # Practice - convert integer to decimal or fractional number, and vice versa
print(int(6.3))
print(int(-3.56))
print(float(15))
print(15)

# # Practice - Try abs() and pow()
print(abs(-3))
print(pow(3,2))


#END