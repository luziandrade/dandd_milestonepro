import os
import json
from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dungeons'
app.config[
    "MONGO_URI"] = 'mongodb+srv://root:010203@myfirstcluster-ekkz4.mongodb.net/dungeons?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_battle')
def get_battle():
    return render_template("battles.html", guides=mongo.db.guides.find())


@app.route('/get_classes')
def get_classes():
    return render_template("classes.html", classes=mongo.db.classes.find())


@app.route('/get_races')
def get_races():
    return render_template("races.html", races=mongo.db.races.find())


@app.route('/get_spells')
def get_spells():
    return render_template("spells.html", spells=mongo.db.spells.find())





@app.route('/articles')
def articles():
    data = []
    with open("data/articles.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("articles.html", page_title="Article", articles=data)


""""@app.route('/battles')
def battles():
    return render_template("battles.html")


@app.route('/articles/<article_title>')
def articles_article(article_title):
    article = {}

    with open("data/articles.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == article_title:
                article = obj

    return render_template("article.html", article=article)"""


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=os.getenv('PORT', '5000'),
            debug=True)
