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



    # file_name = raw_input('Enter a file name to search through:  ')
    # try:
    #     file_handle = open(file_name)
    # except:
    #     print('File cannot be opened:', file_name)
    #     quit() # Stop executing the rest of this file. We need to provide our own error message above as there will be no traceback

    # count2 = 0
    # for line in file_handle:
    #     if 'Poseidon' in line:
    #         count2 += 1
    # print('Lines with Poseidon', count2)



    #LISTS [] like arrays in JS
    # LISTs ARE mutable
    print(['blue', 'red', 'yellow', 24, 89.6])
    print(['Dan', 'Steve', [1, 'Snow'], 'Kim'])

    friends = ['Sam', 'Ari', 'Jake', 'Zac', 'Kim', 'Rikke']
    for friend in friends: # This loop is fine if you don't need to know your position in the loop
        print('Happy Birthday:', friend)
    print('The end')

    print(friends[1]) # ari
    print(len(friends)) # Number of items in a list ie: 6
    print(range(3)) # range gives us a list upto that number ie: [0, 1, 2]
    print(range(len(friends))) # range combined with len give us each index of the list ie: [0, 1, 2, 3, 4, 5]

    for index in range(len(friends)): # This for statement uses index to find the data stored at each location in the list
        friend = friends[index]       # SAME AS ABOVE LOOP BUT USES INDEX
        print('Happy New Year:', friend)


    #You can add lists together like this:
    a = [1, 2, 3]
    b = [5, 6, 7]
    c = a + b
    print('Two lists added together', c)

    #LIST SLICING
    my_list = [3, 94, 75, 63, 7, 800, 19, 10, 151, 812, 1, 14]
    print(my_list[1:3])
    print(my_list[:4])
    print(my_list[5:])
    print(my_list[:])

    #LIST METHODS
    stuff = list() # makes an empty list
    stuff.append('book')
    stuff.append(56)
    print(stuff)
    
    print(94 in my_list)
    print(10 in my_list)
    print(24 not in my_list)

    print('Pre-sort', my_list)
    my_list.sort()
    print('Sorted', my_list)

    print(len(my_list))
    print(max(my_list))
    print(min(my_list))
    print(sum(my_list))
    print(sum(my_list)/len(my_list))

    total = 0 # Create a for loop to add up the values of numbers input into the computer, the find average
    count = 0
    while True:
        inputt = input('Enter a number: ')
        if inputt == 0 : 
            break
        value = float(inputt)
        total += value
        count += 1
    average = total / count
    print('Average is:', average)

    # Create a list to add numbers to, then find average
    new_list = list()
    while True:
        inputt2 = input('Enter a number: ')
        if inputt2 == 0 : break
        new_list.append(inputt2)
    print(sum(new_list)/len(new_list))

    return 'and here we go'