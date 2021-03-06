#### SESSIONS ####
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # SEE FLASK FOR MORE NOTES

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username']) #escape used here for example only
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form method='post'>
       <p><input type=text name=username>
       <p><input type=submit value=Login>
    </form>
    '''

@app.route('/logout')
def logout():
    # remove the useranme from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

## NOTES IN FLASK ABOUT CREATING SESSION KEYS