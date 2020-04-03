def string_search(search_term, file_list):
    count = 0
    for text in file_list:
        with open(text.lower(), 'r') as fp:
            for line in fp:
                count += line.count(search_term)
    return count
