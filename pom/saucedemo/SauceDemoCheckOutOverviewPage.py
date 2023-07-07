from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoCheckOutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.total_amount = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_info_label summary_total_label']"))
        )
        self.finish = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Finish']"))
        )

    def get_total_amount(self):
        return self.total_amount

    def get_finish(self):
        return self.finish
