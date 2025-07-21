from stats import *
import sys

def main():
    file_path = sys.argv[1]
    book_file = file_path
    book_text = get_book_file(book_file)
    word_count = get_book_word_count(book_text)
    char_count = get_char_count(book_text)
    char_sorted = char_sorted_list(char_count)
    print_report(book_file, word_count, char_sorted)


def print_report(book_file, word_count, char_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()