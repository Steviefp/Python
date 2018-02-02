import json
import requests

import urllib.request

class json_write:



    def file_write(self):
        self.link_json=requests.get(link)

        self.link_info=self.link_json.json()

        self.file.writelines(json.dumps(self.link_info,indent=4, sort_keys=True))

    def __init__(self,link,file_name):
        self.link=link
        self.file_name=file_name+".json"
        print(self.file_name)
        self.file=open(self.file_name,"w")
        self.file_write()



file_name=input("What do you want the file to be named?: ")
link=input("paste link: ")
file1=json_write(link,file_name)


