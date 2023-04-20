import requests

api = 'https://superheroapi.com/api/'
Token = '2619421814940190/'

url_seach = api+Token+'/search/'

heroes =['Hulk', 'Captain America', 'Thanos']
intelligence_of_hero = {}
for hero in heroes:
    url = url_seach+hero
    param = requests.get(url = url).json()
    id = param['results'][0]['id']
    intelligence = param['results'][0]['powerstats']['intelligence']
    if intelligence_of_hero == {}:
        intelligence_of_hero = {'hero':hero,'id':id,'intelligence':intelligence}
    elif int(intelligence) > int(intelligence_of_hero['intelligence']):
        intelligence_of_hero = {'hero':hero,'id':id,'intelligence':intelligence}
    else:
        pass
print(f"Самым умным героем является {intelligence_of_hero['hero']}\n"
        f"его интелект равен {intelligence_of_hero['intelligence']}")
