list = [1, 2, 3, 4 , 545 ,354]
# index = 0
# for i in list:
#     print(f"the item number {index} is {i}")
#     index += 1

# this can be done more efficiently using enumerate.

for index, i in enumerate(list):
    print(f"the item number at indec {index} is {i}")

#output:
# the item number at index 0 is 1
# the item number at index 1 is 2
# the item number at index 2 is 3
# the item number at index 3 is 4
# the item number at index 4 is 545
# the item number at index 5 is 354

