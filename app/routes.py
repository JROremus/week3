from app import app2 as app
from app.forms import LoginForm
from flask import render_template, redirect, flash

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JR'}

    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard.'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy.'
        },

        {
            'title': {'main': 'I love C#'},
            'body': 'c# can do some thing, and it is very easy!'
        }
    ]

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

app.run()