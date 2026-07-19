import pytest


#2. Fixture Chaining
#One fixture depends on another fixture.

#example - 1


@pytest.fixture
def username():
    return "Ujjwal"

@pytest.fixture
def greeting(username):
    return f"Hello {username}"

def test_message(greeting):
    assert greeting == "Hello Ujjwal"

# Example 2


@pytest.fixture
def database():
    return "Database Connected"

@pytest.fixture
def employee(database):
    return f"Employee loaded using {database}"

def test_employee(employee):
    assert employee == "Employee loaded using Database Connected"