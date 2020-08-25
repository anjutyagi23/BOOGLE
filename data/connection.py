import requests
from elasticsearch import Elasticsearch
import json
import random

res = requests.get('http://localhost:9200/')
#print(res.content)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
i=1
books_list=["python","R","information science","AI","deep learning","elastic search","information retrieval","image processing","search engine",'reactjs',"html",
           "server side","javascript","Data Mining","nference and Prediction","data analysis","cloud computing","client side","ethical hacking","Statistical Learning"
           "Pattern Recognition and Machine Learning","mathematics for machine learning","coding","c++","C#","java","scripting languages","linux","unix","virtual environment"]
for book in books_list:
    books = requests.get("https://www.googleapis.com/books/v1/volumes?q=" +
                            book +
                            "&maxResults=40&key=AIzaSyCjewB8JaZil--qGlfSy8aZf0QVL4qK5jQ").json()
    r = json.dumps(books)
    loaded_books = json.loads(r)
    dict_book={}
   
    for item in loaded_books["items"]:
        try:
            dict_book["id"]=i
            if "title" not in item["volumeInfo"]:
                dict_book["title"]='NA'
            else:
                dict_book["title"]=item["volumeInfo"]["title"]
            if "description" not in item["volumeInfo"]:
                dict_book["description"]='NA'
            else:
                dict_book["description"]=item["volumeInfo"]["description"]
            if "authors" not in item["volumeInfo"]:
                dict_book["authors"]='NA'
            else:
                dict_book["authors"]=item["volumeInfo"]["authors"]
            if "previewLink" not in item["volumeInfo"]:
                dict_book["previewLink"]="NA"
            else:
                dict_book["previewLink"]=item["volumeInfo"]["previewLink"]
            if "infoLink" not in item["volumeInfo"]:
                dict_book["infoLink"]="NA"
            else:
                dict_book["infoLink"]=item["volumeInfo"]["infoLink"]

            es.index(index='books_tech', doc_type='book',id=i,  body=dict_book)
            i=i+1
            print(i)

        except:
            continue;

    
print("Done!")

   


