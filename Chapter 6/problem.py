# Write a program to find the greatest of four numbers entered by the user.
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
n3 = int(input("enter the third number: "))
n4 = int(input("enter the fourth number: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print("n1 is the greatest number")
elif n2 > n1 and n2 > n3 and n2 > n4:
    print("n2 is the greatest number")
elif n3 > n1 and n3 > n2 and n3 > n4:
    print("n3 is the greatest number")
else:
    print("n4 is the greatest number")

#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

s1 = int(input("enter the marks of the first subject: "))
s2 = int(input("enter the marks of the second subject: "))
s3 = int(input("enter the marks of the third subject: "))

total_marks = (100*(s1 + s2 + s3)/300)

if total_marks >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33:
    print("you have passed the exam", total_marks)
else:
    print("you have failed the exam", total_marks)


#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spamss

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("enter the comment: ")

if p1 in comment or p2 in comment or p3 in comment or p4 in comment:
    print("this is a spam")
else:
    print("this is not a spam")


#Write a program to find whether a given username contains less than 10 characters or not. 

username = input("enter the username: ")
if len(username) < 10:
    print("username is less than 10 characters")
else:
    print("username is more than 10 characters")

#Write a program which finds out whether a given name is present in a list or not. 

list = ["harry", "shubham", "rohan", "hammad", "shivam"]
name = input("enter the name: ")

if name in list:
    print("name is present in the list")
else:
    print("name is not present in the list")

'''Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50=> F'''

marks = int(input("enter the marks: "))
if marks >= 90 and marks <= 100:
    print("Ex")
elif marks >= 80 and marks < 90:
    print("A")
elif marks >= 70 and marks < 80:
    print("B")
elif marks >= 60 and marks < 70:
    print("C")
elif marks >= 50 and marks < 60:
    print("D")
else:
    print("F")

#Write a program to find out whether a given post is talking about “Harry” or not.

post = input("enter the post: ")
if "harry".lower() in post.lower():
    print("harry is present in the post")
else:
    print("harry is not present in the post")





