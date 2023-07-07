from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoCheckOutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.thank_you_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[@class='complete-header']"))
        )
        self.back_home = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Back Home']"))
        )

    def get_thank_you_header(self):
        return self.thank_you_header

    def get_back_home(self):
        return self.back_home
