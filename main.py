from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:admin@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name 


blogs = []

@app.route('/')

def blog():
    return render_template('blog.html')

@app.route('/', methods=['POST', 'GET'])
def new_blog():
    name = request.form['title']
    new_blog = Blog(name)
    db.session.add(new_blog)
    db.session.commit()

    return render_template('newpost.html')


app.run()