import requests
import bs4


class countering_champ:


    def grab_request(self):
        self.url_request=requests.get(self.url_link)

        self.url_text=self.url_request.text

        self.page_soup=bs4.BeautifulSoup(self.url_text,"html.parser")

        self.page=self.page_soup.find_all('div',{'class':'block3 _all'})

        for x in self.page:
            self.champ_block=x.find_all('div',{"class":"champ-block"})

            for counter,f in enumerate(self.champ_block):
                if counter <6:

                    self.champ_list.append(f.div['find'])
                else:
                    break



    def __init__(self,champ):
        self.champ=champ
        self.url_link = 'http://lolcounter.com/champions/%s'% self.champ
        self.champ_list=[]
        self.grab_request()
        print(self.champ_list)


