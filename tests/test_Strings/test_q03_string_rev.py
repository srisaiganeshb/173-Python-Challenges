# 173-Python-Challenges/tests/test_Strings/test_q03_string_rev.py

from Strings.q03_string_rev import string_reverse, string_reverse_with_slicing

# ==========================================
# Tests for string_reverse (Manual Loop)
# ==========================================

def test_string_reverse_with_normal_word_returns_reversed():
    # Arrange
    test_input = "hello"
    
    # Act
    actual_result = string_reverse(test_input)
    
    # Assert
    assert actual_result == "olleh"

def test_string_reverse_with_palindrome_returns_same_word():
    # Arrange
    test_input = "racecar"
    
    # Act
    actual_result = string_reverse(test_input)
    
    # Assert
    assert actual_result == "racecar"

def test_string_reverse_with_spaces_and_numbers_returns_reversed():
    # Arrange
    test_input = "123 abc"
    
    # Act
    actual_result = string_reverse(test_input)
    
    # Assert
    assert actual_result == "cba 321"

def test_string_reverse_with_single_character_returns_same_character():
    # Arrange
    test_input = "A"
    
    # Act
    actual_result = string_reverse(test_input)
    
    # Assert
    assert actual_result == "A"

def test_string_reverse_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = string_reverse(test_input)
    
    # Assert
    assert actual_result == ""

# ==========================================
# Tests for string_reverse_with_slicing 
# ==========================================

def test_string_reverse_with_slicing_normal_word_returns_reversed():
    # Arrange
    test_input = "python"
    
    # Act
    actual_result = string_reverse_with_slicing(test_input)
    
    # Assert
    assert actual_result == "nohtyp"

def test_string_reverse_with_slicing_palindrome_returns_same_word():
    # Arrange
    test_input = "madam"
    
    # Act
    actual_result = string_reverse_with_slicing(test_input)
    
    # Assert
    assert actual_result == "madam"

def test_string_reverse_with_slicing_spaces_and_numbers_returns_reversed():
    # Arrange
    test_input = "x y 9"
    
    # Act
    actual_result = string_reverse_with_slicing(test_input)
    
    # Assert
    assert actual_result == "9 y x"

def test_string_reverse_with_slicing_single_character_returns_same_character():
    # Arrange
    test_input = "Z"
    
    # Act
    actual_result = string_reverse_with_slicing(test_input)
    
    # Assert
    assert actual_result == "Z"

def test_string_reverse_with_slicing_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = string_reverse_with_slicing(test_input)
    
    # Assert
    assert actual_result == ""