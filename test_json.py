# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:32:35 2021

@author: Peridot
"""
#%%
# Convertir un dictionnaire python en  JSON avec la fonction json.dumps()
import json

dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"}

json_object = json.dumps(dictionary, indent = 4)
print(json_object)

#%%
# Convertir un dictionnaire python en fichier JSON avec la fonction json.dump()
import json

dictionary = {
    "name" : "sathiyajith",  
    "rollno" : 56,  
    "cgpa" : 8.6,  
    "phonenumber" : "9976770500"
    }

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
    
#%%
# Convertir un fichier JSON en dictionnaire Python grace à la fonction json.load()
import json

with open("sample.json") as json_file:
    data = json.load(json_file)
    
print("Type", type(data))

print("\nPeople1:", data["people1"])
print("\nPeople2:", data["people2"])