from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SauceDemoInventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[@class='product_sort_container']"))
        )
        self.item_prices = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='inventory_item_price']"))
        )
        self.add_to_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Add to cart')]"))
        )
        self.cart_icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))
        )

    def get_sort_dropdown(self):
        return self.sort_dropdown

    def get_item_prices(self):
        return self.item_prices

    def get_add_to_cart(self):
        return self.add_to_cart

    def get_cart_icon(self):
        return self.cart_icon
