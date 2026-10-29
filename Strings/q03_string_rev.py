"""
String Manipulation Utilities: String Reverser

This module provides functionalities to reverse a given string.
It includes two different implementations:
1. A manual approach using a for loop (Accumulator pattern).
2. A Pythonic approach using built-in string slicing.
"""

def string_reverse(user_input: str) -> str:
    rev_of_input = ""
    for char in user_input:
        rev_of_input = char + rev_of_input
    return rev_of_input

def string_reverse_with_slicing(user_input: str) -> str:
    return user_input[::-1]

if __name__ == "__main__":
    word = input("Enter the word to be reversed: ")
    rev_word = string_reverse(word)
    rev_word_slicing = string_reverse_with_slicing(word)

    print(f"Reverse of {word} is {rev_word} - without slicing")
    print(f"Reverse of {word} is {rev_word_slicing} - with slicing")