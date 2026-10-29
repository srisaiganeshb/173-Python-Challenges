# tests/test_Strings/test_q07_anagram_check.py

from Strings.q07_anagram_check import (
    anagram_check_using_sorted,
    anagram_check_using_dict,
    anagram_check_using_count,
    anagram_check_using_counter
)

def test_anagram_checks_with_valid_simple_anagrams_returns_true():
    # Arrange
    word1 = "listen"
    word2 = "silent"
    
    # Act
    result_sorted = anagram_check_using_sorted(word1, word2)
    result_dict = anagram_check_using_dict(word1, word2)
    result_count = anagram_check_using_count(word1, word2)
    result_counter = anagram_check_using_counter(word1, word2)
    
    # Assert
    assert result_sorted is True
    assert result_dict is True
    assert result_count is True
    assert result_counter is True

def test_anagram_checks_with_multi_word_and_mixed_case_returns_true():
    # Arrange
    word1 = "Rail Safety"
    word2 = "Fairy Tales"
    
    # Act
    result_sorted = anagram_check_using_sorted(word1, word2)
    result_dict = anagram_check_using_dict(word1, word2)
    result_count = anagram_check_using_count(word1, word2)
    result_counter = anagram_check_using_counter(word1, word2)
    
    # Assert
    assert result_sorted is True
    assert result_dict is True
    assert result_count is True
    assert result_counter is True

def test_anagram_checks_with_different_lengths_returns_false():
    # Arrange
    word1 = "cat"
    word2 = "catch"
    
    # Act
    result_sorted = anagram_check_using_sorted(word1, word2)
    result_dict = anagram_check_using_dict(word1, word2)
    result_count = anagram_check_using_count(word1, word2)
    result_counter = anagram_check_using_counter(word1, word2)
    
    # Assert
    assert result_sorted is False
    assert result_dict is False
    assert result_count is False
    assert result_counter is False

def test_anagram_checks_with_same_length_non_anagrams_returns_false():
    # Arrange
    word1 = "apple"
    word2 = "mango"
    
    # Act
    result_sorted = anagram_check_using_sorted(word1, word2)
    result_dict = anagram_check_using_dict(word1, word2)
    result_count = anagram_check_using_count(word1, word2)
    result_counter = anagram_check_using_counter(word1, word2)
    
    # Assert
    assert result_sorted is False
    assert result_dict is False
    assert result_count is False
    assert result_counter is False

def test_anagram_checks_with_empty_strings_returns_true():
    # Arrange
    word1 = ""
    word2 = ""
    
    # Act
    result_sorted = anagram_check_using_sorted(word1, word2)
    result_dict = anagram_check_using_dict(word1, word2)
    result_count = anagram_check_using_count(word1, word2)
    result_counter = anagram_check_using_counter(word1, word2)
    
    # Assert
    assert result_sorted is True
    assert result_dict is True
    assert result_count is True
    assert result_counter is True