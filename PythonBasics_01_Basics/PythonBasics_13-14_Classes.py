# CH04. Classes & Modules
# CH04-01. Classes I
# CH04-02. Classes II

# Object oriented programming: a programming paradigm based on the concept of objects, which and contain data and code
# Class: a blueprint for creating objects
# To create a class, use the keyword "class"
# class gummybear :
#     pass

# Now we can use the class named gummybear to create objects.
# red_jelly = gummybear()
# yellow_jelly = gummybear()
# green_jelly = gummybear()

# The __init__() Function: All classes have a function called __init__(), which is always executed when the class is being initiated.
#   Use this to assign values to object properties, or other operations that are necessary to do when the object is being created
# Method: Methods in objects are functions that belong to the object

class GummyBear :
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste

# Create a list of jellies in 'GummyBear'
jellies = [
    GummyBear("red", "strawberry"),
    GummyBear("yellow", "lemon"),
    GummyBear("green", "apple")
]

# Print the color and taste of each jelly!
list_number = 0

for a in jellies:
    print("Color:", jellies[list_number].color, "|", "Taste:", jellies[list_number].taste)
    list_number = list_number + 1


# Inheritance: Inheritance allows us to define a class that inherits all the methods and properties from another class.
#   Parent class (base class): the class being inherited from
#   Child class (derived class): the class that inherits from another class
# The child's __init__() function overrides the inheritance of the parent's __init__() function.

# Create a parent and its child class
class Jellies:
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste

    def print_info(self):
        print("This is the parent class.")
        print("Class name: Jellies")

class FizzyFish(Jellies):
    def print_info(self):
        print("This is the child class.")
        print("Class name: FizzyFish")
        print("I'm overriding the print_info of my parent.")
        print("Taste : ", self.taste)
        print("Color : ", self.color)

# Now create an object of each class, and print their information.

black_jelly = Jellies("black", "cherry")
black_jelly.print_info()

blue_jelly = FizzyFish("blue", "cream soda")
blue_jelly.print_info()

# What did it return?
#   This is the parent class.
#   Class name: Jellies

#   This is the child class.
#   Class name: FizzyFish
#   I'm overriding the print_info of my parent.
#   Taste :  cream soda
#   Color :  blue


# The super() function
#   : will make the child class inherit all the methods and properties from its parent

# Now create another child class of Jellies, using the super() function
class Frutips(Jellies):
    def print_info(self):
        super().print_info()
        print("This is the child class.")
        print("Class name: Frutips")
        print("I'm using my parent's print_info. I'm behaving!")
        print("Taste : ", self.taste)
        print("Color : ", self.color)

# Create an object and print the info to check out the difference

pink_jelly = Frutips("pink", "peach")
pink_jelly.print_info()

# This is the parent class.
# Class name: Jellies
# This is the child class.
# Class name: Frutips
# I'm using my parent's print_info. I'm behaving!
# Taste :  peach
# Color :  pink