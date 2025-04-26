from stats import get_num_words, get_num_characters

def get_book_text(path_to_book):

    with open(path_to_book) as file:
        return file.read()

def print_count_message(count, type):

    message = f"{count} {type} found in the document"

    print(message)

    

def main():

    #read the book
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)

    #count inside the book
    number_of_words = get_num_words(book_text)
    number_of_chars = get_num_characters(book_text)

    #print counts
    print_count_message(number_of_words, "words")
    print(number_of_chars)

    
main()