from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    admin_cta = (By.CSS_SELECTOR,"a[href='/web/index.php/admin/viewAdminModule']")

    def __init__(self, driver):
        self.driver =driver 


    def admin_cta_click(self):
            WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.admin_cta)).click()
            time.sleep(5)
