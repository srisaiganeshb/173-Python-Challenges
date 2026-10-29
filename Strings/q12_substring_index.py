"""
String Searching Utilities: Substring Index Finder

This module provides functionalities to find the starting index 
of the first occurrence of a substring within a main string.
It includes a standard built-in approach and a manual sliding window approach.
"""

def index_of_substring(main_string: str, substring: str) -> int:
    """
    Finds the index of the first occurrence of a substring using the built-in .find() method.
    Returns -1 if the substring is not found.
    """
    return main_string.find(substring)

def index_of_substring_manual(main_string: str, substring: str) -> int:
    """
    Finds the index of the first occurrence of a substring using a manual sliding window.
    Time Complexity: O(N * M) where N is main_string length and M is substring length.
    """
    i = 0
    # Boundary check: Stop when the remaining string is shorter than the substring
    while i <= len(main_string) - len(substring):
        current_stop_index = i + len(substring)
        
        # Slicing the window and comparing
        if main_string[i:current_stop_index] == substring:
            return i  # Early exit on first match
            
        i += 1
        
    return -1

if __name__ == "__main__":
    print("\n*** First Occurrence Index Finder ***")
    main_string = input("Enter a string: ")
    
    if main_string:
        sub_string = input("Enter a substring to find its index: ")
        
        if sub_string:
            index = index_of_substring(main_string, sub_string)
            if index != -1:
                print(f"The index of the first instance of '{sub_string}' in '{main_string}' is: {index} (Built-in)")
            else:
                print("Given substring is not found in the main string (Built-in).")
            
            index_manual = index_of_substring_manual(main_string, sub_string)
            if index_manual != -1:
                print(f"The index of the first instance of '{sub_string}' in '{main_string}' is: {index_manual} (Manual)")
            else:
                print("Given substring is not found in the main string (Manual).")
                
        else:
            print("\nGiven substring is invalid (empty).")
    else:
        print("\nGiven string is invalid (empty).")