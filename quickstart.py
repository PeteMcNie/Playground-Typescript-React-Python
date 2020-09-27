from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'hello world, see me run'

# @app.route('/')
# def index():
#     return 'Home page'

@app.route('/hello')
def hello():
    return 'Sup world'


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

# @app.route('/')
# def index():
#     url_for('static', filename='styles.css)
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    # print(url_for('index'))
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


#### REQUEST OBJECT ####
from flask import request, render_template

#### TESTING - see flask docs ####
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

# @app.route('/loginagain', methods=['POST', 'GET'])
# def loginagain():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username or password'
#             # code below executed if GET request OR credentials not valid
#     return render_template('login.html', error=error)


## to access params in URL use the args attribute:
## my_param = request.args.get('key', '')

## SEE MORE INFO ON FLASK WEBPAGE



#### REDIRECTS AND ERRORS ####
from flask import abort, url_for, redirect

def this_is_never_executed():
    return 'Why can\'t you see me?'

@app.route('/')
def index():
    return redirect(url_for('loginthird'))

@app.route('/loginthird')
def loginthird():
    abort(401)
    this_is_never_executed()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
