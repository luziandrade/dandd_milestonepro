import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/articles')
def articles():
    return render_template("articles.html")


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=os.getenv('PORT', '5000'),
            debug=True)
