
letter="hello World"

#capitalize
print(letter.capitalize()) 

#Upper
print(letter.upper()) 

#lower
print(letter.lower())

#Find
print("World".find('o'))  
print(letter.find('l'))

#split
print(letter.split())  

#join
print("-".join(letter))  

#replace
print(letter.replace('W', 'X'))   

#count
print(letter.count('o'))    
print(letter.count('l'))

#isalnum
print(letter.isalnum())

#format
num=len(letter)
new_letter=(f"The Index value of {letter} is {num}.")
print(new_letter)

#strip
name= "      tiru           "
print(name)
print(name.strip())

#swapcase():
print(letter.swapcase())

#startswith
print(letter.startswith('hello'))
print(letter.startswith('world'))
print(letter.startswith('h'))

