import re

def reg_search(search_term, file_list):
    word_count = {}
    for text in file_list:
        with open(text, 'r') as file_input:
                line = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_input.read().lower())
                search = re.findall(r'(\b' + search_term + r'\b)', line)
                count = len(search)
                word_count[text] = count
    return word_count
