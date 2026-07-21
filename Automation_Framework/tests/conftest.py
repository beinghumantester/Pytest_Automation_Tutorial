import pytest

from selenium import webdriver

@pytest.fixture(params=["chrome","edge"])
def driver(request):
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()