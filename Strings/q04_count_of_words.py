"""
Text Processing Utilities: Word Counter

This module provides functionalities to analyze text data.
It includes a core function to count the total number of words 
in a given string by tokenizing it based on whitespace.
"""

def words_counter(user_input: str)-> int:
    """
    Counts the number of words in a string.
    Automatically handles leading/trailing spaces and multiple spaces between words.
    """
    user_input = user_input.strip().split()
    total_words = len(user_input)
    return total_words

if __name__ == "__main__":
    print("\n*** Word Counter ***")
    input_string = input("Enter a string to count the number of words: ")

    total_words = words_counter(input_string)

    print(f"Total number of words in the given string: {total_words}")