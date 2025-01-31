# CH02. Variable and Data Types
# CH02-06. Set

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable (except for adding and removing items), and unindexed.
#   If want to make it ordered, use a list or tuple instead.
# Create a set with the set() constructor.
set1 = set([10, 11, 12])
print(set1) # {10, 11, 12}
print(type(set1)) # class 'set'

set2 = {"Python sets"}
print(set2) # {'Python sets'}
print(type(set2)) # class 'set'

set3 = set("Python sets")
print(set3) # {'o', 'h', 'y', 'P', 'n', 't', ' ', 'e', 's'}
print(type(set3)) # class 'set'

set4 = set(["Python sets"]) # {'Python sets'}
print(set4) # class 'set'
print(type(set4))

## Key difference between set() and {}
    # : Key Difference:
    # set() is used when you want to convert an iterable (like a list or string) into a set.
    # {} is a literal way to directly create a set with the items you want.

# Union(|), intersection(&), difference(-)
set_a = {1, 2, 3, 4, 5}
set_b = {1, 3, 5, 7, 9}

print(set_a | set_b) # {1, 2, 3, 4, 5, 7, 9}
print(set_a & set_b) # {1, 3, 5}
print(set_a - set_b) # {2, 4}
print(set_b - set_a) # {9, 7}

# Useful functions
#     - add(): to add one item to a set
#     - update(): to add items from another set (or any other iterable)
#     - remove(): to remove the specified element from the set
set_A = {1, 2, 3, 4, 5}
set_A.add(6)
print(set_A) # {1, 2, 3, 4, 5, 6}
set_A.update([13, 11])
print(set_A) # {1, 2, 3, 4, 5, 6, 11, 13}
set_A.remove(6)
print(set_A) # {1, 2, 3, 4, 5, 11, 13}


#END

