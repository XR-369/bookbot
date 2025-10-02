def count_words(text_from_book):
  """
  Counts the number of words in a given string of text.
  Args:
    text_from_book: The input text as a string.
  Returns:
    The number of words in the string.
  """
  words = text_from_book.split()  # Splits the string by whitespace into a list of words
  return len(words)


def character_count(text):
    """
    Counts the number of times each character (including symbols and spaces)
    appears in the given string.
    Args:
        text (str): The input string from the book.
    Returns:
        dict: A dictionary where keys are characters and values are their counts.
    """
    char_counts = {}
    text = text.lower()
    for char in text:
        char_counts[char] = char_counts.get(char, 0) +1
    
    return char_counts

    """
     ------MODEL ONE------
    # Create a list of formatted strings, sorted by count descending

    """ 
   ## sorted_counts = [
   ##     f"{char}: {count}"
   ##     for char, count in sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
   ## ]
    
   ## return "\n".join(sorted_counts)

"""
------MODEL TWO------
# Usually the cleanest method is this:

"""
# First, we create a "sort_on" function:

def sort_on(d):
    return d["num"]


# Then, we create a new function called "def chars_dict_to_sorted_list":

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


