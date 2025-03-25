import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform():
    # Test round-trip transformation works correctly
    test_cases = ['banana', 'hello', 'a', 'abracadabra']
    
    for text in test_cases:
        bwt = burrows_wheeler_transform(text)
        assert inverse_burrows_wheeler_transform(bwt) == text

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

def test_bwt_properties():
    # Check basic properties of BWT
    test_cases = ['banana', 'hello world', 'abracadabra', 'xyz']
    
    for text in test_cases:
        bwt = burrows_wheeler_transform(text)
        
        # BWT should be same length as input
        assert len(bwt) == len(text) + 1
        
        # BWT should include terminator character
        assert '$' in bwt
        
        # Inverse transform should restore original text
        reconstructed = inverse_burrows_wheeler_transform(bwt)
        assert reconstructed == text