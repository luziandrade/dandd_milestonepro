import os
import json
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session, g
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'some_secret'
app.config["MONGO_DBNAME"] = 'dungeons'
app.config[
    "MONGO_URI"] = 'mongodb+srv://root:010203@myfirstcluster-ekkz4.mongodb.net/dungeons?retryWrites=true&w=majority'
#app.config['MONGO_URI'] = os.environ.get("MONGODB_URI")
mongo = PyMongo(app)


@app.route('/')
def index():
        data = []
        with open("data/article.json", "r") as json_data:
            data = json.load(json_data)
        return render_template("index.html", page_title="Article", articles=data)


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
    classes = mongo.db.classes.find()
    spells = mongo.db.spells.find()
    classes = mongo.db.classes.find()
    spellevel5 = mongo.db.spells.find({"class": "Barbarian", "level": "Cantrip"})
    spellevel1 = mongo.db.spells.find({"class": "Barbarian", "level": "1st"})
    spellevel2 = mongo.db.spells.find({"class": "Barbarian", "level": "2nd"})
    spellevel3 = mongo.db.spells.find({"class": "Barbarian", "level": "3rd"})
    spellevel4 = mongo.db.spells.find({"class": "Barbarian", "level": "4th"})
    return render_template("spells.html", classes=classes,
                                          spells=spells,
                                         spells5=spellevel5,
                                          spells1=spellevel1,
                                          spells2=spellevel2,
                                          spells3=spellevel3,
                                         spells4=spellevel4)


@app.route('/spells_name/<class_name>')
def spells_name(class_name):
    classes = mongo.db.classes.find()
    spellevel = mongo.db.spells.find({"class": class_name, "level": "Cantrip"})
    spellevel1 = mongo.db.spells.find({"class": class_name, "level": "1st"})
    spellevel2 = mongo.db.spells.find({"class": class_name, "level": "2nd"})
    spellevel3 = mongo.db.spells.find({"class": class_name, "level": "3rd"})
    spellevel4 = mongo.db.spells.find({"class": class_name, "level": "4th"})

    return render_template('spells_name.html',
                           spells=spellevel,
                           spells1=spellevel1,
                           spells2=spellevel2,
                           spells3=spellevel3,
                           spells4=spellevel4,
                           classes=classes)


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


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')


@app.route('/get_comments')
def get_comments():
    if g.username:
        return render_template("forum.html",
                               questions=mongo.db.questions.find(),
                               users=mongo.db.users.find({"name": session['username']}))
    return render_template('register.html')


@app.route('/insert_reply', methods=['POST'])
def insert_reply():
    if g.username:
        comment = mongo.db.comments
        comment.insert({'question_name': request.form['question_name'],
                        'reply_name': request.form['reply_name'],
                        'username': request.form['username']})
        return redirect(url_for('get_comments'))

    return render_template('register.html')


@app.route('/reply_question/<question_id>/<question_name>')
def reply_question(question_id, question_name):
    questions = mongo.db.questions.find_one({"_id": ObjectId(question_id)})
    comments = mongo.db.comments.find({"question_name": question_name})
    author = mongo.db.users.find({"name": session['username']})
    user = session['username']
    return render_template("reply.html", question=questions, comments=comments, user=user, users=author)


@app.route('/get_questions', methods=['POST'])
def insert_questions():

    comment = mongo.db.questions
    comment.insert({'question_name': request.form['question_name'], 'username': session['username']})
    return redirect(url_for('get_comments'))


@app.route('/edit_comment/<comment_id>')
def edit_comment(comment_id):
    the_comments = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    all_questions = mongo.db.questions.find()
    return render_template("editcomment.html", comments=the_comments, questions=all_questions)


@app.route('/update_comment/<comment_id>', methods=["POST"])
def update_comment(comment_id):
    comments = mongo.db.comments
    comments.update_one({'_id': ObjectId(comment_id)}, {"$set": {'reply_name': request.form.get('reply_name')}})
    return redirect(url_for('get_comments'))


@app.route('/delete_comment/<comment_id>')
def delete_comment(comment_id):
    comments = mongo.db.comments
    comments.remove({'_id': ObjectId(comment_id)})
    return redirect(url_for('get_comments'))


""""@app.route('/battles')
def battles():
    return render_template("battles.html")"""

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=True)
