"""
String Manipulation Utilities: Character Occurrences Counter

This module provides functionalities to count the number of times 
a specific character appears in a given string. It includes three 
different O(N) approaches:
1. Hash Map / Counter method.
2. Built-in string count method.
3. Manual iteration using a for loop.
"""

from collections import Counter

def char_instances_counter(user_str_input: str, user_char_input: str) -> int:
    """
    Counts the number of instances of a specific character using collections.Counter.
    Time Complexity: O(N) - Suitable for long strings.
    """
    user_str_input = user_str_input.lower()
    
    # Counter creates a hash map of all characters. We use .get() to fetch 
    # the target character's count, defaulting to 0 if it doesn't exist.
    return Counter(user_str_input).get(user_char_input.lower(), 0)

def char_instances_count(user_str_input: str, user_char_input: str) -> int:
    """
    Counts the number of instances of a specific character using the built-in .count() method.
    Time Complexity: O(N) - Suitable for long strings.
    """
    # .count() is highly optimized in C, making it practically the fastest approach here
    user_str_input = user_str_input.lower()
    return user_str_input.count(user_char_input.lower())

def char_instances_count_using_loop(user_str_input: str, user_char_input: str) -> int:
    """
    Counts the number of instances of a specific character using a manual for loop.
    Time Complexity: O(N) - Suitable for long strings.
    """
    user_str_input = user_str_input.lower()
    count = 0
    
    # Iterate through each character and increment the accumulator if it matches the target
    for char in user_str_input:
        if char == user_char_input.lower():
            count += 1
            
    return count

if __name__ == "__main__":
    print("\n*** Character Occurrences Counter ***")
    string_input = input("Enter a string: ")
    char_input = input("Enter a character to know its count in the given string: ")

    # Defensive Programming: Handle empty inputs to prevent unexpected errors
    if not string_input or not char_input:
        print("Invalid input. Please provide valid inputs for both a string and a character.")
        
    # Edge Case Validation: Restrict target input to a single character.
    # Why? Because .count() can count substrings (e.g., "ab"), whereas Counter 
    # and the manual loop strictly compare single characters. This ensures 
    # consistent behavior across all three implementations.
    elif len(char_input) != 1:
        print("Invalid input. Please enter only a single character.")
        
    else:
        char_Counter = char_instances_counter(string_input, char_input)
        char_count = char_instances_count(string_input, char_input)
        char_count_loop = char_instances_count_using_loop(string_input, char_input)

        print(f"The character '{char_input}' appears {char_Counter} times in the given string - using Counter")
        print(f"The character '{char_input}' appears {char_count} times in the given string - using count")
        print(f"The character '{char_input}' appears {char_count_loop} times in the given string - using for loop")