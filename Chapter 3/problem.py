#Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print(f"Good Afternoon {name} ")


#Write a program to fill in a letter template given below with name and date. 
#letter = '''  
#Dear <|Name|>, 
#You are selected! 
#<|Date|> 
#''' 

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Priyam").replace("<|Date|>", "25th of April"))

#Write a program to detect double space in a string.
name = "Priyam  is a  good boy"
print(name.find("  ")) #it will return the index of the first double space. if it is not found it will return -1

#Replace the double space from problem 3 with single space.
name = "Priyam  is a  good boy"
print(name.replace("  ", " "))
