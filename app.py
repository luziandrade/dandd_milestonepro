import os
import json
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/articles')
def articles():
    data = []
    with open("data/articles.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("articles.html", page_title="Article", articles=data)


@app.route('/articles/<article_title>')
def articles_article(article_title):
    article = {}

    with open("data/articles.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == article_title:
                article = obj

    return render_template("article.html", article=article)


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=os.getenv('PORT', '5000'),
            debug=True)
