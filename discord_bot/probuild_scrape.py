
import requests
import bs4



class probuild:

    def request_probuild(self):



    def __init__(self,champ):

        self.champ=champ
        self.link='http://www.probuilds.net/champions/details/%s' % champ
        self.item_list=[]
        self.request_probuild()


coolchamp='annie'

tset=probuild(coolchamp)