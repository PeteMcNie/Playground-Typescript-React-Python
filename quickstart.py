from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'hello world, see me run'

# @app.route('/')
# def index():
#     return 'Home page'

# @app.route('/hello')
# def hello():
#     return 'Sup world'


#### VARIABLE ROUTES ####
from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/user/<path:subpath>')
def show_own_example(subpath):
    return 'Own example is %s' % escape(subpath)



#### UNIQUE URLs ####
# the backslash at the end of the route matters
@app.route('/projects/')
def projects():
    return 'The projects page'

@app.route('/about')
def about():
    return 'The about page'


#### URL BUILDING ####
from flask import url_for

@app.route('/')
def index():
    return 'index'

# @app.route('/login')
# def login():
#     return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='Pablo Sanchez'))


#### HTTP METHODS ####
# By default a route ONLY ANSWERS GET requests, use methods to specify differnent methods
from flask import request

def do_the_login():
    return 'Logging in....'

def show_the_login_form():
    return 'Here is the login form'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

