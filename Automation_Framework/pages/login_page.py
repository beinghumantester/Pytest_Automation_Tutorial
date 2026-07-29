from selenium.webdriver.common.by import By
import time
from utils.logger import get_logger
from test_data.login_data import url
from pages.dashboard_page import DashboardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger=get_logger()
class LoginPage:

    
    @staticmethod

    def login(driver,username,password):

        driver.get(url)
       # time.sleep(3) 
        
       

        WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.NAME, "username")))
        logger.debug("Entering Username")

        driver.find_element(By.NAME, "username").send_keys(username)
        logger.debug("Entering password")
        driver.find_element(By.NAME, "password").send_keys(password)
        logger.debug("Clicking button")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver,15).until(EC.url_contains("dashboard"))

        assert  driver.current_url =="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

        return DashboardPage(driver) 

       


