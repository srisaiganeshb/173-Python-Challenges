"""
String Validation Utilities: Digits Checker

This module provides functionalities to verify if a given string 
consists entirely of numeric digits. It includes two approaches:
1. A manual fail-fast algorithm using a loop and state tracking.
2. A Pythonic shortcut using the built-in string method.
"""

def string_with_only_digits(user_input: str) -> bool:
    """
    Checks if a string contains only digits using a manual fail-fast loop.
    Includes an explicit edge-case check to handle empty strings.
    """
    if user_input:
        digits_string = True
        for char in user_input:
            if not char.isdigit():
                digits_string = False
                break
    else:
        digits_string = False
    return digits_string

def string_with_only_digits_shortcut(user_input: str) -> bool:
    """
    Checks if a string contains only digits using the built-in string method.
    """
    digits_string = user_input.isdigit()
    return digits_string

if __name__ == "__main__":
    input_string = input("Enter the string which needs to be verified whether it contains only digits: ")
    result = string_with_only_digits(input_string)
    shortcut_result = string_with_only_digits_shortcut(input_string)

    if(result):
        print(f"{input_string} has only digits in it.")
    else:
        print(f"{input_string} is not a digits-only string.")

    if(shortcut_result):
        print(f"{input_string} has only digits in it - using shortcut method.")
    else:
        print(f"{input_string} is not a digits-only string - using shortcut method.")
