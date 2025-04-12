s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 10}
print(s1.union(s2)) #output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s1.intersection(s2)) #output: set()
print(s1.difference(s2)) #output: {1, 2, 3, 4, 5}
print(s1.symmetric_difference(s2)) #output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 
print(s1.isdisjoint(s2)) #output: False
print(s1.issubset(s2)) #output: False
print(s1.issuperset(s2)) #output: False 










