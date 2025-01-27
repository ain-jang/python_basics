# CH03. Input & Output, Control flow
# CH03-02. File Input & Output

# Open(file, mode): it opens a file, and returns it as a file object.
#     "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#     "a" - Append - Opens a file for appending, creates the file if it does not exist
#     "w" - Write - Opens a file for writing, creates the file if it does not exist
#     "x" - Create - Creates the specified file, returns an error if the file exist
#     "c" - Close

# Open a file for writing.
myFile = open("python_practice_w.txt", "w")
myFile.write("Python is fun!")
myFile.close()

# Open a file for reading.
#     readline(): returns one line from the file
#     readlines(): returns a list containing each line in the file as a list item.
#     strip(): removes any leading, and trailing whitespaces.

# Open a file, write 2 lines, and close it.
myFile2 = open("python_practice.txt", "w")
myFile2.write("Python is fun!\nIsn't it?")
myFile.close()

# Open the file for reading.
read_file = open("python_practice.txt", "r")
test = read_file.readline()
print(test)

# Open the file for reading.
read_file = open("python_practice.txt", "r")
test2 = read_file.readlines()
print(test2)

# Remove the whitespaces using strip()
read_test_file = open("python-practice.txt", "r")
test_strip = read_test_file.readline().strip()
print(test_strip)
read_test_file.close()


#END