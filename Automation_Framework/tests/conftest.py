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

from utils.screenshot import capturescreenshot
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield

    report = outcome.get_result()

    if report.when=='call' and report.failed: 
        driver = item.funcargs.get("driver")
        if driver:
             capturescreenshot(driver,item.name)