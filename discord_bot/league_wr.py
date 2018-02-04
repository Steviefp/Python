import requests
import json
import urllib.request




def obtain_id(user_name,key):
    user_name = user_name
    account_request = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{0}?api_key={1}'.format(user_name, key))
    account_id=account_request.json()['accountId']
    print(account_id)
    return account_id

def obtain_champion(champion_name,key):
    champion_name=champion_name
    urllib.request.urlretrieve('https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&dataById=false&api_key=%s'%key,"champions.json")
    champion_request=open("champions.json","r")
    champion_request=json.load(champion_request)
    champion_id=champion_request['data'][champion_name]['id']
    return champion_id

def obtain_game_id(champion_id,account_id,game_id_list,key):
    champion_id=champion_id
    account_id=account_id
   # game_id_request=requests.get("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{0}?queue=440&season=11&champion={1}&{2}".format(account_id,champion_id,key))
    urllib.request.urlretrieve("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{0}?queue=420&season=11&champion={1}&api_key={2}".format(account_id,champion_id,key),"game_id.json")
    game_id_request_file=open("game_id.json","r")
    game_id_request_json=json.load(game_id_request_file)

    for a in range(len(game_id_request_json['matches'])):
        if game_id_request_json['matches'][a]['champion']==champion_id:
            game_id_list.append(game_id_request_json['matches'][a]['gameId'])


    urllib.request.urlretrieve("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{0}?queue=440&season=11&champion={1}&api_key={2}".format(account_id,champion_id,key),"game_id.json")
    game_id_request_file=open("game_id.json","r")
    game_id_request_json=json.load(game_id_request_file)

    for a in range(len(game_id_request_json['matches'])):
        if game_id_request_json['matches'][a]['champion'] == champion_id:
            game_id_list.append(game_id_request_json['matches'][a]['gameId'])

def obtain_win(champion_id,game_state_list,game_id_list,key):
    champion_id=champion_id
    for b in range(len(game_id_list)):
        game_state=requests.get("https://na1.api.riotgames.com/lol/match/v3/matches/{0}?api_key={1}".format(game_id_list[b],key))
        game_state_json=game_state.json()

        for counter,x in enumerate(game_state_json["participants"]):
            if game_state_json["participants"][counter]['championId']==champion_id:
                game_state_list.append(game_state_json["participants"][counter]['stats']['win'])

def obtain_ratio(game_state_list):
    wins=0
    for counter in range(len(game_state_list)):
        if game_state_list[counter]==True:
            wins+=1
    ratio=wins/len(game_state_list)*100
    return ratio



def main(user_name,champion_name,key):
    key=key
    game_id_list = []
    game_state_list = []
    user_name=user_name
    champion_name=champion_name
    account_id=obtain_id(user_name,key)
    champion_id=obtain_champion(champion_name,key)
    obtain_game_id(champion_id,account_id,game_id_list,key)
    print(game_id_list)
    obtain_win(champion_id,game_state_list,game_id_list,key)
    print(game_state_list)
    ratio=obtain_ratio(game_state_list)
    print(ratio)
    print("len of game_id_list",len(game_id_list))
    return ratio


