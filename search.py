import os
import requests

class gbooks():
    googleapikey="AIzaSyDgVyqZBnpNyoEC-U44rPw_f9KgRG_JSyA"
    def search(self, value):
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print(r.url)
        rj = r.json()
        print(rj["totalItems"])
        for i in rj["items"]:
            try:
                print(repr(i["volumeInfo"]["description"]))
            except:
                pass
            try:
                print(repr(i["volumeInfo"]["imageLinks"]["thumbnail"]))
            except:
                pass

