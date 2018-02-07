import requests
import bs4

url_link='http://lolcounter.com/champions/annie'
url=requests.get(url_link)

text=url.text

page_soup= bs4.BeautifulSoup(text,"html.parser")


coollist=[]

testing=page_soup.find_all('div',{'class':'block3 _all'})
counter=0
for x in testing:
    cool=x.find_all('div',{"class":"champ-block"})
    for f in cool:
        if counter<6:
            coollist.append(f.div)
            counter+=1
        else:
            break

for x in coollist:
    print(x)