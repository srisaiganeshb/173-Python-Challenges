"""
Palindrome Checker Utilities

This module provides functions to verify whether a given string is a palindrome.
It includes two different implementations:
1. A Two-Pointer algorithm approach (with early exit).
2. A Pythonic string slicing approach.
"""

def palindrome_check(user_input: str) -> bool:
    """
    Checks if a given string is a palindrome using the Two-Pointer algorithm.
    """
    l_index = 0
    r_index = len(user_input) - 1
    is_palindrome = True
    user_input = user_input.lower()

    while(l_index < r_index):
        if(user_input[l_index] != user_input[r_index]):
            is_palindrome = False
            break
        l_index +=1
        r_index -=1

    return is_palindrome

def palindrome_check_with_slicing(user_input: str) -> bool:
    """
    Checks if a given string is a palindrome using string slicing.
    """
    user_input = user_input.lower()
    is_palindrome = user_input == user_input[::-1]
    return is_palindrome

if __name__ == "__main__":
    word = input("Enter the word to be verified: ")
    is_palindrome = palindrome_check(word)
    sliced_palindrome_status = palindrome_check_with_slicing(word)

    if(is_palindrome):
        print(word+" is a palindrome - using while loop")
    else:
        print(word+" is not a palindrome - using while loop")

    if(sliced_palindrome_status):
        print(word+" is a palindrome - using slicing")
    else:
        print(word+" is not a palindrome - using slicing")