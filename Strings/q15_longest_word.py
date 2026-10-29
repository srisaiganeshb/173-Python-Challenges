"""
String Manipulation Utilities: Longest Word Finder

This module provides functionalities to identify the longest word(s) within a given string.
It includes three distinct implementations:
1. A manual accumulator pattern to track and return the first longest word.
2. A robust manual approach that handles length ties by accumulating all longest words into a list.
3. A highly optimized Pythonic approach using the built-in max() function with a custom key.
"""

def longest_word(user_input: str) -> str:
    """
    Finds the first longest word in a string using manual state tracking.
    """
    longest_word_length = 0
    longest_word_result = ""
    
    for word in user_input.split():
        if longest_word_length < len(word):
            longest_word_length = len(word)
            longest_word_result = word
            
    return longest_word_result


def longest_words_list(user_input: str) -> list:
    """
    Finds all longest words in a string, dynamically replacing or appending 
    to a list to safely handle multiple words of the same maximum length.
    """
    longest_word_length = 0
    longest_words = []
    
    for word in user_input.split():
        if longest_word_length < len(word):
            longest_word_length = len(word)
            longest_words = [word]
        elif len(word) == longest_word_length:
            longest_words.append(word)
            
    return longest_words


def longest_word_using_max(user_input: str) -> str:
    """
    Finds the longest word utilizing Python's built-in max() function 
    with 'len' as the sorting key.
    """
    return max(user_input.split(), key=len)


# Execution Guard (Dashboard)
if __name__ == "__main__":
    print("\n*** Longest Word Finder ***")
    user_input = input("Enter a string: ")
    
    if user_input.strip():
        longest_word_in_string = longest_word(user_input)
        print(f"'{longest_word_in_string}' is the longest word in the given string - manual")

        longest_word_through_max = longest_word_using_max(user_input)
        print(f"'{longest_word_through_max}' is the longest word in the given string - max()")

        longest_word_through_list = longest_words_list(user_input)
        print(f"Longest word/s in the given string: {longest_word_through_list}")
    else:
        print("Given string is invalid or empty.")