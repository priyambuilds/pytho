#properties of sets:
#1. Sets are unordered.
#2. Sets are mutable.
#3. Sets cannot contain duplicate values.
#4. there is no way to change the elements of the set.
#5. sets are unindexed.

s = {1, 2, 3, 4, 5, "harry"}
empty_set = set()
print(type(empty_set)) #output: <class 'set'>
empty_dict = {}
print(type(empty_dict)) #output: <class 'dict'>

#set methods
s.add(343)
print(s) #output: {1, 2, 3, 4, 5, 343, "harry"}
s.remove(5)
print(s) #output: {1, 2, 3, 4, 343, "harry"}
s.clear()
print(s) #output: set()




