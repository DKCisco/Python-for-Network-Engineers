import pytest

@pytest.fixture
def my_info():
    with open("myinfo.txt") as f:
        content = f.read()
    return content

def test_one(my_info):
    assert "tiger" in my_info


def test_two(my_info):
    assert "zeebra" in my_info


