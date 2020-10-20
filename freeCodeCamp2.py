from flask import Flask
app = Flask(__name__)

@app.route('/')
def python():
    myFile = open('data.txt')
    for each_line in myFile:
        print(each_line)


    a_file = open('data.txt')
    line_count = 0
    for new_line in a_file:
        line_count += 1
    print('Line count', line_count)



    return 'and here we go'