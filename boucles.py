# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:26:00 2021

@author: Peridot
"""

#%%
# Growing Strength
strength = 5
print("The player's strength is %s" % strength)
while strength <= 10:
    print("Now the player's strength is %s" % strength)
    strength += 1
print("The player has grown too strong, he passed to the next level of the game.")

#%%
# Game Preferences
games = ["World of Warcraft", "Kena: Bridge of Spirits", "The Elder Scrolls V: Skyrim"]
for game in games:
    print("I like to play %s" % game)
new_game = input("Please tell me a game you like to play: ")
games.append(new_game)
for game in games:
    print("We like to play %s" % game)

#%%
# Many Games
games = ["World of Warcraft", "Kena: Bridge of Spirits", "The Elder Scrolls V: Skyrim"]
for game in games:
    print("I like to play %s" % game)
new_game = ""
while new_game != "quit":
    new_game = input("Please tell me a game you like to play, or enter 'quit': ")
    if new_game != "quit":
        games.append(new_game)
for game in games:
    print("\nquitWe like to play %s" % game)
    
#%%
# Marveling at Infinity !!!!WARNING INFINITE LOOP!!!!
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number -= 1