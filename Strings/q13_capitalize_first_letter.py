"""
String Manipulation Utilities: Capitalize Words

This module provides functionalities to capitalize the first letter 
of each word in a given string. It includes both a manual algorithmic 
approach and a Pythonic built-in approach.
"""

def capitalize_first_letter(user_input: str) -> str:
    """
    Capitalizes the first letter of each word using Python's built-in .title() method.
    """
    return user_input.title()


def capitalize_first_letter_manual(user_input: str) -> str:
    """
    Capitalizes the first letter of each word manually by splitting the string,
    applying .capitalize() to each token, and joining them back together.
    """
    capitalized_words_list = []
    
    for word in user_input.split():
        capitalized_words_list.append(word.capitalize())
        
    return " ".join(capitalized_words_list)


if __name__ == "__main__":
    print("\n*** Word Capitalization Utility ***")
    user_input = input("Enter a string to capitalize the first letter of every word: ")
    
    if user_input.strip():
        updated_str = capitalize_first_letter(user_input)
        print(f"Updated string (built-in): {updated_str}")

        updated_str_manual = capitalize_first_letter_manual(user_input)
        print(f"Updated string (manual): {updated_str_manual}")
    else:
        print("Given string is invalid or empty.")