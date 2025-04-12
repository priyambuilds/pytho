a = ["harry", "priyam", "subha", "rohan"]

# we want to join these strings with a comma and a space.

final = "::".join(a)
print(final) #output: harry::priyam::subha::rohan

# we can also join a list of numbers with a comma and a space.
b = [1, 2, 3, 4, 5]
final = ", ".join(b)
print(final) #output: 1, 2, 3, 4, 5