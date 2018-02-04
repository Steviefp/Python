import requests


class summoner_wr:



    def obtain_account_id(self):
        self.account_id_json=requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{0}?api_key={1}".format(self.summoner_name,self.riot_key))
        self.account_id=self.account_id_json.json()['accountId']
        return self.account_id

    def obtain_game_Id(self):
        self.info_json=requests.get("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{0}/recent?api_key={1}".format(self.account_id,self.riot_key))
        for x in range(len(self.info_json.json()['matches'])):
            self.game_id_list.append(self.info_json.json()['matches'][x]['gameId'])


    def obtain_win(self):
        for x in range(len(self.game_id_list)):
            self.win_json=requests.get("https://na1.api.riotgames.com/lol/match/v3/matches/{0}?api_key={1}".format(self.game_id_list[x],self.riot_key))
            for y in range(len(self.win_json.json()['participantIdentities'])):

                if self.win_json.json()['participantIdentities'][y]['player']['accountId']==self.account_id:
                    self.game_win.append(self.win_json.json()["participants"][y]['stats']['win'])

        for x in self.game_win:
            if x:
                self.wins+=1


    def __init__(self,summoner_name,key):
        self.summoner_name = summoner_name
        self.riot_key = key
        self.game_id_list=[]
        self.game_win=[]
        self.wins=0
        self.win_rate="0%"
        self.obtain_account_id()
        self.obtain_game_Id()

        while len(self.game_id_list) > 10:
            self.game_id_list.pop()

        self.obtain_win()
        self.win_rate=str((self.wins/len(self.game_win)*100))+"%"
        return









# test=summoner_wr("steviefnibberp",key)
# 240859557