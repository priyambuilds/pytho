#strings is a collection of characters enclosed in double quotes
#strings are immutable
name = "priyam"

#string slicing
nameshort = len(name)
print(nameshort)

nameshort = name[0:3] #start from index 0 all the way till 3. 
print(nameshort) #output: pri
nameshort = name[0:6] #start from index 0 all the way till 6. 
print(nameshort) #output: priyam
nameshort = name[1:6] #start from index 1 all the way till 6. 
print(nameshort) #output: riyam

#positive indexing
name = "priyam"
print(name[0]) #output: p
print(name[1]) #output: r
print(name[2]) #output: i
print(name[3]) #output: y
print(name[4]) #output: a
print(name[5]) #output: m

#negative indexing
name = "priyam"
print(name[-1]) #output: m
print(name[-2]) #output: a
print(name[-3]) #output: y
print(name[-4]) #output: i
print(name[-5]) #output: r
print(name[-6]) #output: p  

print(name[-4:-1]) #output: iya
print(name[:4]) #output: priy. Its the same as print(name[0:4])
print(name[1:]) #output: riyam. Its the same as print(name[1:6])

#skipping characters
a = "0123456789"
print(a[0:10:2]) #output: 02468. It skips 1 character.
print(a[0:10:3]) #output: 0369. It skips 2 characters.
print(a[1:7:3]) #output: 14. It skips 2 characters. 1:7 means the numbers from 1-6. 3 means it skips 2 characters.
