import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1f0dcbf4804e3e1780ce365ff0f1f038'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
creat_body = {
    "name": "Арни",
    "photo_id": 943
}

create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = creat_body)
print(create.text)

POKEMON_ID = create.json()['id']
print(POKEMON_ID)

change_body = {
    "pokemon_id": POKEMON_ID,
    "name": "НовыйАрни",
    "photo_id": 941
}

change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_body)
print(change.text)

catch_body = {
    "pokemon_id": POKEMON_ID
}

catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_body)
print(catch.text)

list = requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'attack': '1', 'in_pokeball': '1', 'status' : '1'})
print(list.text)

ENEMY_ID = list.json()['data'][1]['id']
print(ENEMY_ID)

battle_body = {
    "attacking_pokemon": POKEMON_ID,
    "defending_pokemon": ENEMY_ID
}

battle = requests.post(url = f'{URL}/battle', headers = HEADER, json = battle_body)
print(battle.text)