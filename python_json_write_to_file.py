import json
import requests
import os
class json_write:



    def file_write(self):

        self.link_json=requests.get(self.link)




        self.link_info=self.link_json.json()

        self.file.writelines(json.dumps(self.link_info,indent=4, sort_keys=True))
        self.file.close()
        print("REEE")

    def file_delete(self):
        os.remove(self.file_name)
        print("STOP")

    def __init__(self,link):
        self.request_state=True
        self.link=link
        self.file_name = 'json_bot'
        self.file_name=self.file_name+".json"
        self.file=open(self.file_name,"w")








