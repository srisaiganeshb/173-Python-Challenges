"""
String Utilities: String Rotation Verifier

This module provides functionalities to check if two strings are 
rotations of each other using an optimized concatenation approach.
"""

def verify_rotations_of_strings(string1: str, string2: str) -> bool:
    """
    Checks if string2 is a rotation of string1.
    Time Complexity: O(N) using the (A + A) substring search trick.
    """
    # Fail-fast: Rotations must have the exact same length
    # If lengths match, check if string2 exists within the doubled string1
    return len(string2) == len(string1) and string2 in (string1 + string1)


if __name__ == "__main__":
    print("\n*** String Rotation Verifier ***")
    string1 = input("Enter the first string: ")
    
    # Defensive programming: Checking for empty strings
    if string1:
        string2 = input("Enter the second string: ")
        
        if string2:
            result = verify_rotations_of_strings(string1, string2)
            
            if result:
                print("Given strings are rotations of each other.")
            else:
                print("Given strings are not rotations of each other.")
        else:
            print("Given string2 is invalid (empty).")
    else:
        print("Given string1 is invalid (empty).")