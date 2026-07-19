import pytest

#1. Return Fixture
#Provides reusable data to test cases.

#example - 1


@pytest.fixture
def user():
    return {
        "name": "Ujjwal",
        "role": "Tester"
    }

def test_user_name(user):
    assert user["name"] == "Ujjwal"

def test_user_role(user):
    assert user["role"] == "Tester"

#example - 2

@pytest.fixture
def numbers():
    return [10, 20, 30]

def test_total(numbers):
    assert sum(numbers) == 60

def test_count(numbers):
    assert len(numbers) == 3