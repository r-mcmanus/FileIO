import os

f = open("test.txt")
print(f.read())
f.close()

#parsing the words in the text file and storing them in a list
a_list = []

with open('test.txt') as f:
    a_list = f.read().split()
f.close()

new_file = open("test2.txt", "w")
#"w" writes to a file and creates it if it doesn't exist yet.
for word in a_list:
    new_file.write(word + ' ')
new_file.close()

#getting the size of a file
file_size = os.path.getsize('test.txt')
print("File Size is :", file_size, "bytes")