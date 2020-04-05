def string_search(search_term, file_list):
    word_count = {}
    count = 0
    for text in file_list:
        with open(text.lower(), 'r') as file_input:
            for line in file_input:
                line = line.lower()
                count += line.count(search_term)
                word_count[text] = count
    return word_count
