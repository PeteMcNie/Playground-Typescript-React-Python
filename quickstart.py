from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'hello world, see me run'

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'Hey world'
