import hashedindex
import re

def index_search(search_term, file_list):
    word_count = {}
    inverted_index = hashedindex.HashedIndex()
    for text in file_list:
        with open(text, 'r') as file_input:
            clean_document = re.sub('[^a-zA-Z0-9\n\s]', '', file_input.read().lower())
            file_name = text.split('/')
            for term in clean_document.split():
                inverted_index.add_term_occurrence(term, file_name[1])
        try:
            result = inverted_index.get_documents(search_term)
            for key, value in result.items():
                word_count[text] = value
        except IndexError:
            word_count[text] = 0
            continue
    return word_count

def reg_search(search_term, file_list):
    word_count = {}
    for text in file_list:
        with open(text, 'r') as file_input:
                line = file_input.read()
                search = re.findall(r'%s' % search_term, line, re.MULTILINE)
                count = len(search)
                word_count[text] = count
    return word_count

def string_search(search_term, file_list):
    word_count = {}
    count = 0
    for text in file_list:
        with open(text, 'r') as file_input:
            line = re.sub('[^a-zA-Z0-9\n\s]', '', file_input.read().lower())
            search = re.findall(r'(\b' + search_term + r'\b)', line)
            count = len(search)
            word_count[text] = count
    return word_count
