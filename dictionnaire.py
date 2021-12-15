# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:00:58 2021

@author: Peridot
"""

#%%
# Pet Names
pets = {"Cookie": "rabbit",
        "Ramina": "cat",
        "Arachna": "spider"}
for pet_name, pet_type in pets.items():
    print("%s is a %s" % (pet_name, pet_type))
    
#%%
# Polling Friends
friends = {"Benji": "My favorite game is Final Fantasy VII",
           "Monia": "I don't play video games",
           "Valentin": "The best game ever is The Elder Scrolls V: Skyrim"}
for name, respond in friends.items():
    print("%s respond '%s'" % (name, respond))
    
#%%
# Pet Names 2
def print_dictionary(pet_list):
    for pet_name, pet_type in pets.items():
        print("%s is a %s" % (pet_name, pet_type))
        
pets = {"Cookie": "rabbit",
        "Ramina": "cat",
        "Arachna": "spider"}
print_dictionary(pets)
pets["Arachna"] = "frog"
print_dictionary(pets)
pets["Aragog"] = "spider"
print_dictionary(pets)
del pets["Arachna"]
print_dictionary(pets)

#%%
# Mountain Heights
mountains = {"Mount Everest": "8848m",
             "Mont Blanc": "4810m",
             "Gasherbrum III": "7952m",
             "Aconcagua": "6962m",
             "Mount Logan": "5959m"}
for mountain in mountains:
    print(mountain)
for mountain in mountains.values():
    print(mountain)
for mountain, elevation in mountains.items():
    print("%s is %s tall." % (mountain, elevation))
    
#%%
# Mountain Heights 2
mountains = {"Mount Everest": "8848m",
             "Mont Blanc": "4810m",
             "Gasherbrum III": "7952m",
             "Aconcagua": "6962m",
             "Mount Logan": "5959m"}
for mountain in mountains:
    print(mountain)
for mountain in mountains.values():
    print(mountain)
for mountain, elevation in sorted(mountains.items()):
    print("%s is %s tall." % (mountain, elevation))
    
