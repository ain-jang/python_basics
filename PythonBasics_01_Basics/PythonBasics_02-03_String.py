# CH02. Variable and Data Types
# CH02-02. String I
# CH02-03. String II

# Use "" OR '' to create a string
word = "Hello!"
print(word)

print('Hello!')

# How to put '' in a string
print("I'm Ain.")

# Escape character - backslash (\): to insert characters that are illegal in a string, use an escape character.
# Tip: text - "", programming stuff - '' (e.g. \n)
print('I\'m studying \'Python\'.')
print("I'm studying Python.")
print("I'm studying \"Python\".")

# Use """ (OR ''') to create multiline strings.
# In the result, the line breaks are inserted at the same position as in the code.
sentence1 = """
I want to write four lines.
not two,
not three,
four!
"""

print(sentence1)

# Tip - Use \ to remove the new line in the beginning and at the end
sentence2 = """\
I want to write four lines.
not two,
not three,
four!\
"""

print(sentence2)

# Escape characters
#     1) \n : new line
#     2) \t : tab
#     3) \\ : \ (not the escape character, just backslash)
#     4) \' : single quotation
#     5) \" : double quotation
# Try and use them!

a = "1\n2"
b = "1\t2"
c = "1\\2"
d = "\'12\'"
e = "\"12\""

print(a)
print(b)
print(c)
print(d)
print(e)
print("how about I try this?")
print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)

# String Operators:
#     1) + : to connect strings
#     2) * : to repeat strings

phrase1 = "Python"
phrase2 = " is amazing!"
print(phrase1 + phrase2)

# Create a nice banner using [+] and [*]
equal = "=" * 30
banner_message = "\nWelcome to Python world!\n"
banner = equal + banner_message + equal

encouragement = "Go! " * 2
under_banner = encouragement + "Ain!"

print(banner)
print(under_banner)

# Indexing([]): the process of accessing a specific element in a sequence, such as a string or list, using its position or index number.
# The first element in a sequence has an index of 0.
# Use -1 to start at the end.

indexing_example = "It is Saturday."

print(indexing_example[0])
print(indexing_example[-1])
print(indexing_example[2])

# Slicing([:]): to return a range of characters
# string[start index: end index]
# the end index is not included in the return.

slicing_example = "It is Saturday."

print(slicing_example[0:3])
print(slicing_example[-3:-1])

# Formatting(using % operator)
#     1) %d: integers
#     2) %f: floating point numbers
#     3) %c: single character
#     4) %s: string

sentence = "I take Line %d every morning."
print(sentence % 4)

sentence2 = "I take Line %d every morning." % 4
print(sentence2)

a = "work"
b = 3
sentence3 = "I take Line %d to %s." % (b, a)
print(sentence3)

# formatting using 'format()' : this formats the specified value(s) and insert them inside the string's placeholder.
# Define the placeholder using curly brackets({})
# {}.format(value)

print("I take Line {} every morning.".format(4))
print("I take Line {0} every morning.".format(4))


# Useful functions
#     - len(): the number of items in an object
#     - split(): splits a string into a list
#     - count(): returns the number of elements with the specified value.
#     - replace("a", "b"): to replace "a" with "b"
#     - find("a"): finds the first occurrence of the specified value
#     - upper(): returns a string where all characters are in upper case
#     - lower(): returns a string where all characters are in lower case
#     - join(): takes all items in an iterable and joins them into one string

sentence = "She loves you."
print(len(sentence))
print(sentence.split())
print(sentence.count("o"))
# print(sentence.replace("She", "He"))
sentence_replaced = sentence.replace("She", "He")
print(sentence_replaced)
print(sentence.find("s"))

file_name = "Chocolate.jpg"
print(file_name)
print(file_name.upper())
print(file_name.lower())

join_sentence = ".".join("LOVE")
print(join_sentence)


#END