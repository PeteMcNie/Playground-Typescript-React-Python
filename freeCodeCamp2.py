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


    the_file = open('data.txt')
    a_string = the_file.read() # ONLY READ WHOLE FILES IF THEY ARE SMALL < 200,000 characters
    print('Number of characters is file', len(a_string)) # prints whole length as file returned as a string
    print('Only first 30 characters', a_string[:30]) # uses slice to print only first 30 characters


    search_for = open('data.txt')
    for each_new_line in search_for:
        if each_new_line.startswith('Poseidon'):
            print(each_new_line)    #WILL DEFAULT PRINT A NEW LINE (WHICH YOU PROBABLY DONT WANT)

    search_with_no_new_line = open('data.txt')
    for no_new_line in search_with_no_new_line:
        no_new_line = no_new_line.rstrip() # new lines (\n) count as white space so can strip away
        if no_new_line.startswith('Poseidon'):
            print(no_new_line)



    using_in_operator = open('data.txt')
    for line in using_in_operator:
        line = line.rstrip()
        if not 'Athena' in line: # searches for lines WITH Athena in
            continue
        print('Only print lines with Athena', line)



    file_name = raw_input('Enter a file name to search through:  ')
    try:
        file_handle = open(file_name)
    except:
        print('File cannot be opened:', file_name)
        quit() # Stop executing the rest of this file. We need to provide our own error message above as there will be no traceback

    count2 = 0
    for line in file_handle:
        if 'Poseidon' in line:
            count2 += 1
    print('Lines with Poseidon', count2)



    #LISTS [] like arrays in JS













    return 'and here we go'