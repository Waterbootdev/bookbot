from stats import get_num_words, get_printable_char_counts
from prints import print_bookbot

def get_book_text(path_to_book):

    with open(path_to_book) as file:
        return file.read()



def main():

    # read the book
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)

    # analize book conten's 
    number_of_words = get_num_words(book_text)
    number_of_chars = get_printable_char_counts(book_text)

    # print report  
    print_bookbot(path_to_book, number_of_words, number_of_chars)

main()