from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.check_out = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "checkout"))
        )

    def get_check_out(self):
        return self.check_out
