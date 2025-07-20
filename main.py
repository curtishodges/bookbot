from stats import *

def main():
    book_text = get_book_file("books/frankenstein.txt")
    print_report(get_book_word_count(book_text), get_char_count(book_text))


main()