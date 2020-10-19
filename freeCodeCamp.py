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
    # print('US Floor', usFloor)

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

    


    # LOOP IDIOMS
    print('before')
    for theNumber in [9, 47, 65, 23]:
        print(theNumber)
    print('after')


    largest_so_far = -1
    print('before', largest_so_far)
    for num1 in [56, 2, 57, 34, 444, 86, 234, 0, 84]:
        if num1 > largest_so_far:
            largest_so_far = num1
        print(largest_so_far, num1)
    print('after', largest_so_far)

    count = 0
    loop_total = 0
    print('before', loop_total)
    for loop_num in [56, 2, 57, 34, 444, 86, 234, 0, 8]:
        count += 1
        loop_total += loop_num
        print(count, loop_total, loop_num)
    print('after', count, loop_total, loop_total / count)

    print('before')
    for num2 in [56, 2, 57, 34, 444, 86, 234, 0, 84]:
        if num2 > 100:
            print('Numbers greater than 100: ', num2)
    print('after')

    # Better technique for setting the initial variable when you don't know a starting number
    smallest = None
    print('before')
    for num3 in [56, 12, 57, 34, 444, 86, 234, 1, 84]:
        if smallest is None:
            smallest = num3
        elif num3 < smallest:
            smallest = num3
            print('Smallest number:', smallest)
    print('after', smallest)


    #LOOPING STRINGS
    fruit_i_like = 'banana'
    letter = fruit_i_like[2]
    print(letter)
    # letter = fruit_i_like[54] Cannot search for string indexes out of range / longer than string length
    # print(letter)
    print(len(fruit_i_like))

    index = 0
    while index < len(fruit_i_like):
        letter2 = fruit_i_like[index]
        print(index, letter2)
        index += 1


    for letter in fruit_i_like:
        print(letter)
    

    a_count = 0
    for letter in fruit_i_like:
        if letter == 'a':
            a_count += 1
    print(a_count)


    # SLICING STRINGS
    s = 'Hello world'
    print(s[0:4])
     # read as: print 's', 0 = sub-zero, : = through to, 4 = up to but NOT INCLUDING 4
    print(s[6:7])
    print(s[:7])
    # means start at the start

    print(s[6:])
    # means end at the end

    print(s[:])
    # mean start at the start and end at the end


    # in can be used as an operator (== etc)
    if 'a' in fruit_i_like:
        print('Would be true')

    if 'y' in fruit_i_like:
        print('Would be false so this text will not show!!!!')


    greeting = 'Hello Pete'
    lowercase = greeting.lower()
    print(greeting, lowercase)

    position = fruit_i_like.find('na')
    print(position)
    uppercase = fruit_i_like.upper()
    print(uppercase)
    lowercase1 = fruit_i_like.lower()
    print(lowercase1)
    newString = fruit_i_like.replace('banana', 'orange')
    print(newString)
    newLetter = fruit_i_like.replace('a', 'XX')
    print(newLetter)

    spaces = '        hello spaces      '
    print(spaces)
    spaces1 = spaces.lstrip()
    print(spaces1)
    spaces2 = spaces.rstrip()
    print(spaces2)
    spaces3 = spaces.strip()
    print(spaces3)

    line = "Have a nice day"
    print(line.startswith('Have'))
    print(line.startswith('h'))


    email_data = 'pablo_sanchez455@hotdog.co.net FEB 2020'

    atsignpos = email_data.find('@')
    print(atsignpos)

    spacepos = email_data.find(' ', atsignpos)
    #                             point to search for the space AFTER
    print(spacepos)

    pablosaddress = email_data[atsignpos +1:spacepos]
    print(pablosaddress)














    return favouriteTeam('manu')