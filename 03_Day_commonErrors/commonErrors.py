# # # #1.SyntaxError:
# # # print "helloworld" #missing () parenthess is after print function

# # # #2.IndexError:

# # # l=[1,2,3,4]
# # # print(l[5])  #index out of range. The list has only four elements so the maximum index should be 3 not 5.

# # # #3.ModulNotFoundError:

# # # import notMoble #module named 'notMoble' is not a module

# # # #4.KeyError:

# # # d={'1':'a','2':'b'} 
# # # print(d['3'])   #key error as there is no key '3' in dictionary

# # # #5.ImportError:
# # # from math  import cube #function cube is not present in math module
# # #                         #so it will show ImportError: cannot import name 'cube' from 'math'


# # #6.stopIteration :
# # it=iter([1,2,3])
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))#after this line stop iteration error occurs because iterator is exhausted and we are trying to get next element


# #7.typeError:
# a=12+"12"
# print(a) # TypeError: can only concatenate str (not "int") to str

# # #8.valueError:
# # b=int('xyz')
# # print(b) # ValueError: invalid literal for int() 

# # #9.NameError:
# # print(age)  # NameError: name 'age' is not defined

# # #10.ZeroDivisionError:
# # num1 = 0/100; 
# # print(num1)

# #11.KeyBoardIntereuptError:
name=input("Enter your name: ") # if a click ctrl+c on keyboard interrupt button then it shows KeyboardInterrupt Error

