# CH03. Input & Output, Control flow
# CH03-01. Input & Output

# User input - input(prompt) : to allow user input.
# The result is always strings.

x = input("What's your name?")
print(x)
print(type(x))

y = input("What's your favorite number?")
print(y)
print(type(y)) # str

# # Convert it to an integer or float
a = input("Give me a number")
b = input("Give me another one")
int_a = int(a) #1
int_b = int(b) #2

print(a + b) #12
print(type(a + b)) #str
print(int_a + int_b) #3
print(type(int_a + int_b)) #int


# Output - print() or ""
print("Python " + "is " + "good.")
print("Python " "is " "good.")

# use "," for space
print("Python", "is", "good.")


#END