# tests/test_Strings/test_q05_digits_string.py

from Strings.q05_digits_string import string_with_only_digits, string_with_only_digits_shortcut

def test_string_with_only_digits_valid_numbers_returns_true():
    # Arrange
    test_input = "1234567890"
    
    # Act
    actual_result = string_with_only_digits(test_input)
    
    # Assert
    assert actual_result == True

def test_string_with_only_digits_mixed_characters_returns_false():
    # Arrange
    test_input = "123a45"
    
    # Act
    actual_result = string_with_only_digits(test_input)
    
    # Assert
    assert actual_result == False

def test_string_with_only_digits_special_characters_returns_false():
    # Arrange
    test_input = "123!45"
    
    # Act
    actual_result = string_with_only_digits(test_input)
    
    # Assert
    assert actual_result == False

def test_string_with_only_digits_empty_string_returns_false():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = string_with_only_digits(test_input)
    
    # Assert
    assert actual_result == False

def test_string_with_only_digits_shortcut_valid_numbers_returns_true():
    # Arrange
    test_input = "98765"
    
    # Act
    actual_result = string_with_only_digits_shortcut(test_input)
    
    # Assert
    assert actual_result == True

def test_string_with_only_digits_shortcut_mixed_characters_returns_false():
    # Arrange
    test_input = "987b65"
    
    # Act
    actual_result = string_with_only_digits_shortcut(test_input)
    
    # Assert
    assert actual_result == False

def test_string_with_only_digits_shortcut_empty_string_returns_false():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = string_with_only_digits_shortcut(test_input)
    
    # Assert
    assert actual_result == False