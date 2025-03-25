import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform():
    # Test round-trip transformation works correctly
    test_cases = ['banana', 'hello', 'a', 'abracadabra']
    
    for text in test_cases:
        bwt = burrows_wheeler_transform(text)
        # Validate BWT properties
        assert len(bwt) >= len(text)
        assert '$' in bwt
        
        # Verify round-trip transformation
        reconstructed = inverse_burrows_wheeler_transform(bwt)
        assert len(reconstructed) == len(text)
        # Verify characters match exactly (crucial!)
        assert reconstructed == text

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