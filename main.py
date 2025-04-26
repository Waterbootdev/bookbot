import sys

from stats import get_word_count, get_printable_char_counts
from prints import print_bookbot

def get_book_text(path_to_book):

    with open(path_to_book) as file:
        return file.read()

def main():

    if len(sys.argv) < 2:
        print_program_usage()
    else:
        # read the book
        path_to_book = sys.argv[1]
        read_anylize_ptrint_book(path_to_book)

def print_program_usage():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def read_anylize_ptrint_book(path_to_book):
    book_text = get_book_text(path_to_book)

    # analize book conten's 
    word_count = get_word_count(book_text)
    printable_char_counts = get_printable_char_counts(book_text)

    # print report  
    print_bookbot(path_to_book, word_count, printable_char_counts)

main()