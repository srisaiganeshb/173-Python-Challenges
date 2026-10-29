"""
String Utilities: Prefix Verification

This module provides functionalities to verify if a main string 
starts with a specific prefix. It includes a Pythonic approach 
using built-in methods and a manual slicing approach, both 
implemented with case-insensitivity.
"""

def verify_prefix(given_string: str, given_prefix: str) -> bool:
    """
    Checks if the string starts with the specified prefix using the built-in method.
    Comparison is case-insensitive.
    """
    return given_string.lower().startswith(given_prefix.lower())

def verify_prefix_manual(given_string: str, given_prefix: str) -> bool:
    """
    Checks if the string starts with the specified prefix using manual index slicing.
    Comparison is case-insensitive.
    """
    return given_string.lower()[0:len(given_prefix)] == given_prefix.lower()

if __name__ == "__main__":
    print("\n*** String Prefix Verifier ***")
    given_string = input("Enter a string: ")
    
    # Input validation (Edge Case Handling)
    if given_string:
        given_prefix = input("Enter the prefix to verify: ")
        
        if given_prefix:
            # Built-in Method
            if verify_prefix(given_string, given_prefix):
                print(f"'{given_prefix}' is the prefix of the given string (Built-in).")
            else:
                print(f"'{given_prefix}' is not the prefix of the given string (Built-in).")

            # Manual Slicing
            if verify_prefix_manual(given_string, given_prefix):
                print(f"'{given_prefix}' is the prefix of the given string (Manual).")
            else:
                print(f"'{given_prefix}' is not the prefix of the given string (Manual).")
        else:
            print("Given prefix is invalid (empty).")
    else:
        print("Given string is invalid (empty).")