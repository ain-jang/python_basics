# CH02. Variable and Data Types
# CH02-05. Tuple & Dictionary

# Tuple '(data1, data2, data3, ...)'
#     * Should put ' , ' at the end when there's only one item > (data1,)

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is order and UNCHANGEABLE.

# Create a tuple with only one item
tuple1 = (1.5,)
print(tuple1)
print(type(tuple1))
float1 = (1.5)
print(float1)
print(type(float1))

tuple2 = 1, 2, 3, 4, 5
print(tuple2)
print(type(tuple2))

# Indexing & Slicing with tuples
tuple_indexing = 9, 8, 7, 6
print(tuple_indexing[0])

tuple_slicing = 9, 8, 7, 6
print(tuple_slicing[:2])

# Operators: +, *, len()
tuple_op_1 = (4, 3, 2, 1, 0)
tuple_op_2 = 1, 2, 3, 4, 5
tuple_op_test = tuple_op_1 * 2 + tuple_op_2
print(tuple_op_test)
print(len(tuple_op_test))



# Dictionary '{key1 : value1, key2 : value2, ...}'
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable, and do not allow duplicates.

# Create a dictionary
dictionary1 = {
    "name" : "Ain",
    "zodiac sign" : "Capricorn",
    "member since" : 2025
}

print(dictionary1)
print(dictionary1["name"])
print(dictionary1["zodiac sign"])
print(dictionary1["member since"])


# Dictionaries are changeable!
# Add an item "favorite" to the dictionary
dictionary1["favorite"] = ["Iced Americano", "Chai Latte"]
print(dictionary1)
# Now try and edit the items
dictionary1["favorite"] = ["Iced Americano", "Mocha Latte"]
print(dictionary1)
# delete the 'favorite' item
del dictionary1["favorite"]
print(dictionary1)


# Useful functions
#     - keys() : returns the "keys" of the dictionary as a list
#     - values() : returns the "values" of the dictionary as a list
#     - items() :  returns the dictionary's "key-value pairs".
#     - get(keyname, value) : returns the value of the item with the specified key
#     - in(keyname in dictionaryname) : to see if the specific key is in the dictionary
#     - clear() : removes all the elements from a dictionary


dictionary2 = {
    "name": "Ain",
    "zodiac sign": "Capricorn",
    "member since": 2025
}
print(dictionary2)

# Try and find out the keys and values in the dictionary.
print(dictionary2.keys())
print(dictionary2.values())
print(dictionary2.items())

# What is Ain's zodiac sign?
print(dictionary2.get("zodiac sign"))


#END