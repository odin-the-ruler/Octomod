import re

def get_valid_words(letters, pattern, word_list):
    """
    Get valid words that match the given pattern and can be formed using the given letters.
    
    :param letters: String of available letters
    :param pattern: Pattern to match (with underscores for unknown letters)
    :param word_list: List of valid words
    :return: List of valid words that match the pattern
    """
    try:
        pattern = pattern.lower()
        word_length = len(pattern)
        letters = letters.lower()
        possible_words = []

        # Create regex pattern from the given pattern
        regex_pattern = "^" + pattern.replace("_", ".") + "$"

        # Filter words from nltk's word list that match the length and regex pattern
        for word in word_list:
            if len(word) == word_length and re.match(regex_pattern, word):
                if all(word.count(l) <= letters.count(l) for l in set(word)):
                    possible_words.append(word)

        return possible_words if possible_words else ""
    except Exception as e:
        print(f"An error occurred in get_valid_words: {e}")
        return ""

def format_string(input_str):
    """
    Format the input string to extract and join letters.
    
    :param input_str: Input string containing letters
    :return: Formatted string of letters in uppercase
    """
    try:
        # Split the input string into parts
        parts = input_str.split()

        # Remove the first two elements (the number and the word "letter")
        letters = parts[2:]

        # Convert to uppercase and join
        result = "".join(letters).upper()

        return result
    except Exception as e:
        print(f"An error occurred in format_string: {e}")
        return ""
