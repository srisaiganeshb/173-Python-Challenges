"""
String Formatting Utilities: Case Converter

This module provides functionalities to convert a given string 
into its uppercase and lowercase formats simultaneously.
"""

def str_upper_lower(user_input: str) -> tuple:
    """
    Converts the input string to both uppercase and lowercase.
    Returns a tuple containing (uppercase_version, lowercase_version).
    """

    uppercase_str = user_input.upper()
    lowercase_str = user_input.lower()
    return uppercase_str, lowercase_str

if __name__ == "__main__":
    print("\n*** String Conversion to Uppercase and Lowercase ***")
    user_input = input("Enter a string to convert to uppercase and Lowercase:")

    if not user_input:
        print("Invalid input. Please provide a valid string.")
    else:
        uppercase, lowercase = str_upper_lower(user_input)
        print(f"The uppercase version of the given string is: {uppercase} \nThe lowercase version of the given string is: {lowercase}")