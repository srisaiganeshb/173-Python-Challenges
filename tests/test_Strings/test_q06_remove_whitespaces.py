# tests/test_Strings/test_q06_remove_whitespaces.py

from Strings.q06_remove_whitespaces import remove_whitespaces, remove_whitespaces_using_join

# ==========================================
# Tests for remove_whitespaces (Manual Loop)
# ==========================================

def test_remove_whitespaces_with_normal_spaces_removes_them():
    # Arrange
    test_input = "Hello World Python"
    
    # Act
    actual_result = remove_whitespaces(test_input)
    
    # Assert
    assert actual_result == "HelloWorldPython"

def test_remove_whitespaces_with_tabs_and_newlines_removes_all():
    # Arrange
    test_input = "Data\tScience\nRocks"
    
    # Act
    actual_result = remove_whitespaces(test_input)
    
    # Assert
    assert actual_result == "DataScienceRocks"

def test_remove_whitespaces_with_leading_and_trailing_spaces_removes_them():
    # Arrange
    test_input = "   Spaced Out   "
    
    # Act
    actual_result = remove_whitespaces(test_input)
    
    # Assert
    assert actual_result == "SpacedOut"

def test_remove_whitespaces_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = remove_whitespaces(test_input)
    
    # Assert
    assert actual_result == ""

def test_remove_whitespaces_with_only_spaces_returns_empty():
    # Arrange
    test_input = "   \t \n  "
    
    # Act
    actual_result = remove_whitespaces(test_input)
    
    # Assert
    assert actual_result == ""

def test_remove_whitespaces_with_no_spaces_returns_original_string():
    # Arrange
    test_input = "CompactString"
    
    # Act
    actual_result = remove_whitespaces(test_input)
    
    # Assert
    assert actual_result == "CompactString"

# ==========================================
# Tests for remove_whitespaces_using_join 
# ==========================================

def test_remove_whitespaces_using_join_with_normal_spaces_removes_them():
    # Arrange
    test_input = "Hello World Python"
    
    # Act
    actual_result = remove_whitespaces_using_join(test_input)
    
    # Assert
    assert actual_result == "HelloWorldPython"

def test_remove_whitespaces_using_join_with_tabs_and_newlines_removes_all():
    # Arrange
    test_input = "Data\tScience\nRocks"
    
    # Act
    actual_result = remove_whitespaces_using_join(test_input)
    
    # Assert
    assert actual_result == "DataScienceRocks"

def test_remove_whitespaces_using_join_with_leading_and_trailing_spaces_removes_them():
    # Arrange
    test_input = "   Spaced Out   "
    
    # Act
    actual_result = remove_whitespaces_using_join(test_input)
    
    # Assert
    assert actual_result == "SpacedOut"

def test_remove_whitespaces_using_join_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = remove_whitespaces_using_join(test_input)
    
    # Assert
    assert actual_result == ""

def test_remove_whitespaces_using_join_with_only_spaces_returns_empty():
    # Arrange
    test_input = "   \t \n  "
    
    # Act
    actual_result = remove_whitespaces_using_join(test_input)
    
    # Assert
    assert actual_result == ""

def test_remove_whitespaces_using_join_with_no_spaces_returns_original_string():
    # Arrange
    test_input = "CompactString"
    
    # Act
    actual_result = remove_whitespaces_using_join(test_input)
    
    # Assert
    assert actual_result == "CompactString"