def get_num_words(book_text):

    words = book_text.split()
    return len(words)

def get_num_characters(book_text):
    
    lower_book_text = book_text.lower()
    sorted_keys = sorted(set(lower_book_text))
    dict_num_characters = {key:0 for key in sorted_keys}

    for char in lower_book_text:
        dict_num_characters[char] += 1

    return dict_num_characters

