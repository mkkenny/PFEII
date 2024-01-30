
"""
Mary Kate Kenny
Programming for Everyone II
Exercise 2: Pandas, I Choose You!
"""

print()
print("Welcome to our Pokedex! What would you like to do?")
print("Search by NAME or REGION?")
searchID=input().upper()
print()

import pandas as pd

#for name:
    #want to merge all data frames with name, index, locations,minplacelevel, maxplacelevel, moveset data
    #then when user inputs name, seach merged df for name to provide all info
    
#for region:
    #print regions, user inputs reg, search locations.csv for input
    #merge pokemon and encounters, find pokemon form merged df, print poke in alphabetical order

poke = pd.read_csv("/Users/marykate/Desktop/csc103/ex2/data/orig/pokemon.csv")

moves = pd.read_csv("/Users/marykate/Desktop/csc103/ex2/data/orig/moves.csv")

pokemoves = poke.merge(moves,how='left',left_on='id',right_on='generation_id', suffixes=('_poke','_pokemoves'))
pokemoves.to_csv('/Users/marykate/Desktop/csc103/ex2/data/clean/pokemoves.csv')

#for name: provide name, index, locations,minplacelevel, maxplacelevel, moveset

if searchID=="NAME":
    print("Which pokemon do you want to get info on?")
    pokeName=input().lower()
    #merge encounters.csv to pokemoves to add min/max levels 
    #read encounters.csv in with pandas
    enc=pd.read_csv("/Users/marykate/Desktop/csc103/ex2/data/orig/encounters.csv")
    pme=pokemoves.merge(enc,how='left',left_on='min_level',right_on='max_level', suffixes=('_enc','_pokemovesenc'))
    pme.to_csv('/Users/marykate/Desktop/csc103/ex2/data/clean/pokemovesenc.csv')
    #i want it to only print the info for the pokemon the user inputs, but i can't figure out the syntax :(
    print(pme[['identifier_poke','species_id','power']].where(pme['identifier_poke']==pokeName).drop_duplicates().dropna().sort_values(by=["power"],ascending=False).head(4).groupby('identifier_poke').agg({'species_id': lambda x: ', '.join(x),}).reset_index().rename(columns={'identifier_poke': 'Name', 'identifier_d': 'Attacks','min_level': 'Min. Level','max_level': 'Max. Level'}))

   # print(pokemoves[['identifier_poke','species_id','identifier_pokemoves','power']].where(pokemoves['identifier_poke']==pokeName).drop_duplicates().dropna().sort_values(by=["power"],ascending=False).head(4).groupby('identifier_poke').agg({'species_id': lambda x: ', '.join(x),}).reset_index().rename(columns={'identifier_poke': 'Name', 'identifier_d': 'Attacks'}))
               #pmd[['identifier_pm','identifier_d','power']].where(pmd['identifier_pm']=='pikachu').drop_duplicates().dropna().sort_values(by=["power"],ascending=False).head(4).groupby('identifier_pm').agg({'identifier_d': lambda x: ', '.join(x),}).reset_index().rename(columns={'identifier_pm': 'Name', 'identifier_d': 'Attacks'})

    condition = (pokemoves['species_id']==pokeName)
    pokesqt = pokemoves[condition]

    condition = (pokemoves['identifier_poke']==pokeName)

    pokesqt = pokemoves[condition]

    pokesqt.head(4)
    #search for pokeName in column
    #print row with name, index, locations,minplacelevel, maxplacelevel, moveset
    
   #condition = (pokemoves['species_id']=='squirtle')
   #squirt = pokemoves[condition]

   #condition = (pokemoves['identifier_poke']=='squirtle')

   #squirt = pokemoves[condition]

   #squirt.head(4) 
   #--------------------------------------------------------
   #condition = (pokemoves['species_id']==pokeName)
   #pokesqt = pokemoves[condition]

   #condition = (pokemoves['identifier_poke']==pokeName)

  # pokesqt = pokemoves[condition]

  # pokesqt.head(4) 
   
if searchID=="REGION":
    
    print("Which region do you want to get info on? Type the number.")
    myRegions=open('/Users/marykate/Desktop/csc103/ex1/regions.csv')
    regInfo=myRegions.read()
    print(regInfo)
    pokeRegid=input().lower()
    print('Which city/town do you want to look at?')
    
    
    
    #need to clean up locations first
    #making new clean file with 'Special Event'
    l=pd.read_csv('/Users/marykate/Desktop/csc103/ex2/data/orig/locations.csv')
    l.loc[l['region_id'].isnull()]
    l['region_id'].fillna('Special Event',inplace=True)
    l.to_csv('/Users/marykate/Desktop/csc103/ex2/data/clean/locations.csv')
    
    #open locations.csv, read it, print 'identifier' column with no duplicates
    print(l.drop_duplicates())#only print where region_id=user input
    myCitown=open('/Users/marykate/Desktop/csc103/ex2/data/clean/locations.csv')
    citinfo=myCitown.read()
    citown=input().lower()
    print(citinfo[['identifier']].where(citinfo['identifier']==citown).drop_duplicates()) #only print for city/town user inputs
    print()
    
    # merge clean locations with file that matches pokemon to city/town, but can't find??
      
  


