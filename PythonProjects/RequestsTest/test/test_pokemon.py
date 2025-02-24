import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1f0dcbf4804e3e1780ce365ff0f1f038'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22493'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer():
    response_trainer = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer.json()['data'][0]['trainer_name'] == 'Менсен'