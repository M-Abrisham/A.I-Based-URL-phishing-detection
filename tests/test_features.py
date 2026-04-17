import pytest

from phishing_detector import features


def test_extract_features_stub():
    with pytest.raises(NotImplementedError):
        features.extract_features("http://example.com")
