#recursive function is a function that calls itself.
# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2*1
# factorial(3) = 3*2*1
# factorial(4) = 4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(n) = n*n-1*n-2*n-3*......3*2*1
# factorial(n) = n*factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")

#The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most direct way to code an algorithm.