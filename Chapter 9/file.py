f = open("readme.txt")
content = f.read()
print(content) #output will be priyam is a good boy
f.close()

#modes
# "r" - read
# "w" - write
# "a" - append
# "r+" - read and write

st = "priyam is a coder"
f = open("myreadme.txt", "w")
f.write(st)
f.close()

# more file functions
# f.tell() - tells the current position of the cursor
# f.seek() - moves the cursor to the specified position
# f.readline() - reads a single line from the file
# f.readlines() - reads all lines from the file and returns a list of lines

#The best way to open and close the file automatically is the with statement. 
# Open the file in read mode using 'with', which automatically closes the file 
