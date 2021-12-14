# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:29:19 2021

@author: Peridot
"""
#%%
# True or False
print(5==5)
print(5<6)
print(3<=3)
print(3>2)
print(7>=7)
print(3==5)
print(3!=3)
print(6>8)
print("6"==6)
print("g" in ["a", "b", "c"])

#%%
# Three is a Crowd
def crowd_test(name_list):
    if len(names) > 3:
        print("The room is crowded!")
        
names = ["Fanny", "Cookie", "Ramina", "Emilie"]
crowd_test(names)
del names[2:]
crowd_test(names)

#%%
# Three is Crowd - Part 2
def crowd_test(name_list):
    if len(names) > 3:
        print("The room is crowded!")
    else:
        print("The room is not very crowded!")
        
names = ["Fanny", "Cookie", "Ramina", "Emilie"]
crowd_test(names)
del names[2:]
crowd_test(names)

#%%
# Six is a Mob
def crowd_test(name_list):
    if len(names) > 5:
        print("There is a mob in the room!")
    elif len(names) > 3:
        print("The room is crowded!")
    elif len(names) > 0:
        print("The room is not very crowded!")
    else:
        print("The room is empty!")
        
names = ["Fanny", "Cookie", "Ramina", "Emilie", "Benjamin", "Monia"]
crowd_test(names)
del names[-2:]
crowd_test(names)
del names[-2:]
crowd_test(names)
del names[-2:]
crowd_test(names)