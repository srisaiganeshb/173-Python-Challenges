# 173-Python-Challenges/tests/test_Strings/test_q01_palindrome.py

from Strings.q01_palindrome import palindrome_check, palindrome_check_with_slicing

# ==========================================
# Tests for palindrome_check (Two-Pointer)
# ==========================================

def test_palindrome_check_with_valid_palindrome_returns_true():
    # Arrange
    test_input = "racecar"
    
    # Act
    actual_result = palindrome_check(test_input)
    
    # Assert
    assert actual_result == True

def test_palindrome_check_with_mixed_case_palindrome_returns_true():
    # Arrange
    test_input = "RaceCar"
    
    # Act
    actual_result = palindrome_check(test_input)
    
    # Assert
    assert actual_result == True

def test_palindrome_check_with_non_palindrome_returns_false():
    # Arrange
    test_input = "hello"
    
    # Act
    actual_result = palindrome_check(test_input)
    
    # Assert
    assert actual_result == False

def test_palindrome_check_with_empty_string_returns_true():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = palindrome_check(test_input)
    
    # Assert
    assert actual_result == True

# ==========================================
# Tests for palindrome_check_with_slicing
# ==========================================

def test_palindrome_check_with_slicing_valid_palindrome_returns_true():
    # Arrange
    test_input = "level"
    
    # Act
    actual_result = palindrome_check_with_slicing(test_input)
    
    # Assert
    assert actual_result == True

def test_palindrome_check_with_slicing_mixed_case_palindrome_returns_true():
    # Arrange
    test_input = "Level"
    
    # Act
    actual_result = palindrome_check_with_slicing(test_input)
    
    # Assert
    assert actual_result == True

def test_palindrome_check_with_slicing_non_palindrome_returns_false():
    # Arrange
    test_input = "python"
    
    # Act
    actual_result = palindrome_check_with_slicing(test_input)
    
    # Assert
    assert actual_result == False

def test_palindrome_check_with_slicing_empty_string_returns_true():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = palindrome_check_with_slicing(test_input)
    
    # Assert
    assert actual_result == True