# tests/test_Strings/test_q16_rotations_of_each_other.py

from Strings.q16_rotations_of_each_other import verify_rotations_of_strings

def test_verify_rotations_valid_rotation_returns_true():
    # Arrange
    string1 = "waterbottle"
    string2 = "erbottlewat"
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    assert actual_result == True

def test_verify_rotations_same_string_returns_true():
    # Arrange
    string1 = "hello"
    string2 = "hello"
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    assert actual_result == True

def test_verify_rotations_invalid_rotation_same_length_returns_false():
    # Arrange
    string1 = "hello"
    string2 = "holle"
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    assert actual_result == False

def test_verify_rotations_different_lengths_returns_false():
    # Arrange
    string1 = "hello"
    string2 = "helloo"
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    assert actual_result == False

def test_verify_rotations_both_empty_strings_returns_true():
    # Arrange
    string1 = ""
    string2 = ""
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    # Two empty strings are technically identical, hence valid rotations of length 0.
    assert actual_result == True

def test_verify_rotations_one_empty_string_returns_false():
    # Arrange
    string1 = "hello"
    string2 = ""
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    assert actual_result == False

def test_verify_rotations_with_spaces_and_special_chars_returns_true():
    # Arrange
    string1 = "a b c!"
    string2 = "c!a b "
    
    # Act
    actual_result = verify_rotations_of_strings(string1, string2)
    
    # Assert
    assert actual_result == True