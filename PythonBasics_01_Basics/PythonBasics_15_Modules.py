# CH04. Classes & Modules
# CH04-03. Modules

# Module: A file containing a set of functions you want to include in your application.
# Built-in modules & External modules

# Built-in modules: a set of libraries that come pre-installed with the Python installation
#   help('modules') will show you all available modules in python
# External modules: collections of pre-written code that offer additional functions, classes, or methods not available in Python's standard library.
#   Use "pip" to install and manage the modules

# import statement (module_name.function_name.)
#   : Use a module by using the import statement
# Try and use math module
import math
print(math.floor(1.2)) #1
print(math.ceil(1.2)) #2

# from keyword (from module_name import function)
#   : to import only parts from a module
# Use from keyword, to import only floor and ceil from the math module
from math import floor, ceil
print(floor(1.2))
print(ceil(1.2))

# as keyword (import module_name as name_you_want)
#   : is used to create an alias
import math as m
print(m.floor(1.6))
print(m.ceil(1.2))


# External modules
#   : Numpy, Pandas,  Matplotlib, Seaborn, BeautifulSoup, Scikit_Learn
# Refer to module_practice_folder/practice_module_and_package.py

