# tests/test_Strings/test_q14_verify_prefix.py

from Strings.q14_verify_prefix import verify_prefix, verify_prefix_manual

# =====================================================================
# Tests for verify_prefix (Built-in Method)
# =====================================================================

def test_verify_prefix_valid_prefix_returns_true():
    # Arrange
    main_string = "python programming"
    prefix = "pyth"
    
    # Act
    result = verify_prefix(main_string, prefix)
    
    # Assert
    assert result == True

def test_verify_prefix_case_insensitive_returns_true():
    # Arrange
    main_string = "Python Programming"
    prefix = "pyTH"
    
    # Act
    result = verify_prefix(main_string, prefix)
    
    # Assert
    assert result == True

def test_verify_prefix_invalid_prefix_returns_false():
    # Arrange
    main_string = "java programming"
    prefix = "pyth"
    
    # Act
    result = verify_prefix(main_string, prefix)
    
    # Assert
    assert result == False

def test_verify_prefix_empty_prefix_returns_true():
    # Arrange
    main_string = "hello"
    prefix = ""
    
    # Act
    # In Python, any string technically starts with an empty string
    result = verify_prefix(main_string, prefix)
    
    # Assert
    assert result == True

def test_verify_prefix_prefix_longer_than_string_returns_false():
    # Arrange
    main_string = "py"
    prefix = "python"
    
    # Act
    result = verify_prefix(main_string, prefix)
    
    # Assert
    assert result == False

# =====================================================================
# Tests for verify_prefix_manual (Manual Slicing Method)
# =====================================================================

def test_verify_prefix_manual_valid_prefix_returns_true():
    # Arrange
    main_string = "python programming"
    prefix = "pyth"
    
    # Act
    result = verify_prefix_manual(main_string, prefix)
    
    # Assert
    assert result == True

def test_verify_prefix_manual_case_insensitive_returns_true():
    # Arrange
    main_string = "Python Programming"
    prefix = "pyTH"
    
    # Act
    result = verify_prefix_manual(main_string, prefix)
    
    # Assert
    assert result == True

def test_verify_prefix_manual_invalid_prefix_returns_false():
    # Arrange
    main_string = "java programming"
    prefix = "pyth"
    
    # Act
    result = verify_prefix_manual(main_string, prefix)
    
    # Assert
    assert result == False

def test_verify_prefix_manual_empty_prefix_returns_true():
    # Arrange
    main_string = "hello"
    prefix = ""
    
    # Act
    result = verify_prefix_manual(main_string, prefix)
    
    # Assert
    assert result == True