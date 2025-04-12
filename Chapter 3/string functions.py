name = "priyam"
print(len(name)) #output: 6
print(name.endswith("m")) #output: True
print(name.endswith("yama")) #output: False
print(name.capitalize()) #output: Priyam
print(name.startswith("p")) #output: True

#most used string functions
name = "priyam"
print(name.count("a")) #output: 2
print(name.count("a", 0, 6)) #output: 2
print(name.count("a", 0, 3)) #output: 1
print(name.count("a", 3, 6)) #output: 1

#find function this function returns the index of the word we are looking for.
name = "priyam"
print(name.find("a")) #output: 2
print(name.find("a", 0, 6)) #output: 2
print(name.find("a", 0, 3)) #output: 1
print(name.find("a", 3, 6)) #output: 1              

#replace function this function replaces the word we are looking for with the word we want to replace it with.
name = "priyam"
print(name.replace("a", "o")) #output: priyom
print(name.replace("a", "o", 1)) #output: priyom. It replaces only the first occurrence of "a" with "o".

#split function
name = "priyam"
print(name.split("a")) #output: ['priy', 'm']
print(name.split("a", 1)) #output: ['priy', 'm']
print(name.split("a", 2)) #output: ['priy', 'm']


