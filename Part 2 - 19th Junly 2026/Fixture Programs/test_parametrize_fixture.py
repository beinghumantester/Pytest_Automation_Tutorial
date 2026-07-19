import pytest


# 3. Parameterized Fixture
# Run the same test multiple times using different inputs.

#example - 1

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def browser(request):
    return request.param

def test_browser(browser):
    print(browser)

# Example 2
import pytest

@pytest.fixture(params=[10, 20, 30])
def number(request):
    return request.param

def test_number(number):
    if number%2==0:
        print("Number is even.")
    else:
        print("Number is odd.")
