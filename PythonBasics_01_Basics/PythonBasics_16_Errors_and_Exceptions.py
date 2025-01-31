# CH04. Classes & Modules
# CH04-04. Errors and Exceptions

# Syntax Errors
#   : When the proper syntax of the language is not followed then a syntax error is thrown.
# For example...
# print("Python is fun!)
# This returns an error message since a quotation mark is missing.

# Runtime Errors (Exception)
#   : A runtime error occurs when the program is executed and encounters an issue that prevents it from continuing.
# For example...
# myList = [1, 2, 3, 4]
# myList[7]

# Exception Handling
#   : When an exception occurs, Python will normally stop and generate an error message.
#     These exceptions can be handled using the try,  except, else statements
#       The try block lets you test a block of code for errors.
#       The except block lets you handle the error.
#       The else block lets you execute code when there is no error.
#       The finally block lets you execute code, regardless of the result of the try- and except blocks.

try :
    Number = int(input("What's your favorite number? :"))
except :
    print("Error")
else :
    print("The user's favorite number is " + str(Number) + ".")
finally :
    print("END")

