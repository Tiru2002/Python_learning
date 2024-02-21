# list

empty_list=list()
print(len(empty_list)) 

fruits = ['banana', 'orange', 'mango', 'lemon'] 
print(fruits)
print(len(fruits)) #length of list
print(fruits[2])#accessing the element at index 2 of the list, mango

#modifying list

fruits [0]= "apple"   #changing the first element 
print(fruits)
fruits[3]= "grape"    #adding a new element
print(fruits)

#checking iteams
check_fruits = "mango" in fruits     #check if an element is present or not
print(check_fruits)

#removing items from list
fruits.remove("orange") 
print(fruits)

#Append
fruits.append('banana')
print(fruits)

#insert
fruits.insert(1,'kiwi')
print(fruits)

#pop
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

#sort
fruits.sort()
print(fruits)

age=[25,18,19,22]
print(age)
age.sort()
print(age)

#join extend
num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
print(num1)
print(num2)
num2.extend(num1)
print(num2)

#clear
num1.clear()
print(num1)
fruits.clear()
print(len(fruits))