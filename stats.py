
char_key = "char"
num_key= "num"

def get_word_count(book_text):

    words = book_text.split()
    
    return len(words)

def get_all_char_counts(book_text):
    
    lower_book_text = book_text.lower()
    sorted_keys = sorted(set(lower_book_text))
    dict_num_characters = {key:0 for key in sorted_keys}

    for char in lower_book_text:
        dict_num_characters[char] += 1

    return dict_num_characters

def convert_and_filter_char_count(char_count_dict):
    return sorted([{char_key:char, num_key: num} for char, num in char_count_dict.items() if char.isalpha()], key=lambda charcount: charcount[num_key], reverse=True)
 
def get_printable_char_counts(book_text):
    return convert_and_filter_char_count(get_all_char_counts(book_text))