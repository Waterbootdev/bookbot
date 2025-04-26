from stats import char_key, num_key

def print_count_message(count, type):

    message = f"{count} {type} found in the document"

    print(message)

def print_char_counts(char_counts_list):

    print("--------- Character Count -------")
    
    for char_count in char_counts_list:
        char = char_count[char_key]
        num = char_count[num_key]
        print(f"{char}: {num}")

def print_word_count(count):

    print("----------- Word Count ----------")

    print(f"Found {count} total words")

def print_bookbot_start():
    print("============ BOOKBOT ============")
    
def print_bookbot_end():
    print("============= END ===============")

def print_source(path_to_book):
    print(f"Analyzing book found at {path_to_book}...")

def print_bookbot(path_to_book, word_count, char_counts_list):
    print_bookbot_start()
    print_source(path_to_book)
    print_word_count(word_count)
    print_char_counts(char_counts_list)
    print_bookbot_end()

    