#unlike strings, lists are mutable.
friends = ["apple", "orange", 5, 334.56, False, "aakash", "rohan"]
#list slicing
print(friends[0]) #output: apple
print(friends[0:4]) #output: apple, orange, 5, 334.56
print(friends[-4:]) #output: 5, 334.56, False, aakash 

#list methods
l1 = [1, 6, 2, 56, 765, 46, 787, 12, 49, 10]
print(l1)
l1.sort() #output: [1, 2, 6, 10, 12, 46, 49, 56, 765, 787]
print(l1)
l1.reverse() #output: [787, 765, 56, 49, 12, 10, 6, 2, 1]
print(l1)
l1.append(45) #output: [1, 2, 6, 10, 12, 46, 49, 56, 765, 787, 45] adds 45 at the end of the list
print(l1)
l1.insert(0, 544) #output: [544, 1, 2, 6, 10, 12, 46, 49, 56, 765, 787, 45] adds 544 at the index 0.
print(l1)
l1.pop(2) #output: [544, 1, 6, 10, 12, 46, 49, 56, 765, 787, 45] removes the element at index 2.
print(l1)
l1.remove(12) #output: [544, 1, 6, 10, 46, 49, 56, 765, 787, 45] removes 12 from the list.
print(l1)
l1.pop() #output: [544, 1, 6, 10, 46, 49, 56, 765, 787] removes the last element from the list.
print(l1)
l1.clear() #output: [] clears the list.
print(l1)
#every time the entire list will be changed.
















