import pytest

# 4. Scoped Fixture
# Function Scope


@pytest.fixture(scope="function")
def setup():
    print("\nSetup")
    yield
    print("Teardown")

def test_one(setup):
    print("Test One")

def test_two(setup):
    print("Test Two")


# Module Scope


@pytest.fixture(scope="module")
def database():
    print("\nConnecting Database")
    yield
    print("Disconnecting Database")

def test_insert(database):
    print("Insert Record")

def test_update(database):
    print("Update Record")


# Class Scope


@pytest.fixture(scope="class")
def browser():
    print("\nLaunching Browser")
    yield
    print("Closing Browser")

class TestLogin:

    def test_login(self, browser):
        print("Login Test")

    def test_logout(self, browser):
        print("Logout Test")


# Session Scope


@pytest.fixture(scope="session")
def application():
    print("\nStarting Application")
    yield
    print("Closing Application")

def test_home(application):
    print("Home Page")

def test_profile(application):
    print("Profile Page")
