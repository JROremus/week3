from app import app2 as app
from app.forms import LoginForm
from flask import render_template, redirect, flash

from app.models import Post

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JR'}

    posts = Post.query.all()

    return render_template('index.html', user=user, posts=posts, title='A Title')


@app.route('/store')
def store():

    items = [
        {
            'title': 'Python Book',
            'body': '200'
        },

        {
            'title': 'Cook Book',
            'body': '2'
        },

        {
            'title': 'iPhone X',
            'body': '1000'
        }
    ]

    return render_template('store.html', items=items)

@app.route('/login' , methods=['Get' , 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}' .format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)