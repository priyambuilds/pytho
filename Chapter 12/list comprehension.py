list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squaredlist = []
# for item in list:
#     squaredlist.append(item**2)

# print(squaredlist)#output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# this can be done more efficiently using list comprehension.

squaredlist = [i for i in list]
print(squaredlist)#output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# this is more efficient because it is a one line code and it is more readable.


# we can also add conditions to the list comprehension.

squaredlist = [i for i in list if i%2 == 0]
print(squaredlist)#output: [2, 4, 6, 8, 10]

# we can also add multiple conditions to the list comprehension.

squaredlist = [i for i in list if i%2 == 0 and i%3 == 0]
print(squaredlist)#output: [6]