import requests
import json

print("Welcome to the Pokedex CLI!!!")

pokemonName = input("Which Pokemon do you want to search? ")

data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")

if data.status_code == 200:
    data = json.loads(data.text)

    print(f"You Chose {data['name']}!!!")

    action = input("What information would you like to see? \n (i = info, s = stats) ")

    if action == "i" or action == "info":
        print(f"id: {data['id']}")
        print(f"name: {data['name']}")
        print(f"height: {data['height']}")
        print(f"weight: {data['weight']}")
        pokemon_type = ""
        for type in data["types"]:
            if data["types"].index(type) == (len(data["types"]) - 1):\
                pokemon_type += f"{type['type']['name']}"
            else:
                pokemon_type += f"{type['type']['name']}, "
        print(f"type: {pokemon_type}")
    elif action == "s" or action =="stats":
        print(f"HP: {data['stats'][0]['base_stat']}")
        print(f"Attack: {data['stats'][1]['base_stat']}")
        print(f"Defense: {data['stats'][2]['base_stat']}")
        print(f"Speed: {data['stats'][5]['base_stat']}")
        print(f"Special Attack: {data['stats'][3]['base_stat']}")
        print(f"Special Defense: {data['stats'][4]['base_stat']}")
    

    else:
        print("Sorry we don't recognize that command")
else:
    print("Sorry that's not a valid pokemon")
#i = info, s = stats,
#name, id, weight, height, types of pokemon