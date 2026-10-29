"""
String Manipulation Utilities: Whitespace Remover

This module provides functionalities to remove all whitespace characters 
(spaces, tabs, newlines) from a given string. It includes two approaches:
1. A manual accumulator loop using the isspace() filter.
2. A Pythonic shortcut using split() and join() methods.
"""

def remove_whitespaces(user_input: str) -> str:
    """
    Removes all whitespaces manually by iterating through the string 
    and filtering out whitespace characters.
    """
    str_without_whitespaces = ""
    for char in user_input:
        if not char.isspace():
            str_without_whitespaces += char
    return str_without_whitespaces

def remove_whitespaces_using_join(user_input: str) -> str:
    """
    Removes all whitespaces using Python's built-in split() and join() methods.
    """
    return "".join(user_input.split())

if __name__ == "__main__":
    user_input = input("Enter a string in which you want to remove whitespaces: ")
    forLoop_result = remove_whitespaces(user_input)
    join_result = remove_whitespaces_using_join(user_input)


    print(f"Please find your string without whitespaces: {forLoop_result} - using for loop")
    print(f"Please find your string without whitespaces: {join_result} - using join")