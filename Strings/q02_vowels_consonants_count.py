"""
Text Processing Utilities: Vowel and Consonant Counter

This module provides functionalities to analyze text data.
It includes a core function to calculate the total number of vowels 
and consonants in a given string, completely ignoring numbers, 
spaces, and special characters.
"""

def count_vowels_consonants(user_input: str) -> tuple[int, int]:
    v, c = 0, 0
    vowels = "aeiou"
    user_input = user_input.lower()

    for char in user_input:
        if char.isalpha():
            if(char in vowels):
                v+=1
            else:
                c+=1
    return v, c

if __name__ == "__main__":
    word = input("\n***Vowels and Consonants Counter***\nEnter the word: ")
    v, c = count_vowels_consonants(word)
    print(f"Total vowels: {v}\nTotal consonants: {c}")