"""
String Manipulation Utilities: Substring Replacer

This module provides functionalities to replace all occurrences 
of a specific substring within a target string. It includes three engines:
1. A standard approach using the built-in .replace() method.
2. A manual algorithmic approach using a sliding window and dynamic step sizes.
3. An advanced pattern-matching approach using the 're' (regex) module.
"""

def replace_substring_occurrences(user_input: str, substring: str, replacement: str) -> str:
    """
    Replaces occurrences of a substring using Python's built-in string method.
    """
    return user_input.replace(substring, replacement)

def replace_substring_occurrences_manual(user_input: str, substring: str, replacement: str) -> str:
    """
    Replaces occurrences of a substring manually using a sliding window technique.
    Ensures safe index jumps to prevent infinite loops and redundant checks.
    """
    result = ""
    i = 0
    
    while i < len(user_input):
        current_stop_index = i + len(substring)
        
        # Check if the current window matches the target substring
        if user_input[i:current_stop_index] == substring:
            result += replacement
            step_size = len(substring)  # Jump past the replaced word
        else:
            result += user_input[i]
            step_size = 1               # Move forward by one character
            
        i += step_size
        
    return result

def replace_substring_occurrences_using_regex_with_flags_and_count(
    user_input: str, substring: str, replacement: str, flags=0, count=0
) -> str:
    """
    Replaces occurrences of a substring using regular expressions.
    Safely escapes special characters in the substring to prevent pattern errors.
    """
    import re
    # re.escape() acts as a defensive shield against regex special characters (like . or *)
    return re.sub(re.escape(substring), replacement, user_input, flags=flags, count=count)

# Execution Guard (Dashboard)
if __name__ == "__main__":
    print("\n*** String Replacement Utility ***")
    user_input = input("Enter a string to perform substring replacement: ")
    substring = input("Enter the substring to be replaced: ")
    replacement = input("Enter the replacement string: ")

    if not user_input or not substring:
        print("Invalid input. Please provide valid strings.")
    else:
        replaced_string = replace_substring_occurrences(user_input, substring, replacement)
        print(f"The string after replacing '{substring}' with '{replacement}' is: {replaced_string}")

        replaced_string_manual = replace_substring_occurrences_manual(user_input, substring, replacement)
        print(f"The string after manually replacing '{substring}' with '{replacement}' is: {replaced_string_manual}")

        replaced_string_regex_flags_count = replace_substring_occurrences_using_regex_with_flags_and_count(
            user_input, substring, replacement
        )
        print(f"The string after replacing '{substring}' with '{replacement}' using regex is: {replaced_string_regex_flags_count}")