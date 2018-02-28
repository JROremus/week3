from flask import Flask, render_template

from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'onlyjames'

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
    return render_template('login.html', title='Sign In', form=form)

app.run()