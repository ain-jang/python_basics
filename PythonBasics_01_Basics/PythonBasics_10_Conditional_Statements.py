# CH03. Input & Output, Control flow
# CH03-03. Conditional Statements

# If statement : if the statement is true, it will execute the code. if false, it won't execute the code.
# Mind the indentation!
# Else: The else keyword catches anything which isn't caught by the preceding conditions.

python_study = False

if python_study :
    print("Python is fun!")
else :
    print("Python is not fun at all!")


# Elif: "if the previous conditions were not true, then try this condition if the previous conditions were not true, then try this condition"

score = "C"
if score == "A" :
    print("Class A")
elif score == "B" :
    print("Class B")
elif score == "C" :
    print("Class C")
else :
    print("Class 0")

# in / not in Operators
if "y" not in "python" :
    print(True)
else:
    print(False)

# pass keyword
basket = ["apple", "banana"]

if "strawberry" not in basket :
    pass

# Logical Operators; not, and, or
print(not True) # False
print(not False) #True

print(True and True) #True
print(True and False) #False
print(False and False) #False
print(False and True) #False

print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False



## Practice!
question1 = input("Is the class over? (Y/N)")
endOfSelenaClass = question1

if endOfSelenaClass == "Y" :
    question2 = input("Self Review Score?")
    SelfReviewScore = int(question2)
    if  SelfReviewScore >= 90 :
        print("Perfect! :)")
    elif 50 <= SelfReviewScore < 90 :
        print("Not bad! Keep going!")
    else :
        print("Try harder. You've got this! :)")
else :
    print("Focus on the class!")