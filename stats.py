# opens text file and returns the contents as a string
def get_book_file(filepath):
    with open(filepath) as f:
        return f.read()

# Returns total word count for the file inputted
def get_book_word_count(book_text):
    word_count = book_text.split()
    return len(word_count)

# Loops through the file text, adding each chharacter to a dictonary then returns dictonary
def get_char_count(book_text):
    char_count = {}
    lower_case_book_text = book_text.lower()
    for char in lower_case_book_text:
        if char not in char_count:
            char_count.update({char:1})
        else:
            char_count[char] += 1
    return char_count

def sort_on(d):
    return d["num"]

# Turns the dictonary returned in get_char_count and sorts it ready for printing
def char_sorted_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

