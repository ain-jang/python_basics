# CH02. Variable and Data Types
# CH02-04. List

# List = Lists are used to store multiple items in a single variable.
# To create a list, use square brackets ([]).
# List = [element1, element2, ...]
mylist = [1, 1.25, 1, "word", [1, 2, [3, 4]]]
print(mylist)

# Indexing
print(mylist[0]) # 1
print(mylist[4][1]) # 2
print(mylist[4][2][0]) # 3

# Slicing
print(mylist[0:2]) # 1, 1.25
print(mylist[3:]) # "word", [1, 2, [3, 4]]

# Practice - what would be returned?
myList = [1, 5.2, 2*3, ['coffee', 'water', ['earl grey', 'english breakfast']]]
print(myList[3][2][0][:3])
#   ear

# +, -, len()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 * 2 + list2
print(list3) # [1, 2, 3, 1, 2, 3, 4, 5, 6]
print(len(list3)) # 9

# amend & delete elements
# 1. change "water" to "sparkling water"
# 2. delete "victoria grey"
list_beverage = ["coffee", "water", ["earl grey", "english breakfast", "victoria grey"]]

list_beverage[1] = "sparkling water"
del list_beverage[2][2]
print(list_beverage)

# Useful functions
#     - sort(): to sort the list (ascending by default)
#                 ** this doesn't create a new list!
#     - reverse(): to reverse the elements of the list
#     - append(): to append an element to the end of the list
#     - extend(): to add the specified list elements to the end of the list
#           append vs extend
#           > The append() method adds a single element to the end of the list while the extend() method adds all the elements of an iterable to the end of the list
#     - insert(a, b): to insert the specified value (b) at the specified position (a)
#     - remove(): to remove the first occurrence of a given item from the list
#     - pop():  to remove an element from a list at a specified index and return that element
#     - count(): returns the number of elements with the specified value.

mylist = [1, 5.2, 2, 6, 2]
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
mylist.append(90)
print(mylist)
mylist.insert(0, 80)
print(mylist)
mylist.extend([-2, 2.5])
print(mylist)
mylist.remove(5.2)
print(mylist)
mylist.sort()
mylist.reverse()
print(mylist)

last_number = mylist.pop()
print(last_number)

pop_and_delete = mylist.pop(1)
print(pop_and_delete)
print(mylist)

print(mylist.count(2))


#END