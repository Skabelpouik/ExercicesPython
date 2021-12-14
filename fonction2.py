# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:27:29 2021

@author: Peridot
"""
#%%
#Games
def likeGame(gameName="chess"):
    print("I like playing %s" % gameName)
    
likeGame("World Of Warcraft")
likeGame("Kena: Bridge of Spirits")
likeGame("The Elder Scrolls V: Skyrim")
likeGame()

#%%
#Favorite Movie
def likeMovie(movieName="The Princess Bride"):
    print("My favorite movie is %s." % movieName)
    
likeMovie("Star Wars: Return of the Jedi")
likeMovie("Lord of the Rings")
likeMovie()

#%%
#Favorite Colors
def favoriteColor(name="anonymous", color="blue"):
    print("%s's favorite color is %s." % (name.title(), color))
    
favoriteColor("fanny", "green")
favoriteColor("cookie", "red")
favoriteColor("ramina", "yellow")
favoriteColor()

#%%
#Phones
def modelPhone(brand="Nokia", model="3310"):
    print(brand + " " + model)
    
modelPhone("Iphone", "6 Plus")
modelPhone("OnePlus", "9 Pro")
modelPhone("Samsung", "Galaxy S21 Ultra")
modelPhone()

#%%
#Sports Teams
def sportsTeams(city, team):
    print(city + ": " + team)
    
sportsTeams(city ="New York", team ="Knicks")
sportsTeams( team = "Mavericks", city = "Dallas")
sportsTeams(team = "Jazz", city = "Utah")

#%%
#World Languages
def worldLanguages(country, language):
    print(country + ": " + language)
    
worldLanguages(country="France", language="Français")
worldLanguages(language="Français", country="Luxembourg")
worldLanguages(language="Chinese", country="China")