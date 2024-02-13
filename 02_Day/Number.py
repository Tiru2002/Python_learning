# Number are three  types of numbers:
"""
1. Integer - A number that is not a fraction and does not have a decimal point
2. Float - A number that has a decimal point 
3. complex- A number with both real and imaginary parts
"""

x=1 #int
y=5.5 #float
z=2j #complex

#verfing  the type of a variable using built in function 'type()'

print("x:",type(x))
print("x:",type(y))
print("x:",type(z))


# converting  one data type to another using built in functions

# int -> float
a=float(x) # x is int
print("converted value of x to float : ",a)

# float -> int
b=int(y) # y is float
print("converted value of y to int : ", b)

#float -> complex
c=complex(y)  # y is float
print("converted value of y to complex : ", c)