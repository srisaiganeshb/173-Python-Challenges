"""
String Manipulation Utilities: String Length Calculator

This module provides functionalities to determine the length of a string 
without using the built-in len() function. It includes a manual iterative 
approach and an advanced approach using hash map frequency aggregation.
"""
def string_length_manually(user_input: str) -> int:
    """
    Calculates the length of a string using a manual for-loop.
    Time Complexity: O(N)
    """

    count = 0
    for char in user_input:
        count +=1
    return count

def string_length_using_counter(user_input: str) -> int:
    """
    Calculates the length of a string by summing the frequency values 
    from a Counter hash map.
    Time Complexity: O(N)
    """
    from collections import Counter

    char_frequency_dict = Counter(user_input)
    return sum(char_frequency_dict.values()) 

if __name__ == "__main__":
    print("\n*** String Length Counter Without Using len() ***")
    user_input = input("Enter a string to know its length: ")

    if not user_input:
        print("Invalid input. Please provide a valid string.")
    else:
        manual_length = string_length_manually(user_input)
        print(f"The length of the given string is: {manual_length} - using manual counting")
        counter_length = string_length_using_counter(user_input)
        print(f"The length of the given string is: {counter_length} - using Counter")