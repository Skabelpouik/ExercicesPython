# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:44:09 2021

@author: Peridot
"""
#%%
important_words = ["variable", "list", "tuple", "loop"]
definitions = ["A variable holds a value. You can change the value of a variable at any point.", "A list is a collection of items, that is stored in a variable.", "Tuples are basically lists that can never be changed.", "A loop is a block of code that repeats itself until it runs out of items to work with, or until a certain condition is met."]
for word, definition in zip(important_words, definitions):
    print(word.title() + ": ")
    print(definition + "\n")
