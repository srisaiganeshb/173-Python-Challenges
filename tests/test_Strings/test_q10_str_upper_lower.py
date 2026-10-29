# tests/test_Strings/test_q10_str_upper_lower.py

from Strings.q10_str_upper_lower import str_upper_lower

def test_str_upper_lower_with_mixed_case_returns_correct_tuple():
    # Arrange
    test_input = "PyThOn"
    
    # Act
    uppercase, lowercase = str_upper_lower(test_input)
    
    # Assert
    assert uppercase == "PYTHON"
    assert lowercase == "python"

def test_str_upper_lower_with_all_lowercase_returns_correct_tuple():
    # Arrange
    test_input = "hello"
    
    # Act
    uppercase, lowercase = str_upper_lower(test_input)
    
    # Assert
    assert uppercase == "HELLO"
    assert lowercase == "hello"

def test_str_upper_lower_with_numbers_and_special_characters():
    # Arrange
    test_input = "123!@#aBc"
    
    # Act
    uppercase, lowercase = str_upper_lower(test_input)
    
    # Assert
    assert uppercase == "123!@#ABC"
    assert lowercase == "123!@#abc"

def test_str_upper_lower_with_empty_string_returns_empty_strings():
    # Arrange
    test_input = ""
    
    # Act
    uppercase, lowercase = str_upper_lower(test_input)
    
    # Assert
    assert uppercase == ""
    assert lowercase == ""