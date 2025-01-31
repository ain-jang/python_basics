# CH02. Variable and Data Types
# CH02-07. Bool

# Bool: represent one of two values - True or False
# When you run a condition in an if statement, Python returns True or False
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print("Python" == "Python") #True
print(10<11) #True
print(10>11) #False

# Conditions and If statements
if "python" :
    print("True")
else :
    print("False")  # True

if [] :
    print("True")
else :
    print("False") # False

if 1 :
    print("True")
else :
    print("False") # True

if 0 :
    print("True")
else :
    print("False") # False

# bool() Function : returns the boolean value of a specified object.
print(bool('')) # False
print(bool([1, 2, 3])) # True


#END