from flask import Flask
app = Flask(__name__)

x = 100
y = 45
string = '123'
num = int(string)
# name = input('Who are you?') # Input gives you a STRING

# europeFloor = input('Eupore floor is?')
# usFloor = int(europeFloor) + 1



@app.route('/')
def hello():
    print(x)
    print(float(45))
    print(type(y))
    print(string)
    print(num)
    # print('Welcome', name)
    print('US Floor', usFloor)

    if x < 70:
        print('yes, less than 70')
    if x > 100:
        print('more than 70')
    if x == 100:
        print('100!!')
        print('One hundred')
        print('Still 100!!!')
    print('this is not included in the block')

    if x >50:
        print('greater than 50')
    else:
        print('smaller than 50')
    print('finished')

    if  y > 2000:
        print('greater than 2000')
    elif y > 100:
        print('greater than 100')
    elif y > 50:
        print('greater than 50')
    elif y > 10:
        print('greater than 10')
    else: # Dont have to have an else
        print('Not greater than 10')
    print('All done')

    try: 
       number2 = float('Hello')
    except:
        print('Passed, except block ran as string cannot be floated')
    print('Try block')

    def my_name():
        print('my_name function ran')
        print('Another line')
        print(max('Hello world'))  
        print(float(45) * 30 / 4 + int('450'))
    
    my_name()
    my_name()

    def favouriteTeam(team):
        if team == 'manu':
            return 'The best team in the world...maybe'
        elif team == 'newcastle':
            return 'Not that great'
        else:
            return 'Enter a team name'
        return 'function finished'

    print(favouriteTeam('manu'))
    print(favouriteTeam(''))

    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown = countdown - 1
    print('Liftoff!!')

    apples = 2
    while apples > 3:
        line = input('> ')
        if line == 'hello':
            break # exit loop
        print(line)
    print('while loop break hit')

    bananas = 2
    while bananas > 3:
        line = input('> ')
        if line[0] == '#':
            continue # go back to start of loop
        print(line)
        if line == 'done':
            break # exit loop
        print(line)
    print('done')

    for i in [5, 4, 3, 2, 1]:
        print(i)
    print('done')

    return favouriteTeam('manu')