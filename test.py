import requests
import json


key='api_key=RGAPI-111d98ef-6312-4779-9f1c-80d89b0ccb17'

def obtain_id(user_name):
    user_name = user_name
    account_request = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{0}?{1}'.format(user_name, key))
    account_id=account_request.json()['accountId']
    print(account_id)
    return account_id

user_name="Steviefnibberp"
account_id=obtain_id(user_name)
print(account_id)
