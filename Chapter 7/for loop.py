# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

#the same can be done using loops

#for loop. for loop is used to repeat a block of code a specific number of times.
for i in range(1,6):
    print(i) #output: 1 2 3 4 5

#step size. the third argument in the range function is the step size.
for i in range(1, 100, 4):
    print(i) #output: 1 5 9 13 17 21 25 29 33 37 41 45 49 53 57 61 65 69 73 77 81 85 89 93 97

#iteration using for loop
list = [1, 2, 3, 4, 5, 34, 455, 45]
for i in list:
    print(i) #output: 1 2 3 4 5 34 455 45

tuple = (1, 2, 3, 4, 5, 34, 455, 45)
for i in tuple:
    print(i) #output: 1 2 3 4 5 34 455 45

string = "priyam"
for i in string:
    print(i) #output: p r i y a m

#iteration using for loop

# for loop with else
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    print(i)
else:
    print("done") #output: 1 2 3 4 5 6 7 8 9 10 done

#break statement
for i in range(1, 100):
    if i == 17:
        break #exit the loop right now.
    print(i) #output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

#continue statement
for i in range(1, 35):
    if i == 17: 
        continue #skip the current iteration.
    print(i) #output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34. it skips 17.

#pass statement
for i in range(645):
    pass #pass statement is used to do nothing. it is used to avoid errors.

i = 0
while(i<645):
    print(i)
    i += 1





