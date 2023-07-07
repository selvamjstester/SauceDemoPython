from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        self.password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        self.login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='login-button']"))
        )

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.password

    def get_login_button(self):
        return self.login_button
