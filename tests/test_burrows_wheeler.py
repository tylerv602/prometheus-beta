import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform():
    # Comprehensive test cases covering various scenarios
    test_cases = [
        'banana', 
        'hello', 
        'a', 
        'abracadabra', 
        'python',
        'compression'
    ]
    
    for text in test_cases:
        # Perform BWT
        bwt = burrows_wheeler_transform(text)
        
        # Validate BWT properties
        assert len(bwt) == len(text) + 1
        assert '$' in bwt
        
        # Perform inverse transform
        reconstructed = inverse_burrows_wheeler_transform(bwt)
        
        # Verify character count preservation
        assert len(reconstructed) == len(text)
        assert sorted(reconstructed) == sorted(text)

def test_error_handling():
    # Test type errors
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        inverse_burrows_wheeler_transform(123)
    
    # Test empty string errors
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform('')
    
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        inverse_burrows_wheeler_transform('')

def test_edge_cases():
    # Test single character
    single_char = 'a'
    bwt = burrows_wheeler_transform(single_char)
    reconstructed = inverse_burrows_wheeler_transform(bwt)
    assert len(reconstructed) == len(single_char)
    assert reconstructed == single_char

    # Test repeated characters
    repeated_chars = 'aaa'
    bwt = burrows_wheeler_transform(repeated_chars)
    reconstructed = inverse_burrows_wheeler_transform(bwt)
    assert len(reconstructed) == len(repeated_chars)
    assert reconstructed == repeated_chars