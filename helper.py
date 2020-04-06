import hashedindex
import re

def index_search(search_term, file_list):
    
    word_count = {}
    
    inverted_index = hashedindex.HashedIndex()

    for text in file_list:
        with open(text, 'r') as file_input:
            clean_document = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_input.read().lower())
            file_name = text.split('/')
            for term in clean_document.split():
                inverted_index.add_term_occurrence(term, file_name[1])

    result = inverted_index.get_documents(search_term)
    for key, value in result.items():
        path = "sample_text/" + key
        word_count[path] = value
    return word_count

def reg_search(search_term, file_list):
    word_count = {}
    for text in file_list:
        with open(text, 'r') as file_input:
                line = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_input.read().lower())
                search = re.findall(r'(\b' + search_term + r'\b)', line)
                count = len(search)
                word_count[text] = count
    return word_count

def string_search(search_term, file_list):
    word_count = {}
    count = 0
    for text in file_list:
        with open(text, 'r') as file_input:
            line = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_input.read().lower())
            word_list = line.split()
            word_count[text] = word_list.count(search_term)
    return word_count
