from flask import Flask
app = Flask(__name__)

@app.route('/')
def myfunction():
    # Dictionaries
    my_dict = dict()
    my_dict['akey'] = 1
    my_dict['anotherkey'] = 45
    my_dict['calledanything'] = 6
    print(my_dict)
    print(my_dict['anotherkey'])

    my_dict['anotherkey'] =   my_dict['anotherkey'] - 23
    print(my_dict['anotherkey'])


    #comparing lists and dictionaries
    my_list = list()
    my_list.append(34)
    my_list.append(56)
    print(my_list)
    my_list[0] = 22
    print(my_list)


    my_new_dict = dict()
    my_new_dict['keyagain'] = 76
    my_new_dict['anotherkey'] = 24
    print(my_new_dict)
    my_new_dict['anotherkey'] = 88
    print(my_new_dict)


    # dictionary literals
    dictionary = { 'key': 22, 'anotherkey': 56, 'bananas': 77 }
    print(dictionary)
    create_empty_dict = {}
    print(create_empty_dict)


    #Counting frequency of things
    counting = dict()
    counting['pablo'] = 1
    counting['rahul'] = 1
    print(counting)
    counting['pablo'] = counting['pablo'] + 1
    print(counting)


    count = dict()
    names = ['pete', 'nigel', 'court', 'atlas', 'jeff', 'atlas', 'court']
    for name in names:
        if name not in count:
            count[name] = 1
        else:
            count[name] = count[name] + 1
    print(count)

    count2 = dict()
    names2 = ['pete', 'nigel', 'court', 'atlas', 'jeff', 'atlas', 'court', 'pete', 'atlas']
    for name in names2:
        count2[name] = count2.get(name, 0) + 1  #using get to simplify counting
    print(count2)


    dictionary_of_words = dict()  #This loops through BUILDING a dictionary
    my_file = open('data.txt')
    for each_line in my_file:
        words = each_line.split()
        
        for word in words:
            dictionary_of_words[word] = dictionary_of_words.get(word, 0) + 1
    print('Counting....')
    print(dictionary_of_words)
    

    new_dict = { 'foo': 3, 'bar': 7, 'ninja': 56 }
    for key in new_dict:
        print(key, new_dict[key])

    print(list(new_dict))
    print('Printing keys', new_dict.keys())
    print('Printing values', new_dict.values())
    print('Printing keys and values: output is a tuple', new_dict.items())

    for key,value in new_dict.items(): # AWESOME FOR LOOP WHICH ACCESSES BOTH KEYS AND VALUES AT THE SAME TIME
        print(key,value)



    file_name = raw_input('Enter file name here:   ') # user can input file to search
    handle = open(file_name) #open up that file

    a_dict = dict() # initialise a new EMPTY dict
    for e_line in handle:
        words = e_line.split() # Break each line into indivdual words

        for word in words:
            a_dict[word] = a_dict.get(word, 0) + 1 # if the word is new, add the word TO THE DICT and give it a value of 1. If word already seen, add 1.
    
    most_counted = None
    word_most_counted = None
    for word,count in a_dict.items(): # check keys and values in our dict
        if most_counted is None or count > most_counted: # if a number in our dict is GREATER THAN most_counted, most_counted is THAT NUMBER (two lines down)
            word_most_counted = word # WHATEVER WAS THE HIGHEST COUNT, THE WORD NEXT TO IT IS THE word_most_counted
            most_counted = count

    print(most_counted, word_most_counted)











    return 'Data structures'