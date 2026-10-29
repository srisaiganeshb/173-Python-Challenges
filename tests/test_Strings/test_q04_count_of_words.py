# tests/test_Strings/test_q04_count_of_words.py

from Strings.q04_count_of_words import words_counter

def test_words_counter_with_normal_sentence_returns_correct_count():
    # Arrange
    test_input = "Python is a great language"
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 5

def test_words_counter_with_multiple_spaces_between_words_ignores_extra_spaces():
    # Arrange
    test_input = "Python    is       great"
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 3

def test_words_counter_with_leading_and_trailing_spaces_ignores_them():
    # Arrange
    test_input = "   Hello World   "
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 2

def test_words_counter_with_empty_string_returns_zero():
    # Arrange
    test_input = ""
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 0

def test_words_counter_with_only_spaces_returns_zero():
    # Arrange
    test_input = "       "
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 0

def test_words_counter_with_alphanumeric_and_special_characters_treats_them_as_words():
    # Arrange
    test_input = "Hello 123 !@# testing"
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 4

def test_words_counter_with_single_word_returns_one():
    # Arrange
    test_input = "Supercalifragilisticexpialidocious"
    
    # Act
    actual_count = words_counter(test_input)
    
    # Assert
    assert actual_count == 1