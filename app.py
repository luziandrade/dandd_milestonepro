import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'some_secret'
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
    with open("data/article.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("articles.html", page_title="Article", articles=data)


@app.route('/articles/<article_name>')
def articles_article(article_name):
    article = {}

    with open("data/article.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == article_name:
                article = obj

    return render_template("article.html", article=article)


"""@app.route('/spells_level')
def spells_bard():
    spell_ = mongo.db.spells.find({"class":"Bard","level":"Cantrip"})
    spell1 = mongo.db.spells.find({"class": "Bard", "level": "1st"})

    return render_template("spells_level.html", spellevel=spell, spellevel1=spell1)


@app.route('/spells_level')
def spells_wizard():
    spell = mongo.db.spells.find({"class":"Wizard","level":"Cantrip"})
    return render_template("spells_level.html", spellevel=spell)"""


"""@app.route('/spells_level')
def spells_level():
    query = {"level":"Cantrip", "class":"Bard"}
    return render_template('spells_level.html', spellevel=mongo.db.spells.find(query))"""


""""@app.route('/battles')
def battles():
    return render_template("battles.html")"""


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=True)
