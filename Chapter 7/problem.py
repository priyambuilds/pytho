# Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

#Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")

#Attempt problem 1 using while loop. 
n = int(input("Enter a number: "))
i = 1
while(i<=10):
    print(f"{n} x {i} = {n*i}")
    i += 1

#Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not a prime number")
        break
    else:
        print("Prime number")
        break

#Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter a number: "))
i = 1
sum = 0 #for sum we need to initialize a variable as 0.
while(i<=n):
    sum += i
    i += 1
print(f"The sum of first {n} natural numbers is {sum}")

#Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter a number: "))
factorial = 1 #for product we need to initialize a variable as 1.
for i in range(1, n+1):
    factorial = factorial * i
print(f"The factorial of {n} is {factorial}") #output: The factorial of 5 is 120

#Write a program to print the following star pattern: 
#* 
#** 
#***      for n = 3
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*" * i)
    print()

#Write a program to print the following star pattern. 
#* 
#*** 
#***** for n = 3
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="") # 2*i-1 is the formula to print the odd number of stars.
    print()

#Write a program to print the following star pattern. 
#* * * 
#*   *   for n = 3 
#* * *  
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print("*" + " " * (n-2) + "*", end="")
    print()

# Write a program to print multiplication table of n using for loops in reversed order. 
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")