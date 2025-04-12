# dictionaries are used to store a list of key-value pairs.
#properties of dictionaries:
#1. Dictionaries are unordered.
#2. Dictionaries are mutable.
#3. Dictionaries are indexed.
#4. Dictionaries cannot contain duplicate keys.

marks = {"rohan": 56, "aakash": 45, "aayush": 78}
print(marks, type(marks))
print(marks["rohan"]) #output: 56

#dictionary methods
print(marks.items()) #output: dict_items([('rohan', 56), ('aakash', 45), ('aayush', 78)])
print(marks.keys()) #output: dict_keys(['rohan', 'aakash', 'aayush'])
print(marks.values()) #output: dict_values([56, 45, 78])
marks.update({"aayush": 80, "akansha": 90})
print(marks) #output: {'rohan': 56, 'aakash': 45, 'aayush': 80}

print(marks.get("aayush1")) #output: None
print(marks["aayush1"]) #output: KeyError: 'aayush1'

print(marks.pop("aayush")) #it removes the key-value pair from the dictionary
print(marks) #output: {'rohan': 56, 'aakash': 45}







