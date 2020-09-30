from flask import Flask
app = Flask(__name__)

x = 100
y = 45
string = '123'
num = int(string)
name = input('Who are you?') # Input gives you a STRING
europeFloor = input('Eupore floor is?')
usFloor = int(europeFloor) + 1

@app.route('/')
def hello():
    print(x)
    print(float(45))
    print(type(y))
    print(string)
    print(num)
    print('Welcome', name)
    print('US Floor', usFloor)

    return 'Hey y\'all'