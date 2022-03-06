import requests

Hulk = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
Captain_America = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain America')
Thanos = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')

Hulk_id = Hulk.json()['results'][0]['id']
Hulk_pow = requests.get(f'https://superheroapi.com/api/2619421814940190/{Hulk_id}/powerstats')
Hulk_int = int(Hulk_pow.json()['intelligence'])


Captain_America_id = Captain_America.json()['results'][0]['id']
Captain_America_pow = requests.get(f'https://superheroapi.com/api/2619421814940190/{Captain_America_id}/powerstats')
Captain_America_int = int(Captain_America_pow.json()['intelligence'])


Thanos_id = Thanos.json()['results'][0]['id']
Thanos_pow = requests.get(f'https://superheroapi.com/api/2619421814940190/{Thanos_id}/powerstats')
Thanos_int = int(Thanos_pow.json()['intelligence'])

heroes = (Hulk_pow.json(), Captain_America_pow.json(), Thanos_pow.json())
has_bb = max(Hulk_int, Captain_America_int, Thanos_int)

for b in heroes:
    if int(b['intelligence']) == has_bb:
        print(f'Самый умный: ', b['name'])


# print(Hulk_pow.json())
