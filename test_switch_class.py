import pytest
from switch_class import switch


def test_initialize():
    default = 'not found'
    myswitch = switch(default)
    assert myswitch.default_return_value == default
