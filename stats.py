
char_key = "char"
num_key="num"

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

def to_sorted_char_count_list(char_count_dict):
    return sorted([{char_key:char, num_key: num} for char, num in char_count_dict.items()],key=lambda charcount: charcount[num_key], reverse=True)

def filter_printable(char_count_list):
    return list(filter(lambda charcount: charcount[char_key].isalpha() ,char_count_list))        
 
def get_printable_char_counts(book_text):
    return filter_printable(to_sorted_char_count_list(get_num_characters(book_text)))