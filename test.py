import requests
import bs4

user_input=input("What champ")
link='http://www.probuilds.net/champions/details/%s'% user_input
test=requests.get(link).text

soup=bs4.BeautifulSoup(test,'html.parser')

ff=soup.find_all('div',{'class':'popular-section'})
counter=0
cool_list=[]
for x in ff:
    gg=x.find_all('div',{'class':'bigData'})
    for j in gg:
        if counter <6:
         cool_list.append(j.img.get('alt'))
         counter+=1
print(cool_list)