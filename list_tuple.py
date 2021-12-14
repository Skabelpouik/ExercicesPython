# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:00:04 2021

@author: Peridot
"""
#%%
#First List
languages = ["python", "c", "java"]
print(languages[0])
print(languages[1])
print(languages[2])

#%%
#First Neat List
languages = ["python", "c", "java"]
print("A nice programming language is " + languages[0])
print("A nice programming language is " + languages[1])
print("A nice programming language is " + languages[2])

#%%
#Your First List
vehicles = ["bike", "scooter", "car", "bus", "truck"]
print("I take the " + vehicles[3] + " to go to work.")

#%%
#First List - Loop
languages = ["python", "c", "java"]
for language in languages:
    print(language)

#%%
#First Neat List - Loop
languages = ["python", "c", "java"]
for language in languages:
    print("A nice programming language is " + language)
    
#%%
#Your First List - Loop
vehicles = ["bike", "scooter", "car", "bus", "truck"]
for vehicle in vehicles:
    print("I take the " + vehicle + " to go to work.")
    
#%%
#Working List
careers = ["actor", "programmer", "pet sitter", "teacher"]
print(careers.index("pet sitter"))
print("teacher" in careers)
careers.append("nurse")
careers.insert(0, "cooking chef")
for career in careers:
    print(career)

#%%
#Starting From Empty
careers = []
careers.append("cooking chef")
careers.append("actor")
careers.append("programmer")
careers.append("pet sitter")
careers.append("teacher")
careers.append("nurse")
print("The first career is " + careers[0])
print("The last career is " + careers[-1])

#%%
#Ordered Working List
careers = ["actor", "programmer", "pet sitter", "teacher"]
print("List in original order:")
for career in careers:
    print(career)
print("List in alphabetical order:")
for career in sorted(careers):
    print(career)
print("List in original order:")
for career in careers:
    print(career)
print("List in reverse alphabetical order:")
for career in sorted(careers, reverse=True):
    print(career)
print("List in original order:")
for career in careers:
    print(career)
print("List in the reverse order from what it started:")
careers.reverse()
for career in careers:
    print(career)
print("List in original order:")
careers.reverse()
for career in careers:
    print(career)
print("List in alphabetical order:")
careers.sort()
for career in careers:
    print(career)
print("List in reverse alphabetical order:")
careers.sort(reverse=True)
for career in careers:
    print(career)
   
#%%
#Ordered Numbers
numbers = [4, 7, 9, 2, 6]
print("Numbers in original order:")
for number in numbers:
    print(number)
print("Numbers in increasing order:")
for number in sorted(numbers):
    print(number)
print("Numbers in original order:")
for number in numbers:
    print(number)
print("Numbers in decresing order:")
for number in sorted(numbers, reverse=True):
    print(number)
print("Numbers in original order:")
for number in numbers:
    print(number)
print("Numbers in the reverse order from what it started:")
numbers.reverse()
for number in numbers:
    print(number)
print("Numbers in the original order:")
numbers.reverse()
for number in numbers:
    print(number)
print("Number in increasing order:")
numbers.sort()
for number in numbers:
    print(number)
print("Numbers in decreasing order:")
numbers.sort(reverse=True)
for number in numbers:
    print(number)

#%%    
#List Lengths
numbers = [4, 7, 9, 2, 6]    
careers = ["actor", "programmer", "pet sitter", "teacher"] 
vehicles = ["bike", "scooter", "car", "bus", "truck"]
print("The list has " + str(len(numbers)) + " numbers.")
print("There is " + str(len(careers)) + " careers in the list.")
print("There is " + str(len(vehicles)) + " vehicles in the list.")

#%%
#Famous People
peoples = ["Mylène Farmer", "Hayao Miyazaki", "Darth Vader", "Bibi"]
peoples.pop()
peoples.pop(1)
del peoples[0]
peoples.remove("Darth Vader")
print("There are no famous people in this list")
print(peoples)

#%%
#Alphabet Slices
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(alphabet[:3])
print(alphabet[3:6])
print(alphabet[5:])

#%%
#Protected List
peoples = ["Mylène Farmer", "Hayao Miyazaki", "Darth Vader"]
peoples_copy = peoples[:]
peoples_copy.append("Bibi")
peoples_copy.append("Winnie the Pooh")
print("It's the original list:")
for people in peoples:
    print(people)
print("It's the copied list:")
for people in peoples_copy:
    print(people)
    
#%%
#First Twenty
numbers = list(range(1, 21))
for number in numbers:
    print(number)

#%%
#Largest Sets
numbers = list(range(1, 10001))
for number in numbers:
    print(number)

#%%
#Five Wallets
wallets = [34, 67, 2, 13, 21]
print("The fattest wallet has " + str(max(wallets)) + " $")
print("The skinniest wallet has " + str(min(wallets)) + " $")
print("All together, these wallets have " + str(sum(wallets)) + " $")

#%%
#Multiples of Ten
numbers = [number*10 for number in range(1, 11)]
for number in numbers:
    print(number)
    
#%%
#Cubes
numbers = [number**3 for number in range(1, 11)]
for number in numbers:
    print(number)

#%%
#Awesomeness
peoples = ["Mylène Farmer", "Hayao Miyazaki", "Darth Vader", "Bibi", "Winnie the Pooh"]
great_peoples = [people + " the great!" for people in peoples]
for people in great_peoples:
    print(people)

#%%
#Working Backwards
plus_thirteen = []
for number in range(1, 11):
    plus_thirteen.append(number + 13)
for number in plus_thirteen:
    print(number)
    
#%%
#Listing a Sentence
sentence = "There is no try"
for letter in sentence:
    print(letter)
    
#%%
#Sentence List
sentence = "There is no try"
sentence_list = list(sentence)
print(sentence_list)

#%%
#Sentence Slices
sentence = "Store a single sentence in a variable. Create a list from your sentence."
print(sentence[:6])
print(sentence[9:14])
print(sentence[-5:])

#%%
#Finding Python
sentence = "You can read this file into your Python program. Python is a great language."
print("Python" in sentence)
print(sentence.find("Python"))
print(sentence.rfind("Python"))
print(sentence.count("Python"))
words_list = sentence.split(" ")
for word in words_list:
    print(word)
print(sentence.replace("Python", "Ruby"))

#%%
#Gymnast Scrores
scores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("The lowest possible score is %d, and the highest possible score is %d." % (scores[0], scores[-1]))
for score in scores:
    print("A judge can give a gymnast %d points" % score)
