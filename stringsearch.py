import re

def string_search(search_term, file_list):
    word_count = {}
    count = 0
    for text in file_list:
        with open(text, 'r') as file_input:
            line = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_input.read().lower())
            word_list = line.split()
            word_count[text] = word_list.count(search_term)
    return word_count
