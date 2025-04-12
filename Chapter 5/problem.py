#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

hindi_dict = {
    "aaj": "today",
    "kal": "yesterday",
    "parso": "tomorrow",
}
word = input("Enter a word: ")
print(hindi_dict[word])

#Write a program to input eight numbers from the user and display all the unique numbers (once).
numbers = set()
a = int(input("Enter a number 1: "))
numbers.add(int(a))
b = int(input("Enter a number 2: "))
numbers.add(int(b))
c = int(input("Enter a number 3: "))
numbers.add(int(c))
d = int(input("Enter a number 4: "))
numbers.add(int(d))
e = int(input("Enter a number 5: "))
numbers.add(int(e))
f = int(input("Enter a number 6: "))
numbers.add(int(f))
g = int(input("Enter a number 7: "))
numbers.add(int(g))
h = int(input("Enter a number 8: "))
numbers.add(int(h))
print(numbers)

#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
dict ={}
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name:language})
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name:language})
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name:language})
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dict.update({name:language})
print(dict)

#Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]} 
#s[5] = 4 #this will give an error because lists are unhashable.
#you cannot have lists in sets.


