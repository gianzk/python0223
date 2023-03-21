import requests
url='https://pokeapi.co/api/v2/pokedex/1/'

data=requests.get(url).json()
listPokemon=data['pokemon_entries']
#print(type(listPokemon))

#print(listPokemon[0]['pokemon_species'])

for i,value in enumerate(listPokemon):
    name=value['pokemon_species']['name']
    print(i,"=>",name)
###apuntar los que participan

## hacer un buscador 
#urlDemo="https://pokeapi.co/api/v2/pokemon/bulbasaur"
url="https://pokeapi.co/api/v2/pokemon/"

msg="""
    1)listar pokemons
    2)buscar pokemon
        2.1)desea ver la url de la imagen
    """
