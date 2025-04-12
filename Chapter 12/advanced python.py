#walrus operator :=
#walrus operator is used to assign values to variables within an expression, it is used to avoid multiple assignments and reduce the number of lines of code.

#example
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3) 

#types definition
def sum(a: int, b: int) -> int:
    return a + b
print(sum(1, 2)) # Output: 3

#match case
#match case is used to match the value of a variable with a pattern.
#example
def http_status(status): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status" 
# Usage 
print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status 






