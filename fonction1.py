# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:46:10 2021

@author: Peridot
"""
#%%
#Greeter
def greetingPeople(name):
        print("Hi %s!" % name)
        print("Your name is %s and I am very happy to welcome you on board" % name)
        print("See what can you do on this website %s" % name)
        

names = ["Fanny", "Emilie", "Cookie", "Ramina"]
for name in names:
    greetingPeople(name)

#%%
#Full Names
def fullName(firstName, lastName):
    print("Hello, %s %s!" % (firstName, lastName))
    
fullName("Fanny", "Scheltgen")
fullName("Mylène", "Farmer")
fullName("Hayao", "Miyazaki")

#%%
#Addition Calculator
def addNumbers(firstNumber, secondNumber):
    result = firstNumber + secondNumber
    print("The addition of %d and %d is: %d" % (firstNumber, secondNumber, result))
    
addNumbers(3, 2) 
addNumbers(6, 4)
addNumbers(4, 3)

#%%
#Return Calculator
def addNumbers(firstNumber, secondNumber):
    return firstNumber + secondNumber
    
print("The result of the sum of 3 and 2 is %d" % addNumbers(3, 2))

#%%
#Ordered Working List - Functions
def original(careers):
    print("List in original order:")
    for career in careers:
        print(career)

def increase(careers):
    print("List in alphabetical order:")
    for career in sorted(careers):
        print(career)
        
def decrease(careers):
    print("List in reverse alphabetical order:")
    for career in sorted(careers, reverse=True):
        print(career)
        
def reverse_list(careers):
    careers.reverse()
    for career in careers:
        print(career)
        
def increasePermanently(careers):
    careers.sort()
    print("List in alphabetical order:")
    for career in careers:
        print(career)
        
def decreasePermanently(careers):
    careers.sort(reverse=True)
    print("List in reverse alphabetical order:")
    for career in careers:
        print(career)
        
careers = ["actor", "programmer", "pet sitter", "teacher"]
original(careers)
increase(careers)
original(careers)
decrease(careers)
original(careers)
print("List in reverse alphabetical order from what it started:")
reverse_list(careers)
print("List in original order:")
reverse_list(careers)
increasePermanently(careers)
decreasePermanently(careers)

#%%
#Ordered Numbers - Functions
def original(numbers_list):
    print("Numbers in original order:")
    for number in numbers_list:
        print(number)

def increase(numbers_list):
    print("Numbers in increasing order:")
    for number in sorted(numbers_list):
        print(number)
        
def decrease(numbers_list):
    print("Numbers in decreasing order:")
    for number in sorted(numbers_list, reverse=True):
        print(number)
        
def reverse_list(numbers_list):
    numbers_list.reverse()
    for number in numbers_list:
        print(number)
        
def increasePermanently(numbers_list):
    numbers_list.sort()
    print("Numbers in increasing order:")
    for number in numbers_list:
        print(number)
        
def decreasePermanently(numbers_list):
    numbers_list.sort(reverse=True)
    print("Numbers in decreasing order:")
    for number in numbers_list:
        print(number)
        
numbers_list = [4, 7, 9, 2, 6]
original(numbers_list)
increase(numbers_list)
original(numbers_list)
decrease(numbers_list)
original(numbers_list)
print("Numbers in the reverse order from what it started:")
reverse_list(numbers_list)
print("Numbers in original order:")
reverse_list(numbers_list)
increasePermanently(numbers_list)
decreasePermanently(numbers_list)