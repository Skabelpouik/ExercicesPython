# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:44:42 2021

@author: Peridot
"""

#Alien Points
aliens = ["red", "blue", "green", "red", "green", "blue", "red", "green", "green", "blue"]
current_score = 0
for alien in aliens:
    if alien == "red":
        current_score = current_score + 5
    elif alien == "green":
        current_score = current_score + 10
    else:
        current_score = current_score + 20
print("The player earn %d points for destroying all of the aliens in your list" % current_score)