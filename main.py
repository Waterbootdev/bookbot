from stats import get_num_words, get_num_characters, to_sorted_char_count_list, filter_printable
from prints import print_bookbot

def get_book_text(path_to_book):

    with open(path_to_book) as file:
        return file.read()



def main():

    #read the book
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)

    #count inside the book
    number_of_words = get_num_words(book_text)
    number_of_chars = filter_printable(to_sorted_char_count_list(get_num_characters(book_text)))

    #print counts
    #print_count_message(number_of_words, "words")
    
    print_bookbot(path_to_book, number_of_words, number_of_chars)

main()