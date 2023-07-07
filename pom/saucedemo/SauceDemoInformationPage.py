from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))
        )
        self.last_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-test='lastName']"))
        )
        self.zip_code = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']"))
        )
        self.continue_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "continue"))
        )

    def get_firstname(self):
        return self.firstname

    def get_last_name(self):
        return self.last_name

    def get_zip_code(self):
        return self.zip_code

    def get_continue_button(self):
        return self.continue_button
