#Write a program to store seven fruits in a list entered by the user.
fruits = []
f1 = input("Enter fruit 1: ")
fruits.append(f1)
f2 = input("Enter fruit 2: ")
fruits.append(f2)
f3 = input("Enter fruit 3: ")
fruits.append(f3)
f4 = input("Enter fruit 4: ")
fruits.append(f4)
f5 = input("Enter fruit 5: ")
fruits.append(f5)
f6 = input("Enter fruit 6: ")
fruits.append(f6)
f7 = input("Enter fruit 7: ")
print(fruits)

#Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
m1 = int(input("Enter marks of student 1: "))
marks.append(m1)
m2 = int(input("Enter marks of student 2: "))
marks.append(m2)
m3 = int(input("Enter marks of student 3: "))
marks.append(m3)
m4 = int(input("Enter marks of student 4: "))
marks.append(m4)
m5 = int(input("Enter marks of student 5: "))
marks.append(m5)
m6 = int(input("Enter marks of student 6: "))
marks.append(m6)
print(marks)

marks.sort()
print(marks)

#Check that a tuple cannot be changed in python.
a = (1, 2, 3, 4, 5)
print(sum(a)) #output: 15

#Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9) 
print(a.count(0)) #output: 3
