# tests/test_Strings/test_q08_char_instances_count.py

from Strings.q08_char_instances_count import (
    char_instances_counter,
    char_instances_count,
    char_instances_count_using_loop
)

# ==========================================
# Tests for char_instances_counter (Hash Map)
# ==========================================

def test_char_instances_counter_with_mixed_case_returns_correct_count():
    # Arrange
    test_string = "AppLe and baNanA"
    target_char = "a"
    
    # Act
    actual_count = char_instances_counter(test_string, target_char)
    
    # Assert
    # 'A' in AppLe, 'a' in and, 'a', 'a', 'A' in baNanA -> Total 5
    assert actual_count == 5

def test_char_instances_counter_missing_character_returns_zero():
    # Arrange
    test_string = "Python Programming"
    target_char = "z"
    
    # Act
    actual_count = char_instances_counter(test_string, target_char)
    
    # Assert
    assert actual_count == 0

def test_char_instances_counter_with_empty_string_returns_zero():
    # Arrange
    test_string = ""
    target_char = "a"
    
    # Act
    actual_count = char_instances_counter(test_string, target_char)
    
    # Assert
    assert actual_count == 0

# ==========================================
# Tests for char_instances_count (.count() built-in)
# ==========================================

def test_char_instances_count_with_mixed_case_returns_correct_count():
    # Arrange
    test_string = "AppLe and baNanA"
    target_char = "A"
    
    # Act
    actual_count = char_instances_count(test_string, target_char)
    
    # Assert
    assert actual_count == 5

def test_char_instances_count_with_spaces_returns_correct_count():
    # Arrange
    test_string = "  three spaces  "
    target_char = " "
    
    # Act
    actual_count = char_instances_count(test_string, target_char)
    
    # Assert
    assert actual_count == 4

def test_char_instances_count_missing_character_returns_zero():
    # Arrange
    test_string = "Python"
    target_char = "x"
    
    # Act
    actual_count = char_instances_count(test_string, target_char)
    
    # Assert
    assert actual_count == 0

# ==========================================
# Tests for char_instances_count_using_loop (Manual loop)
# ==========================================

def test_char_instances_count_using_loop_with_mixed_case_returns_correct_count():
    # Arrange
    test_string = "AppLe and baNanA"
    target_char = "n"
    
    # Act
    actual_count = char_instances_count_using_loop(test_string, target_char)
    
    # Assert
    # 'n' in and, 'N', 'n' in baNanA -> Total 3
    assert actual_count == 3

def test_char_instances_count_using_loop_with_special_characters_returns_correct_count():
    # Arrange
    test_string = "Hello @ world @@ 2026!"
    target_char = "@"
    
    # Act
    actual_count = char_instances_count_using_loop(test_string, target_char)
    
    # Assert
    assert actual_count == 3

def test_char_instances_count_using_loop_with_empty_string_returns_zero():
    # Arrange
    test_string = ""
    target_char = "b"
    
    # Act
    actual_count = char_instances_count_using_loop(test_string, target_char)
    
    # Assert
    assert actual_count == 0