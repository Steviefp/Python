import bs4
import requests


class probuild_pop:


    def pop_request(self):
        html=requests.get(self.link).text

        self.soup=bs4.BeautifulSoup(html,'html.parser')

        self.soup=self.soup.find_all('div',{'class':'popular-section'})

        for x in self.soup:
            self.second_soup = x.find_all('div', {'class': 'bigData'})
            for a in self.second_soup:
                if self.counter < 6:
                    self.item_list.append(a.img.get('alt'))
                    self.counter+=1




    def __init__(self,champ):
        self.counter=0
        self.champ=champ
        self.link='http://www.probuilds.net/champions/details/%s' % self.champ
        self.item_list=[]

        self.pop_request()





