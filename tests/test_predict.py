import pytest

from phishing_detector import predict


def test_predict_stub():
    with pytest.raises(NotImplementedError):
        predict.predict("http://example.com")
