# tests/test_Strings/test_q17_remove_duplicate_char.py

from Strings.q17_remove_duplicate_char import (
    remove_duplicate_characters,
    remove_duplicate_characters_shortcut,
    remove_duplicate_characters_set
)

# ==========================================
# Tests for remove_duplicate_characters (Manual)
# ==========================================

def test_remove_duplicate_characters_with_duplicates_returns_unique_ordered():
    # Arrange
    test_input = "apple"
    
    # Act
    actual_result = remove_duplicate_characters(test_input)
    
    # Assert
    assert actual_result == "aple"

def test_remove_duplicate_characters_with_mixed_case_and_spaces_returns_normalized_unique():
    # Arrange
    test_input = "P r o G r a m m i n g"
    
    # Act
    actual_result = remove_duplicate_characters(test_input)
    
    # Assert
    # Spaces should be removed, case should be lowered, duplicates removed in order
    assert actual_result == "progamin"

def test_remove_duplicate_characters_with_no_duplicates_returns_same_string_lowered():
    # Arrange
    test_input = "abc"
    
    # Act
    actual_result = remove_duplicate_characters(test_input)
    
    # Assert
    assert actual_result == "abc"

def test_remove_duplicate_characters_with_empty_string_returns_empty():
    # Arrange
    test_input = "   "
    
    # Act
    actual_result = remove_duplicate_characters(test_input)
    
    # Assert
    assert actual_result == ""


# ==========================================
# Tests for remove_duplicate_characters_shortcut (dict.fromkeys)
# ==========================================

def test_remove_duplicate_characters_shortcut_with_duplicates_returns_unique_ordered():
    # Arrange
    test_input = "banana"
    
    # Act
    actual_result = remove_duplicate_characters_shortcut(test_input)
    
    # Assert
    assert actual_result == "ban"

def test_remove_duplicate_characters_shortcut_with_mixed_case_and_spaces_returns_normalized_unique():
    # Arrange
    test_input = "B a N a n A"
    
    # Act
    actual_result = remove_duplicate_characters_shortcut(test_input)
    
    # Assert
    assert actual_result == "ban"

def test_remove_duplicate_characters_shortcut_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = remove_duplicate_characters_shortcut(test_input)
    
    # Assert
    assert actual_result == ""


# ==========================================
# Tests for remove_duplicate_characters_set (set)
# ==========================================

def test_remove_duplicate_characters_set_returns_unordered_unique_characters():
    # Arrange
    test_input = "apple"
    
    # Act
    actual_result = remove_duplicate_characters_set(test_input)
    
    # Assert
    # Since sets are unordered, we sort both sides to verify it contains the correct unique letters
    assert sorted(actual_result) == sorted("aple")

def test_remove_duplicate_characters_set_with_mixed_case_and_spaces():
    # Arrange
    test_input = "A p p L e"
    
    # Act
    actual_result = remove_duplicate_characters_set(test_input)
    
    # Assert
    assert sorted(actual_result) == sorted("aple")

def test_remove_duplicate_characters_set_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = remove_duplicate_characters_set(test_input)
    
    # Assert
    assert actual_result == ""