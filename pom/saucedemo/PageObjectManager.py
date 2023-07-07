from  .SauceDemoCartPage import SauceDemoCartPage
from .SauceDemoCheckOutCompletePage import SauceDemoCheckOutCompletePage
from .SauceDemoCheckOutOverviewPage import SauceDemoCheckOutOverviewPage
from .SauceDemoInformationPage import SauceDemoInformationPage
from .SauceDemoInventoryPage import SauceDemoInventoryPage
from .SauceDemoLoginPage import SauceDemoLoginPage


class PageObjectManager:

    def __init__(self, driver):
        self.driver = driver
        self.s = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None

    def get_sauce_demo_login_page(self):
        self.s5 = SauceDemoLoginPage(self.driver)
        return self.s5

    def get_sauce_demo_inventory_page(self):
        self.s4 = SauceDemoInventoryPage(self.driver)
        return self.s4

    def get_sauce_demo_information_page(self):
        self.s3 = SauceDemoInformationPage(self.driver)
        return self.s3

    def get_sauce_demo_checkout_overview_page(self):
        self.s2 = SauceDemoCheckOutOverviewPage(self.driver)
        return self.s2

    def get_sauce_demo_checkout_complete_page(self):
        self.s1 = SauceDemoCheckOutCompletePage(self.driver)
        return self.s1

    def get_sauce_demo_cart_page(self):
        self.s = SauceDemoCartPage(self.driver)
        return self.s
