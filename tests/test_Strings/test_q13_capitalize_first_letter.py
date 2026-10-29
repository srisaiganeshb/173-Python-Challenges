# tests/test_Strings/test_q13_capitalize_first_letter.py

from Strings.q13_capitalize_first_letter import capitalize_first_letter, capitalize_first_letter_manual

# =====================================================================
# Tests for capitalize_first_letter (Built-in .title() method)
# =====================================================================

def test_capitalize_first_letter_with_normal_sentence_returns_title_case():
    # Arrange
    test_input = "hello world"
    
    # Act
    actual_result = capitalize_first_letter(test_input)
    
    # Assert
    assert actual_result == "Hello World"

def test_capitalize_first_letter_with_mixed_case_returns_normalized_title_case():
    # Arrange
    test_input = "pYtHoN is fUn"
    
    # Act
    actual_result = capitalize_first_letter(test_input)
    
    # Assert
    assert actual_result == "Python Is Fun"

def test_capitalize_first_letter_with_multiple_spaces_preserves_spaces():
    # Arrange
    test_input = "hello   world"
    
    # Act
    actual_result = capitalize_first_letter(test_input)
    
    # Assert
    assert actual_result == "Hello   World"

def test_capitalize_first_letter_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = capitalize_first_letter(test_input)
    
    # Assert
    assert actual_result == ""


# =====================================================================
# Tests for capitalize_first_letter_manual (Manual split and capitalize)
# =====================================================================

def test_capitalize_first_letter_manual_with_normal_sentence_returns_title_case():
    # Arrange
    test_input = "hello world"
    
    # Act
    actual_result = capitalize_first_letter_manual(test_input)
    
    # Assert
    assert actual_result == "Hello World"

def test_capitalize_first_letter_manual_with_mixed_case_returns_normalized_title_case():
    # Arrange
    test_input = "pYtHoN is fUn"
    
    # Act
    actual_result = capitalize_first_letter_manual(test_input)
    
    # Assert
    assert actual_result == "Python Is Fun"

def test_capitalize_first_letter_manual_with_multiple_spaces_collapses_spaces():
    # Arrange
    test_input = "hello   world"
    
    # Act
    actual_result = capitalize_first_letter_manual(test_input)
    
    # Assert
    # .split() removes extra spaces, and " ".join() puts a single space back
    assert actual_result == "Hello World"

def test_capitalize_first_letter_manual_with_empty_string_returns_empty():
    # Arrange
    test_input = ""
    
    # Act
    actual_result = capitalize_first_letter_manual(test_input)
    
    # Assert
    assert actual_result == ""