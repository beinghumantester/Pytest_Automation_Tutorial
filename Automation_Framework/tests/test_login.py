from pages.login_file import LoginPage
# from utils.screenshot import capturescreenshot

def test_login(driver):
    LoginPage.login(driver)

  #  capturescreenshot(driver,"test_login")

  #pytest_runtest_makereport
 #my test case failed -> yes capture the screenshot 



 