# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same. 
try:
    with open("1.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

try:
    with open("2.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

try:
    with open("3.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")


# 2. Write a program to print third, fifth and seventh element from a list using enumerate function. 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, item in enumerate(list):
    if i ==2 or i ==4 or i ==6:
        print(item)

# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number. 

n = int(input("Enter a number: "))
table = [i*n for i in range(1, 11)]
print(table)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’. 
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
try:
    print(n1/n2)
except ZeroDivisionError:
    print("infinite")

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
with open("Tables.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{n} x {i} = {n*i}\n")

