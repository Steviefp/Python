import requests
import bs4



class champsgg_runes:

    def request_runes(self):

        self.rune_request=requests.get(self.link).text

        self.rune_soup=bs4.BeautifulSoup(self.rune_request,'html.parser')

        self.rune_find=self.rune_soup.find_all('div',{'class':'Description__Block-bJdjrS hGZpqL'})

        for x in self.rune_find:
            if self.counter < 8:
                self.runes_win.append(x.div.text)
                self.counter+=1
            else:
                self.runes_freq.append(x.div.text)


    def __init__(self,champ):
        self.counter=0
        self.runes_win=[]
        self.runes_freq=[]
        self.link='http://champion.gg/champion/%s' % champ

        self.request_runes()

        self.runes_win.pop(0)
        self.runes_win.pop(4)

        self.runes_freq.pop(0)
        self.runes_freq.pop(4)


