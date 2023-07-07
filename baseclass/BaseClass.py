import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import Select


class BaseClass:
    driver = None
    ac = None
    s = None

    @staticmethod
    def browser_launch(name):
        if name.lower() == "chrome":
            chrome_service = ChromeService(executable_path="C:\Users\Welcome\eclipse-workspace\Sauce_Demo_Python_Project\Driver\chromedriver.exe")
            driver = webdriver.Chrome(service=chrome_service)
            driver.maximize_window()
        elif name.lower() == "edge":
            edge_service = EdgeService(executable_path="C:\Users\Welcome\eclipse-workspace\Sauce_Demo_Python_Project\Driver\msedgedriver.exe")
            driver = webdriver.Edge(service=edge_service)
            driver.maximize_window()

        BaseClass.driver = driver
        return driver

    @staticmethod
    def get_url(url):
        BaseClass.driver.get(url)

    @staticmethod
    def alert_handling(command):
        if command.lower() == "ok":
            BaseClass.driver.switch_to.alert.accept()
        elif command.lower() == "cancel":
            BaseClass.driver.switch_to.alert.dismiss()

    @staticmethod
    def alert_insert_value(value):
        BaseClass.driver.switch_to.alert.send_keys(value)

    @staticmethod
    def mouse_hover(element):
        ac = ActionChains(BaseClass.driver)
        ac.move_to_element(element).perform()

    @staticmethod
    def right_click(element):
        ac = ActionChains(BaseClass.driver)
        ac.context_click(element).perform()

    @staticmethod
    def select_by_visible_text(element, text):
        s = Select(element)
        s.select_by_visible_text(text)

    @staticmethod
    def select_by_value(element, value):
        s = Select(element)
        s.select_by_value(value)

    @staticmethod
    def select_by_index(element, index):
        s = Select(element)
        s.select_by_index(index)

    @staticmethod
    def take_screenshot(driver, file_name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(os.getcwd(), "screenshots", f"{file_name}_{timestamp}""\.png")
        driver.save_screenshot(file_path)
        return file_path

