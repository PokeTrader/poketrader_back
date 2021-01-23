import os
import requests


def fetch_pokemon(name):
    base_url = os.getenv('POKEAPI_BASE_URL')
    response = requests.get("%s/pokemon/%s" % (base_url, name))
    if response.status_code == 200:
        data = response.json()
        return {
            'id': data['id'],
            'name': data['name'],
            'base_exp': data['base_experience'],
            'sprite': data['sprites'].get('front_default')
        }
    else:
        return None