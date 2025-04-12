try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
else: #will execute if no exceptions are raised
    print("Thank you")


#finally block will execute if an exception is raised or not
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally: #will execute breaking all the rules of the function
        print("hey i am inside finally block")
main()
