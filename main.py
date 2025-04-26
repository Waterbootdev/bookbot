from stats import get_num_words

def get_book_text(path_to_book):

    with open(path_to_book) as file:
        return file.read()

def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    number_of_words = get_num_words(book_text)
    message = f"{number_of_words} words found in the document"
    print(message)

main()