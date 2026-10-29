# tests/test_Strings/test_q11_replace_substring.py

from Strings.q11_replace_substring import (
    replace_substring_occurrences,
    replace_substring_occurrences_manual,
    replace_substring_occurrences_using_regex_with_flags_and_count,
)

# =====================================================================
# Tests for replace_substring_occurrences (Built-in .replace)
# =====================================================================

def test_replace_substring_occurrences_with_normal_words_returns_replaced_string():
    # Arrange
    user_input = "hello world, hello python"
    substring = "hello"
    replacement = "hi"
    
    # Act
    actual_result = replace_substring_occurrences(user_input, substring, replacement)
    
    # Assert
    assert actual_result == "hi world, hi python"

def test_replace_substring_occurrences_with_missing_substring_returns_original_string():
    # Arrange
    user_input = "hello world"
    substring = "python"
    replacement = "java"
    
    # Act
    actual_result = replace_substring_occurrences(user_input, substring, replacement)
    
    # Assert
    assert actual_result == "hello world"

# =====================================================================
# Tests for replace_substring_occurrences_manual (Sliding Window)
# =====================================================================

def test_replace_substring_occurrences_manual_with_normal_words_returns_replaced_string():
    # Arrange
    user_input = "cat bat cat"
    substring = "cat"
    replacement = "dog"
    
    # Act
    actual_result = replace_substring_occurrences_manual(user_input, substring, replacement)
    
    # Assert
    assert actual_result == "dog bat dog"

def test_replace_substring_occurrences_manual_with_overlapping_pattern():
    # Arrange
    user_input = "aaaaa"
    substring = "aa"
    replacement = "b"
    
    # Act
    actual_result = replace_substring_occurrences_manual(user_input, substring, replacement)
    
    # Assert
    assert actual_result == "bba"

def test_replace_substring_occurrences_manual_with_missing_substring_returns_original_string():
    # Arrange
    user_input = "hello"
    substring = "z"
    replacement = "x"
    
    # Act
    actual_result = replace_substring_occurrences_manual(user_input, substring, replacement)
    
    # Assert
    assert actual_result == "hello"

# =====================================================================
# Tests for replace_substring_occurrences_using_regex_with_flags_and_count
# =====================================================================

def test_replace_substring_using_regex_with_normal_words_returns_replaced_string():
    # Arrange
    user_input = "good morning, good night"
    substring = "good"
    replacement = "great"
    
    # Act
    actual_result = replace_substring_occurrences_using_regex_with_flags_and_count(
        user_input, substring, replacement
    )
    
    # Assert
    assert actual_result == "great morning, great night"

def test_replace_substring_using_regex_with_special_characters_is_safely_escaped():
    # Arrange
    user_input = "price is $5.00. yes, $5.00."
    substring = "$5.00"
    replacement = "five dollars"
    
    # Act
    actual_result = replace_substring_occurrences_using_regex_with_flags_and_count(
        user_input, substring, replacement
    )
    
    # Assert
    assert actual_result == "price is five dollars. yes, five dollars."

def test_replace_substring_using_regex_with_count_limit_replaces_only_specified_occurrences():
    # Arrange
    user_input = "a a a a"
    substring = "a"
    replacement = "b"
    count_limit = 2
    
    # Act
    actual_result = replace_substring_occurrences_using_regex_with_flags_and_count(
        user_input, substring, replacement, count=count_limit
    )
    
    # Assert
    assert actual_result == "b b a a"