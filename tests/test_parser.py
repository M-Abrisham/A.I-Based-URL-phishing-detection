import pytest

from emlscope import parser


def test_parse_stub():
    with pytest.raises(NotImplementedError):
        parser.parse("tests/fixtures/clean.eml")
