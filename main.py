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
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

    def __init__(self, name, body):
        self.name = name 
        self.body = body

@app.route('/')

def index:
    
    return redirect('/blog')

@app.route('/blog')

def blog():
    blog_id = request.ergs.get('id')

    if blog_id == None:
        posts = Blog.query.all()
        return render_template('blog.html', posts=posts, title='Build-a-Blog')

    else:
        post = Blog.query.get('blog_id')
        return render_template('newpost.html', post=post)

@app.route('/newpost', methods=['POST', 'GET'])
def new_blog():
    name = request.form['title']
    new_blog = Blog(name)
    db.session.add(new_blog)
    db.session.commit()

    return render_template('newpost.html', title='title', text='text')


app.run()