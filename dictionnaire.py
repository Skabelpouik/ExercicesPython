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
    
#%%
# Mountain Heights 3
mountains_feet = {"Mount Everest": [8848, 29029],
                  "Mont Blanc": [4810,15781],
                  "Gasherbrum III": [7952, 26089],
                  "Aconcagua": [6962, 22841],
                  "Mount Logan": [5959, 19551]}
for mountain in mountains_feet:
    print(mountain)
for mountain in mountains_feet.values():
    print(str(mountain[0]) + " meters")
for mountain in mountains_feet.values():
    print(str(mountain[1]) + " feet")
for mountain in mountains_feet:
    print("%s is %d meters tall, or %d feet." % (mountain, mountains_feet[mountain][0], mountains_feet[mountain][1]))

#%%
# Mountain Heights 4
mountains = {"Mount Everest": {"elevation": 8848, "range": "himalaya"},
             "Mont Blanc": {"elevation": 4810, "range": "alps"},
             "Gasherbrum III": {"elevation": 7952, "range": "karakoram"},
             "Aconcagua": {"elevation": 6962, "range": "andes"},
             "Mount Logan": {"elevation": 5959, "range": "saint elias mountains"}}
for mountain in mountains:
    print(mountain)
for mountain_info in mountains.values():
    print(mountain_info["elevation"])
for mountain_info in mountains.values():
    print(mountain_info["range"])
for mountain in mountains:
    print("%s is %d meters tall mountain in the %s range." % (mountain, mountains[mountain]["elevation"], mountains[mountain]["range"].title() ))

