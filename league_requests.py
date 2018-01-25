import requests
def nice(user_name):
    key='api_key=RGAPI-df4b4833-dbff-4e63-8e49-7a6669d7b015'
    user_name=user_name
    r=requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{0}?{1}'.format(user_name,key))
    ddragon=requests.get("http://ddragon.leagueoflegends.com/cdn/8.2.1/data/en_US/runesReforged.json")
    #print(r.json())
    summoner_id=r.json()['id']
    print(summoner_id)

    r=requests.get('https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{0}?{1}'.format(summoner_id,key))

    #from league api
    for counter in range(len(r.json()['participants'])):#could also just do enumerate without using second variable
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

    rune_name_order=[]
    rune_name_order.append((rune_name[2],rune_name[3],rune_name[4],rune_name[5],rune_name[0],rune_name[1]))
    return rune_name_order