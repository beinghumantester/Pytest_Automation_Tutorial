import pytest

# 5. Autouse Fixture

# Runs automatically before every test.



@pytest.fixture(autouse=True)
def setup():
    print("\nBefore Test")
    yield
    print("After Test")

def test_login():
    print("Executing Login Test")

def test_dashboard():
    print("Executing Dashboard Test")



# Example 2
import pytest

counter = 0

@pytest.fixture(autouse=True)
def increment():
    global counter
    counter += 1

def test_one():
    print(counter)

def test_two():
    print(counter)