# Create 3 files inside the tests folder as the conftest.py created inside tests folder is accessible across all the test files.

# Code of conftest.py file
import pytest

@pytest.fixture
def browser():
    return "Chrome Browser"

# Code of test_login.py file
def test_login(browser):
    assert browser == "Chrome Browser"


# Code of test_dashboard.py file
def test_dashboard(browser):
    assert browser == "Chrome Browser"