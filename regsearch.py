import re

def reg_search(search_term, file_list):
    word_count = {}
    for text in file_list:
        with open(text, 'r') as file_input:
                line = file_input.read()
                line = line.lower()
                search = re.findall(r'(' + search_term + ')', line)
                print(search)
                count = len(search)
                word_count[text] = count
    return word_count
