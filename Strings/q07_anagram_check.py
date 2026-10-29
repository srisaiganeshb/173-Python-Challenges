"""
String Validation Utilities: Anagram Checker

This module provides functionalities to verify if two given strings are anagrams 
(i.e., they contain the exact same characters in the exact same quantities).
It includes four different algorithmic implementations for comparison:
1. Sorting approach (using sorted()).
2. Manual Hash Map / Dictionary approach (frequency counting).
3. Nested iteration approach (using the string .count() method).
4. Pythonic standard approach (using collections.Counter).
"""

# Professional standard: Imports should always be at the top of the file
from collections import Counter

def anagram_check_using_sorted(user_input1: str, user_input2: str) -> bool:
    """
    Checks for anagrams by sorting the characters of both strings.
    Time Complexity: O(N log N).
    """
    user_input1 = ("".join(user_input1.split())).lower()
    user_input2 = ("".join(user_input2.split())).lower()

    if len(user_input1) != len(user_input2):
        return False
        
    return sorted(user_input1) == sorted(user_input2)

def anagram_check_using_dict(user_input1: str, user_input2: str) -> bool:
    """
    Checks for anagrams by manually counting character frequencies using dictionaries.
    Time Complexity: O(N) - Highly optimized for large strings.
    """
    user_input1 = ("".join(user_input1.split())).lower()
    user_input2 = ("".join(user_input2.split())).lower()

    if len(user_input1) != len(user_input2):
        return False
        
    str1_char_count1 = {}
    str2_char_count2 = {}
    
    for char in user_input1:
        str1_char_count1[char] = str1_char_count1.get(char, 0) + 1
        
    for char in user_input2:
        str2_char_count2[char] = str2_char_count2.get(char, 0) + 1
        
    return str1_char_count1 == str2_char_count2

def anagram_check_using_count(user_input1: str, user_input2: str) -> bool:
    """
    Checks for anagrams using the built-in string .count() method.
    Time Complexity: O(N^2) - Suitable for short strings only.
    """
    user_input1 = ("".join(user_input1.split())).lower()
    user_input2 = ("".join(user_input2.split())).lower()

    if len(user_input1) != len(user_input2):
        return False
        
    for char in user_input1:
        if user_input1.count(char) != user_input2.count(char):
            return False
            
    return True

def anagram_check_using_counter(user_input1: str, user_input2: str) -> bool:
    """
    Checks for anagrams using the highly optimized collections.Counter class.
    This is the industry standard for rapid frequency counting.
    """
    user_input1 = ("".join(user_input1.split())).lower()
    user_input2 = ("".join(user_input2.split())).lower()

    return Counter(user_input1) == Counter(user_input2)

# Execution Guard (Dashboard)
if __name__ == "__main__":
    print("\n*** Anagram Checker ***")
    word1 = input("Enter the first word to be verified: ")
    word2 = input("Enter the second word to be verified: ")

    # Engine Calls
    anagram_sorted_result = anagram_check_using_sorted(word1, word2)
    anagram_dict_result = anagram_check_using_dict(word1, word2)
    anagram_count_result = anagram_check_using_count(word1, word2)
    anagram_counter_result = anagram_check_using_counter(word1, word2)
    
    # Output Display
    print("\n--- Results ---")
    if anagram_sorted_result:
        print(f"'{word1}' and '{word2}' are anagrams - using sorted")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams - using sorted")

    if anagram_dict_result:
        print(f"'{word1}' and '{word2}' are anagrams - using dictionary")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams - using dictionary")

    if anagram_count_result:
        print(f"'{word1}' and '{word2}' are anagrams - using count")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams - using count")

    if anagram_counter_result:
        print(f"'{word1}' and '{word2}' are anagrams - using counter")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams - using counter")