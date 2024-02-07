"""
Projekt1
Engeto Online Python Akademie: Projekt 1 - textový analyzátor
author: Andrea Kvapilová
email: a.ndrea@centrum.cz
discord: andreakvapilova
"""
import statistics
import task_template
import registred_user
import re

#global set
separator = 40 * "-" # separator for output
count_text = len(task_template.TEXTS) # number of prepared text

#login to the application
user_name = input("username: ")
password = input("password: ")

#checking the registration
if (user_name, password) in registred_user.registred_user.items():
    #visualization of program - welcome and text selection
    print(separator)
    if count_text > 1:
        print(f"Welcome to the app, {user_name}\nWe have {count_text} texts to be analyzed.")
    else:
        print(f"Welcome to the app, {user_name}\nWe have {count_text} text to be analyzed.")
    print(separator)
    select_text = input(f"Enter a number btw. 1 and {count_text} to select: ")
    if not select_text.isnumeric():
        print(f"Another input, terminating the program..")
        quit()
    select_text = int(select_text)
    if select_text < 1 or select_text > count_text:
        print(f"Number out of range, terminating the program..")
        quit()
    print(separator)

    # import and prepare text from task_template
    choosen_text = task_template.TEXTS[select_text - 1] #indexation adjustment
    text_split = choosen_text.split() #text division
    prepared_text = []
    for word in text_split:
        prepared_word = re.sub('[.?!,]', '', word) # remove punctuation .?!,
        prepared_text.append(prepared_word)

    #visualization of program - statistic
    count_word = statistics.count_all_words(prepared_text)
    if count_word > 1:
        print(f"There are {count_word} words in selected text.")
    else:
        print(f"There is {count_word} word in selected text.")

    count_titlecase = statistics.count_upper_letter(prepared_text)
    if count_titlecase > 1:
        print(f"There are {count_titlecase} titlecase words.")
    else:
        print(f"There is {count_titlecase} titlecase word.")

    count_uppercase = statistics.count_upper_word(prepared_text)
    if count_uppercase > 1:
        print(f"There are {count_uppercase} uppercase words.")
    else:
        print(f"There is {count_uppercase} uppercase word.")

    count_lowercase = statistics.count_lower_word(prepared_text)
    if count_lowercase > 1:
        print(f"There are {count_lowercase} lowercase words.")
    else:
        print(f"There is {count_lowercase} lowercase word.")

    count_numeric = statistics.count_number(prepared_text)
    if count_numeric > 1:
        print(f"There are {count_numeric} numeric strings.")
    else:
        print(f"There is {count_numeric} numeric string.")

    count_sum_numeric = statistics.sum_number(prepared_text)
    print(f"The sum of all numbers {count_sum_numeric}")
    print(separator)

    #visualization of program - graph of lenght words
    len_occur = statistics.len_occur_word(prepared_text)
    max_lenght = max(len_occur.values()) + 2 #adjustment to the longest word in len_occur
    print(f"{"LEN":>3}|{"OCCURENCES":^{max_lenght}}|{"NR.":>3}")
    print(separator)
    for(k, v) in len_occur.items():
        print(f"{k:3d}|{v * "*":<{max_lenght}}|{v:<3}")
else:
    print(f"unregistered user, terminating the program..")
    quit()










