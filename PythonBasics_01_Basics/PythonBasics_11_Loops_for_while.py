# CH03. Input & Output, Control flow
# CH03-04. Loops - for, while

# For Loops
# A for loop is used for iterating over a sequence
#  that is either a list, a tuple, a dictionary, a set, or a string
# for loops are used when you have a block of code which you want to repeat a fixed number of times.

for i in range(5):
    print("Python is the best!")


# Looping through a string
x = "Korea"

for a in x:
    print(a)


# Create a list of country names and print each in the list.
country_list = ["South Korea", "Czechia", "Finland"]

for a in country_list:
    print(a)

# what's different compared to print(country_list)?
print(country_list)


# Looping through a dictionary
mydictionary = {
    "name" : ["James", "Martin"],
    "job" : ["Data Scientist", "Software Engineer"]
    }

for a in mydictionary:
    print(a, ":", mydictionary[a])


# Looping  through a range
# range(): returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
print(range(5)) # range(0, 5)
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(5, 10))) #[5, 6, 7, 8, 9]
print(list(range(5, 10, 2))) #[5, 7, 9]

for i in range(5):
    print(i)

for i in range(3, 20, 4):
    print(i)



# While Loops
# With the while loop we can execute a set of statements as long as a condition is true.
# Remember to increment i, or else the loop will continue forever.

# Print count until it reaches 5
count = 0

while count < 5:
    print("count:", count)
    count = count + 1

# The break statement: you can stop the loop even if the while condition is true
a = 10
count = 0

while a > 3:
    count = count + 1
    a = a + 1
    if count > 20:
        break
    print("a:", a, "count:", count)


print("Loop Ended")


# Continue keyword: is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

num = 0

while num < 10:
    num = num + 1
    if num <= 5:
        continue
    print(num)


#END