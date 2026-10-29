# tests/test_Strings/test_q09_str_length_without_len.py

from Strings.q09_str_length_without_len_method import string_length_manually, string_length_using_counter

# --- Tests for string_length_manually ---

def test_string_length_manually_with_normal_string_returns_correct_length():
    # Arrange
    test_input = "Hello World"
    
    # Act
    actual_length = string_length_manually(test_input)
    
    # Assert
    assert actual_length == 11

def test_string_length_manually_with_empty_string_returns_zero():
    # Arrange
    test_input = ""
    
    # Act
    actual_length = string_length_manually(test_input)
    
    # Assert
    assert actual_length == 0

def test_string_length_manually_with_special_characters_and_spaces():
    # Arrange
    test_input = "  @#123 "
    
    # Act
    actual_length = string_length_manually(test_input)
    
    # Assert
    assert actual_length == 8

# --- Tests for string_length_using_counter ---

def test_string_length_using_counter_with_normal_string_returns_correct_length():
    # Arrange
    test_input = "Python"
    
    # Act
    actual_length = string_length_using_counter(test_input)
    
    # Assert
    assert actual_length == 6

def test_string_length_using_counter_with_empty_string_returns_zero():
    # Arrange
    test_input = ""
    
    # Act
    actual_length = string_length_using_counter(test_input)
    
    # Assert
    assert actual_length == 0

def test_string_length_using_counter_with_special_characters_and_spaces():
    # Arrange
    test_input = "  @#123 "
    
    # Act
    actual_length = string_length_using_counter(test_input)
    
    # Assert
    assert actual_length == 8