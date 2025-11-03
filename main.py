import sys
from stats import number_of_words
from stats import num_of_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(path):
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(text)} total words")
    print("--------- Character Count -------")
    char_dict = sort_dict(num_of_char(text))
    for c in char_dict:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])