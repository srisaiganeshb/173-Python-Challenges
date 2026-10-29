"""
String Manipulation Utilities: Duplicate Character Remover

This module provides functionalities to remove duplicate characters 
from a given string while ignoring spaces and case.
It includes three different engines:
1. A manual approach using a loop and membership checking (Accumulator pattern).
2. A Pythonic shortcut using dict.fromkeys() which preserves order.
3. A Pythonic shortcut using set() which does not preserve order.
"""

def remove_duplicate_characters(user_input: str) -> str:
    """
    Removes duplicate characters manually by checking if a character 
    already exists in the accumulator string. Preserves original order.
    """
    trimmed_str = "".join(user_input.lower().split())
    no_duplicate_char_str = ""

    for ch in trimmed_str:
        if ch not in no_duplicate_char_str:
            no_duplicate_char_str += ch
            
    return no_duplicate_char_str

def remove_duplicate_characters_shortcut(user_input: str) -> str:
    """
    Removes duplicate characters using the dict.fromkeys() method.
    This is highly efficient (O(1) lookup) and preserves insertion order.
    """
    trimmed_str = "".join(user_input.lower().split())
    return "".join(dict.fromkeys(trimmed_str))

def remove_duplicate_characters_set(user_input: str) -> set:
    """
    Removes duplicate characters by converting the string to a set.
    Note: Sets are unordered, so the original character order will be lost.
    """
    trimmed_str = "".join(user_input.lower().split())
    return "".join(set(trimmed_str))

# Execution Guard (Dashboard)
if __name__ == "__main__":
    print("\n*** Duplicate Character Remover ***")
    user_input = input("Enter a string from which only unique characters are required to be displayed: ")
    
    if user_input:
        str_without_duplicate_char = remove_duplicate_characters(user_input)
        print(f"Given string after removing the duplicate characters: '{str_without_duplicate_char}' (Manual loop)")

        str_without_duplicate_char_dict = remove_duplicate_characters_shortcut(user_input)
        print(f"Given string after removing the duplicate characters: '{str_without_duplicate_char_dict}' (using dict.fromkeys())")
        
        str_without_duplicate_char_set = remove_duplicate_characters_set(user_input)
        print(f"Given string after removing the duplicate characters: '{str_without_duplicate_char_set}' (using set())")
    else:
        print("Given string is invalid.")