# tests/test_Strings/test_q02_vowels_consonants_count.py

from Strings.q02_vowels_consonants_count import count_vowels_consonants

def test_count_vowels_consonants_with_mixed_text():
    # Arrange
    test_input = "Hello World 123!"
    
    # Act
    vowels, consonants = count_vowels_consonants(test_input)
    
    # Assert
    # Vowels: e, o, o (3) | Consonants: H, l, l, W, r, l, d (7)
    assert vowels == 3
    assert consonants == 7

def test_count_vowels_consonants_with_only_vowels_mixed_case():
    # Arrange
    test_input = "AEIOUaeiou"
    
    # Act
    vowels, consonants = count_vowels_consonants(test_input)
    
    # Assert
    assert vowels == 10
    assert consonants == 0

def test_count_vowels_consonants_with_only_consonants():
    # Arrange
    test_input = "bCdfGhjK"
    
    # Act
    vowels, consonants = count_vowels_consonants(test_input)
    
    # Assert
    assert vowels == 0
    assert consonants == 8

def test_count_vowels_consonants_with_symbols_and_numbers():
    # Arrange
    test_input = "@#123 456!!!"
    
    # Act
    vowels, consonants = count_vowels_consonants(test_input)
    
    # Assert
    # Numbers and symbols should be completely ignored
    assert vowels == 0
    assert consonants == 0

def test_count_vowels_consonants_with_empty_string():
    # Arrange
    test_input = ""
    
    # Act
    vowels, consonants = count_vowels_consonants(test_input)
    
    # Assert
    assert vowels == 0
    assert consonants == 0