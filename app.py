from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from urllib.parse import quote_plus
import pymongo
import json
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__,template_folder='static/templates')


#allow cross origin script access so can access via js
CORS(app)

mongo = PyMongo(app, uri="mongodb://root:ucbmongodb@35.184.4.63:27017/weather")
conn = 'mongodb://root:ucbmongodb@35.184.4.63:27017'
client = pymongo.MongoClient(conn)
db = client.weather


# Set up routes
@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/tcc.html")
def tcc():
    return render_template("tcc.html")

@app.route("/tcc-documentation.html")
def tcc_doc():
    return render_template("tcc-documentation.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/articles.html")
def articles():
    return render_template("articles.html")

# Set up api routes
@app.route("/api/v1/<year>/<severity>/<algorithm>")
def firePrediction(year,severity,algorithm):
    print("reached the API")
    collection_name = severity + '_' +algorithm + '_' + year
    predictionData = dumps(db[collection_name].find({},{'_id': 0,'x':1,'y':1,'prediction':1}))
    print(predictionData)
    return jsonify(json.loads(predictionData))


if __name__ == '__main__':
    app.run(debug=True)