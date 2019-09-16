import pytest


@pytest.fixture
def fix():
    fix = 1
    return fix


def test():
    assert 1 == 1
