import os
import json
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session
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


@app.route('/spells')
def spells_druid():
    spellevel = mongo.db.spells.find({"class": "Druid", "level": "Cantrip"})
    spellevel1 = mongo.db.spells.find({"class": "Druid", "level": "1st"})
    spellevel2 = mongo.db.spells.find({"class": "Druid", "level": "2nd"})
    spellevel3 = mongo.db.spells.find({"class": "Druid", "level": "3rd"})

    return render_template('spells.html',
                           spells=spellevel,
                           spells1=spellevel1,
                           spells2=spellevel2,
                           spells3=spellevel3)


@app.route('/spells_level')
def spells_bard():
    spellevel4 = mongo.db.spells.find({"class": "Bard", "level": "Cantrip"})
    spellevel5 = mongo.db.spells.find({"class": "Bard", "level": "1st"})
    spellevel6 = mongo.db.spells.find({"class": "Bard", "level": "2nd"})
    spellevel7 = mongo.db.spells.find({"class": "Bard", "level": "3rd"})

    return render_template('spells_level.html',
                           spells4=spellevel4,
                           spells5=spellevel5,
                           spells6=spellevel6,
                           spells7=spellevel7)


@app.route('/spells_level')
def spells_wizard():
    spellevel8 = mongo.db.spells.find({"class": "Wizard", "level": "Cantrip"})
    spellevel9 = mongo.db.spells.find({"class": "Wizard", "level": "1st"})
    spellevel10 = mongo.db.spells.find({"class": "Wizard", "level": "2nd"})
    spellevel11 = mongo.db.spells.find({"class": "Wizard", "level": "3rd"})

    return render_template('spells_level.html',
                           spells8=spellevel8,
                           spells9=spellevel9,
                           spells10=spellevel10,
                           spells11=spellevel11)


@app.route('/spells_level')
def spells_sorcerer():
    spellevel12 = mongo.db.spells.find({"class": "Sorcerer", "level": "Cantrip"})
    spellevel13 = mongo.db.spells.find({"class": "Sorcerer", "level": "1st"})
    spellevel14 = mongo.db.spells.find({"class": "Sorcerer", "level": "2nd"})
    spellevel15 = mongo.db.spells.find({"class": "Sorcerer", "level": "3rd"})

    return render_template('spells_level.html',
                           spells12=spellevel12,
                           spells13=spellevel13,
                           spells14=spellevel14,
                           spells15=spellevel15)


@app.route('/spells_level')
def spells_artificer():
    spellevel16 = mongo.db.spells.find({"class": "Artificer", "level": "Cantrip"})
    spellevel17 = mongo.db.spells.find({"class": "Artificer", "level": "1st"})
    spellevel18 = mongo.db.spells.find({"class": "Artificer", "level": "2nd"})
    spellevel19 = mongo.db.spells.find({"class": "Artificer", "level": "3rd"})

    return render_template('spells_level.html',
                           spells16=spellevel16,
                           spells17=spellevel17,
                           spells18=spellevel18,
                           spells19=spellevel19)


@app.route('/spells_level')
def spells_warlock():
    spellevel20 = mongo.db.spells.find({"class": "Warlock", "level": "Cantrip"})
    spellevel21 = mongo.db.spells.find({"class": "Warlock", "level": "1st"})
    spellevel22 = mongo.db.spells.find({"class": "Warlock", "level": "2nd"})
    spellevel23 = mongo.db.spells.find({"class": "Warlock", "level": "3rd"})

    return render_template('spells_level.html',
                           spells20=spellevel20,
                           spells21=spellevel21,
                           spells22=spellevel22,
                           spells23=spellevel23)


@app.route('/spells_level')
def spells_cleric():
    spellevel24 = mongo.db.spells.find({"class": "Cleric", "level": "Cantrip"})
    spellevel25 = mongo.db.spells.find({"class": "Cleric", "level": "1st"})
    spellevel26 = mongo.db.spells.find({"class": "Cleric", "level": "2nd"})
    spellevel27 = mongo.db.spells.find({"class": "Cleric", "level": "3rd"})

    return render_template('spells_level.html',
                           spells20=spellevel24,
                           spells21=spellevel25,
                           spells22=spellevel26,
                           spells23=spellevel27)


@app.route('/spells_level')
def spells_ranger():
    spellevel28 = mongo.db.spells.find({"class": "Ranger", "level": "Cantrip"})
    spellevel29 = mongo.db.spells.find({"class": "Ranger", "level": "1st"})
    spellevel30 = mongo.db.spells.find({"class": "Ranger", "level": "2nd"})
    spellevel31 = mongo.db.spells.find({"class": "Ranger", "level": "3rd"})

    return render_template('spells_level.html',
                           spells28=spellevel28,
                           spells29=spellevel29,
                           spells30=spellevel30,
                           spells31=spellevel31)


@app.route('/spells_level')
def spells_paladin():
    spellevel32 = mongo.db.spells.find({"class": "Paladin", "level": "Cantrip"})
    spellevel33 = mongo.db.spells.find({"class": "Paladin", "level": "1st"})
    spellevel34 = mongo.db.spells.find({"class": "Paladin", "level": "2nd"})
    spellevel35 = mongo.db.spells.find({"class": "Paladin", "level": "3rd"})

    return render_template('spells_level.html',
                           spells32=spellevel32,
                           spells33=spellevel33,
                           spells34=spellevel34,
                           spells35=spellevel35)


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


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'email': request.form['email'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


@app.route('/get_comments')
def get_comments():
    return render_template("forum.html", questions=mongo.db.questions.find())


@app.route('/insert_reply', methods=['POST'])
def insert_reply():
    comment = mongo.db.comments
    comment.insert({'question_name': request.form['question_name'], 'reply_name': request.form['reply_name']})
    return redirect(url_for('get_comments'))


@app.route('/reply_question/<question_id>/<question_name>')
def reply_question(question_id, question_name):
    questions = mongo.db.questions.find_one({"_id": ObjectId(question_id)})
    comments = mongo.db.comments.find({"question_name": question_name})

    return render_template("reply.html", question=questions, comments=comments)


@app.route('/get_questions', methods=['POST'])
def insert_questions():

    comment = mongo.db.questions
    comment.insert({'question_name': request.form['question_name']})
    return redirect(url_for('get_comments'))


""""@app.route('/battles')
def battles():
    return render_template("battles.html")"""

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=True)
