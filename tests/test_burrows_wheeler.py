import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform():
    # Test basic transformation
    assert burrows_wheeler_transform('banana') == 'annb$aa'
    
    # Test single character
    assert burrows_wheeler_transform('a') == 'a$'
    
    # Test string with repeated characters
    assert burrows_wheeler_transform('hello') == 'ell$ho'

def test_inverse_burrows_wheeler_transform():
    # Test basic inverse transformation
    assert inverse_burrows_wheeler_transform('annb$aa') == 'banana'
    
    # Test single character
    assert inverse_burrows_wheeler_transform('a$') == 'a'
    
    # Test string with repeated characters
    assert inverse_burrows_wheeler_transform('ell$ho') == 'hello'

def test_round_trip_transformation():
    # Test round trip transformation works correctly for various inputs
    test_strings = [
        'banana', 
        'hello world', 
        'abracadabra', 
        'a', 
        'xyz'
    ]
    
    for original in test_strings:
        bwt = burrows_wheeler_transform(original)
        reconstructed = inverse_burrows_wheeler_transform(bwt)
        assert reconstructed == original, f"Failed for input: {original}"

def test_error_handling():
    # Test type errors
    with pytest.raises(TypeError):
        burrows_wheeler_transform(123)
    
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(123)
    
    # Test empty string errors
    with pytest.raises(ValueError):
        burrows_wheeler_transform('')
    
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform('')