import hashedindex
import re

def index_search(search_term, file_list):
    inverted_index = hashedindex.HashedIndex()

    for text in file_list:
        with open(text, 'r') as file_input:
            clean_document = re.sub('[^a-zA-Z0-9\n\.]', ' ', file_input.read().lower())
            file_name = text.split('/')
            for term in clean_document.split():
                inverted_index.add_term_occurrence(term, file_name[1])
        inverted_index.items()
    return
