# opens text file and returns the contents as a string
def get_book_file(filepath):
    with open(filepath) as f:
        return f.read()

def get_book_word_count(book_text):
    word_count = book_text.split()
    return len(word_count)

def get_char_count(book_text):
    char_count = {}
    lower_case_book_text = book_text.lower()
    for char in lower_case_book_text:
        if char not in char_count:
            char_count.update({char:1})
        else:
            char_count[char] += 1
    return(char_count)

def print_report(word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(char_count)

