# tests/test_Strings/test_q15_longest_word.py

import pytest
from Strings.q15_longest_word import (
    longest_word,
    longest_words_list,
    longest_word_using_max
)

# --- Tests for longest_word (Manual) ---

def test_longest_word_with_clear_longest_returns_correct_word():
    # Arrange
    test_input = "I love programming in Python"
    
    # Act
    actual_result = longest_word(test_input)
    
    # Assert
    assert actual_result == "programming"

def test_longest_word_with_length_tie_returns_first_encountered():
    # Arrange
    test_input = "a big cat"
    
    # Act
    actual_result = longest_word(test_input)
    
    # Assert
    # 'big' and 'cat' are both length 3, but 'big' comes first
    assert actual_result == "big"

def test_longest_word_with_empty_string_returns_empty_string():
    # Arrange
    test_input = "   "
    
    # Act
    actual_result = longest_word(test_input)
    
    # Assert
    assert actual_result == ""


# --- Tests for longest_words_list (List Accumulator) ---

def test_longest_words_list_with_clear_longest_returns_single_item_list():
    # Arrange
    test_input = "I love programming in Python"
    
    # Act
    actual_result = longest_words_list(test_input)
    
    # Assert
    assert actual_result == ["programming"]

def test_longest_words_list_with_length_tie_returns_all_longest_words():
    # Arrange
    test_input = "a big cat"
    
    # Act
    actual_result = longest_words_list(test_input)
    
    # Assert
    # Should contain both words of length 3
    assert actual_result == ["big", "cat"]

def test_longest_words_list_with_empty_string_returns_empty_list():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = longest_words_list(test_input)
    
    # Assert
    assert actual_result == []


# --- Tests for longest_word_using_max (Built-in) ---

def test_longest_word_using_max_with_clear_longest_returns_correct_word():
    # Arrange
    test_input = "I love programming in Python"
    
    # Act
    actual_result = longest_word_using_max(test_input)
    
    # Assert
    assert actual_result == "programming"

def test_longest_word_using_max_with_length_tie_returns_first_encountered():
    # Arrange
    test_input = "a big cat"
    
    # Act
    actual_result = longest_word_using_max(test_input)
    
    # Assert
    assert actual_result == "big"

def test_longest_word_using_max_with_empty_string_raises_value_error():
    # Arrange
    test_input = "   "
    
    # Act & Assert
    # max() on an empty sequence raises ValueError. 
    # We use pytest.raises to expect this exact behavior and pass the test.
    with pytest.raises(ValueError):
        longest_word_using_max(test_input)