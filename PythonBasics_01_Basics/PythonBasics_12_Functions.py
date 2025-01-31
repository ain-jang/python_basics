# CH03. Input & Output, Control flow
# CH03-05. Functions

# Function: A function is a block of code which only runs when it's called
# A function is defined using the def keyword

def add(x, y):
    return x + y

z = add(3, 6)
print(z)

# Parameter (Argument): information that are passed into a function
# default arguments: Default values indicate that the function argument will take that value if no argument value is passed during the function call.
# def function_name(param1, param2=default_value2, ...)
def add2(x, y =3):
    return x + y

d = add2(4) # 4 + 3 = 7
print(d)

# *args: Arbitrary Arguments,This way the function will receive a tuple of arguments, and can access the items accordingly

def menu(*values):
    print("What's the menu?")

    for value in values:
        print(value)

menu("Americano", "Cafe Latte", "Chocolate Frappuccino", "Earl Grey")


# Keyword Arguments: You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def new_add(x = 1, y = 2, g =3):
    return x + y + g

jj = new_add(y = 2, g = 3, x = 1) # 1 + 2 + 3 = 6
print(jj)


# return: to exit a function and return a value.

def return_test():
    return "Returned value"

value = return_test()
print(value)

def return_test2():
    n = 3
    m = 4
    return n, m

value1, value2 = return_test2()
print(value1)
print(value2)


#END