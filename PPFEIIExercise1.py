"""
Created on Thu Jan 11 09:36:20 2024

Mary Kate Kenny
Programming for Everyone II
Exercise 1: Python, I Choose You!

"""
print()
print("Welcome to our Pokedex! What would you like to do?")
print("Search by NAME or REGION?")
searchID=input().upper()
#print(searchID)
print()

import pandas as pd 

"""Files
myPokemon is pokemon file
myEncounters is encounters file
myRegions is regions file
myLocations is locations file
"""
#myPokemon=open('Sheet 1-clean-pokemon.csv') 
#myEncounters=open('encounters.csv')
#myRegions=open('regions.csv')
#myLocations=open('locations csv.csv')

#use if statements depending on choice of name or region

#REQS: print name:xx,index:xx,locations:xx,min:xx,max:xx min/max for city
if searchID=="NAME":
    print("Which pokemon do you want to get info on?")
    pokeName=input().lower()
    myPokemon=open('/Users/marykate/Desktop/csc103/ex1/Sheet 1-clean-pokemon.csv')
    pokeInfo=myPokemon.read()
    if  pokeInfo.find(pokeName):
         print("Here's your info.")
         #read file to:
         #print name
         #search for index num, print it
         #search for locations, print them
         #search for  min and city, print it
         #search for max and city, print it
         myPokemon.close()
    
#REQS: present list of regions,choose reg,list cities in reg, choose, list poke there in alphabetical order
if searchID=="REGION":
    print("Which region do you want to get info on?")
    myRegions=open('/Users/marykate/Desktop/csc103/ex1/regions.csv')
    regInfo=myRegions.read()
    print(regInfo)
    print('Which region are you interested in?')
    pokeReg=input().lower()
    print('Which city/town do you want to look at?')
    citown=input().lower()
    myLocations=open('/Users/marykate/Desktop/csc103/ex1/locations csv.csv')
    locInfo=myLocations.read()
    print(locInfo)
        
    print("Here's your info.")
   # print(putinfohere)
    myRegions.close()
   