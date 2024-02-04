"""
Projekt1 - statistika
Engeto Online Python Akademie: Projekt 1 - textový analyzátor
author: Andrea Kvapilová
email: a.ndrea@centrum.cz
discord: andreakvapilova
"""
#text analysis
#function for counting all word in input text
def count_all_words(text: str) -> int:
    count_all_words = 0

    for word in text:
        if word.isalnum():
            count_all_words += 1
    return count_all_words

#function for counting word start with upper letter
def count_upper_letter(text: str) -> int:
    count_upper_letter = 0

    for word in text:
        if word.istitle():
            count_upper_letter += 1
    return count_upper_letter

#function for counting upper case word in input text
def count_upper_word(text: str) -> int:
    count_upper = 0

    for word in text:
        if word.isupper() and word.isalpha():
            count_upper += 1
    return count_upper

#function for counting lower case word in input text
def count_lower_word(text: str) -> int:
    count_lower = 0

    for word in text:
        if word.islower():
            count_lower += 1
    return count_lower

#function for counting number in input text
def count_number(text: str) -> int:
    sum = 0

    for word in text:
        if word.isdigit():
            sum += 1
    return sum

#function for sum all number in input text
def sum_number(text: str) -> int:
    sum = 0

    for word in text:
        if word.isdigit():
            number = int(word)
            sum = sum + number
    return sum

#function for lenght of world and occurence
def len_occur_word(text: str) -> dict:
    len_occ = dict()
    for word in text:
        lenght = len(word)
        if lenght not in len_occ.keys():
            len_occ[lenght] = 1
        else:
            len_occ[lenght] += 1
    sorted_dict = dict(sorted(len_occ.items()))
    return sorted_dict