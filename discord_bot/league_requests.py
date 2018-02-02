import requests
def nice(user_name):
    # This is riot api key
    key='api_key=RGAPI-0a0ed530-0062-4aea-a99d-945976ecfec4'
    # this is discord input
    user_name=user_name
    # I grab from riot api summoners id from summoner name which is the user_name
    r=requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{0}?{1}'.format(user_name,key))
    # ddragon runesReforged.json, this is my only way I could get rune names from rune id
    ddragon=requests.get("http://ddragon.leagueoflegends.com/cdn/8.2.1/data/en_US/runesReforged.json")

    summoner_id=r.json()['id']
    print(summoner_id)

    # I change my request to spectator after I get the summoner Id.
    r=requests.get('https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{0}?{1}'.format(summoner_id,key))

    # From riot api
    # I use bunch of nested loops to get through all the json.
    for counter in range(len(r.json()['participants'])): # could also just do enumerate without using second variable
        for x in r.json()['participants'][counter]:
            if r.json()['participants'][counter][x]==summoner_id:
                rune_list=r.json()['participants'][counter]['perks']['perkIds']


    print(rune_list)
    rune_name=[]

    #from ddragon api thingy

    for x in range(len(ddragon.json())):
        for c,d in enumerate(ddragon.json()[x]['slots']):
            for g,h in enumerate(ddragon.json()[x]['slots'][c]['runes']):
                if ddragon.json()[x]['slots'][c]['runes'][g]['id']in rune_list:
                    rune_name.append(ddragon.json()[x]['slots'][c]['runes'][g]['name'])

                # print(ddragon.json()[x]['slots'][c]['runes'][g]['name'])
                # print(ddragon.json()[x]['slots'][c]['runes'][g]['id'])


    return rune_name