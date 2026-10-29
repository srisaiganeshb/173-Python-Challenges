# tests/test_Strings/test_q12_substring_index.py

from Strings.q12_substring_index import index_of_substring, index_of_substring_manual

# =====================================================================
# Tests for index_of_substring (Built-in .find)
# =====================================================================

def test_index_of_substring_with_word_in_middle_returns_correct_index():
    # Arrange
    main_string = "python programming"
    substring = "gram"
    
    # Act
    actual_result = index_of_substring(main_string, substring)
    
    # Assert
    assert actual_result == 10

def test_index_of_substring_with_missing_word_returns_minus_one():
    # Arrange
    main_string = "hello world"
    substring = "python"
    
    # Act
    actual_result = index_of_substring(main_string, substring)
    
    # Assert
    assert actual_result == -1

def test_index_of_substring_with_substring_longer_than_main_returns_minus_one():
    # Arrange
    main_string = "cat"
    substring = "caterpillar"
    
    # Act
    actual_result = index_of_substring(main_string, substring)
    
    # Assert
    assert actual_result == -1

def test_index_of_substring_with_empty_substring_returns_zero():
    # Arrange
    main_string = "hello"
    substring = ""
    
    # Act
    actual_result = index_of_substring(main_string, substring)
    
    # Assert
    # .find("") always returns 0 because an empty string is conceptually at the very beginning
    assert actual_result == 0

# =====================================================================
# Tests for index_of_substring_manual (Sliding Window Algorithm)
# =====================================================================

def test_index_of_substring_manual_with_word_in_middle_returns_correct_index():
    # Arrange
    main_string = "python programming"
    substring = "gram"
    
    # Act
    actual_result = index_of_substring_manual(main_string, substring)
    
    # Assert
    assert actual_result == 10

def test_index_of_substring_manual_with_multiple_occurrences_returns_first_index():
    # Arrange
    main_string = "the cat and the dog"
    substring = "the"
    
    # Act
    actual_result = index_of_substring_manual(main_string, substring)
    
    # Assert
    # Should exit early and return the index of the very first "the"
    assert actual_result == 0

def test_index_of_substring_manual_with_missing_word_returns_minus_one():
    # Arrange
    main_string = "hello world"
    substring = "python"
    
    # Act
    actual_result = index_of_substring_manual(main_string, substring)
    
    # Assert
    assert actual_result == -1

def test_index_of_substring_manual_with_substring_longer_than_main_returns_minus_one():
    # Arrange
    main_string = "cat"
    substring = "caterpillar"
    
    # Act
    actual_result = index_of_substring_manual(main_string, substring)
    
    # Assert
    assert actual_result == -1

def test_index_of_substring_manual_with_empty_substring_returns_zero():
    # Arrange
    main_string = "hello"
    substring = ""
    
    # Act
    actual_result = index_of_substring_manual(main_string, substring)
    
    # Assert
    assert actual_result == 0