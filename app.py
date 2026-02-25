# import json
# ## Open the JSON file of pokemon data
# pokedex = open("./pokedex.json", encoding="utf8")
# ## create variable "data" that represents the enitre pokedex list
# data = json.load(pokedex)
# print(data[8])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.



# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# def pick():
#     for poke in data:
#         print(poke['name']['english'])
# pick()



# Add a language choice feature and print the pokemons name based on the user input



# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# language = input("Pick a language")
# def pick():
#     for poke in data:
#         print(poke['name'][language])
# pick()



# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user



# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# x=809
# data = json.load(pokedex)
# poke_tpyes = input("What type?").lower().capitalize()
# for pokemon in data:
#     if poke_tpyes in pokemon['type']:
#         print(pokemon['name']['english'])
#     else:
#         x -= 1
#         if x == 0:
#             print("No Pokemon was found of that type.")

    

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 



# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# x = 809
# poke_name = input("What name are you searching for?").lower().capitalize()
# for pokemon in data:
#     if poke_name in pokemon['name']['english']:
#         print(pokemon['name']['english'])
#     else:
#         x -= 1
#         if x == 0:
#             print("No Pokemon was found.")



#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type


import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def pick():
    for poke in data:
        x = poke['name']['english']
        print(x)
pick()
