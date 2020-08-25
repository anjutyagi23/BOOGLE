from flask import Flask ,render_template,request,jsonify 
import requests
from elasticsearch import Elasticsearch

res = requests.get('http://localhost:9200/')
#print(res.content)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)
#AIzaSyDgVyqZBnpNyoEC-U44rPw_f9KgRG_JSyA
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    keywords = request.form['keywords']
    query_body = {
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": ["description", "title"]
            }
        }
    }

    res = es.search(index="books_tech", doc_type="book", body=query_body)
    return render_template("result.html",res =res)
    #return jsonify(res['hits']['hits'])

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000, debug=True)