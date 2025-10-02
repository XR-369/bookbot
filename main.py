import sys
from stats import (
        count_words,
        character_count,
        chars_dict_to_sorted_list
)


def main():
    """
    Main function to read and print the contents of second argument of sys.argv.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print_report(book_path, num_words, chars_sorted_list)

    

def get_book_text(filepath):
    """
    Reads the contents of a file and returns them as a single string.
    Args:
        filepath (str): The path to the file to be read.
    Returns:
        str: The entire content of the file as a string
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()



