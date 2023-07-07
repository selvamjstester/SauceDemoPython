import time

import pytest
from pytest_bdd import given, when, then

from baseclass.BaseClass import BaseClass
from pom.saucedemo import PageObjectManager


pom = PageObjectManager
    
class StepDefinition(BaseClass):
        
    
@given('I am on the Demo Login Page')
def step_given_i_am_on_the_demo_login_page(context):
BaseClass.driver.get('https://www.saucedemo.com')

@when('I fill the account information for account StandardUser into the UserName field and the PassWord field')
def step_when_i_fill_account_info_for_standard_user(context):
    username = context.table[0]['standard_user']
    password = context.table[0]['secret_sauce']
    pom.getSauceDemoLoginPage().getUserName().send_keys(username)
    pom.getSauceDemoLoginPage().getPassword().send_keys(password)

@when('I click the Login Button')
def step_when_i_click_the_login_button(context):
    pom.getSauceDemoLoginPage().getLoginButton().click()

@then('I am redirected to the Demo Main Page')
def step_then_i_am_redirected_to_the_demo_main_page(context):
    expected_url = 'https://www.saucedemo.com/inventory.html'
    actual_url = context.driver.current_url
    assert actual_url == expected_url

@then('I verify the App Logo exists')
def step_then_i_verify_the_app_logo_exists(context):
    app_logo = context.driver.find_element_by_xpath('//div[@class="app_logo"]')
    assert app_logo.is_displayed()

@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def step_when_i_fill_account_info_for_locked_out_user(context):
    username = 'locked_out_user'
    password = 'secret_sauce'
    pom.getSauceDemoLoginPage().getUserName().send_keys(username)
    pom.getSauceDemoLoginPage().getPassword().send_keys(password)

@then('I verify the Error Message contains the text {error_text}')
def step_then_i_verify_error_message_contains_text(context, error_text):
    error_msg = context.driver.find_element_by_xpath('//h3[@data-test="error"]')
    actual_error_text = error_msg.text
    assert actual_error_text == error_text

@given('I am on the inventory page')
def step_given_i_am_on_the_inventory_page(context):
    context.driver.get('https://www.saucedemo.com/inventory.html')

@when('user sorts products from low price to high price')
def step_when_user_sorts_products_from_low_price_to_high_price(context):
    sort = "Price (low to high)"
    pom.getSauceDemoInventoryPage().getSortDropdown().send_keys(sort)

@when('user adds lowest priced product')
def step_when_user_adds_lowest_priced_product(context):
    items_prices = pom.getSauceDemoInventoryPage().getItemPrices()
    lowest_value = None
    add_to_cart_button = None

    for item in items_prices:
        text = item.text
        value = text.replace("$", "")
        item_value = float(value)

        if lowest_value is None or item_value < lowest_value:
            lowest_value = item_value
            time.sleep(1)
            add_to_cart_button = item.find_element_by_xpath(".//ancestor::div[@class='inventory_item']//button")

    add_to_cart_button.click()

@when('user clicks on cart')
def step_when_user_clicks_on_cart(context):
    pom.getSauceDemoInventoryPage().getCartIcon().click()

@when('user clicks on checkout')
def step_when_user_clicks_on_checkout(context):
    pom.getSauceDemoCartPage().getCheckOut().click()

@when('user enters first name {first_name}')
def step_when_user_enters_first_name(context, first_name):
    pom.getSauceDemoInformationPage().getFirstname().send_keys(first_name)

@when('user enters last name {last_name}')
def step_when_user_enters_last_name(context, last_name):
    pom.getSauceDemoInformationPage().getLastName().send_keys(last_name)

@when('user enters zip code {zip_code}')
def step_when_user_enters_zip_code(context, zip_code):
    pom.getSauceDemoInformationPage().getZipCode().send_keys(zip_code)

@when('user clicks Continue button')
def step_when_user_clicks_continue_button(context):
    pom.getSauceDemoInformationPage().getContinueButton().click()

@then('I verify in Checkout overview page if the total amount for the added item is ${total_amount}')
def step_then_i_verify_total_amount_in_checkout_overview(context, total_amount):
    expected_total_amount = f"Total: ${total_amount}"
    actual_total_amount = pom.getSauceDemoCheckOutOverviewPage().getTotalAmount().text
    assert actual_total_amount == expected_total_amount

@when('user clicks Finish button')
def step_when_user_clicks_finish_button(context):
    pom.getSauceDemoCheckOutOverviewPage().getFinish().click()

@then('Thank You header is shown in Checkout Complete page')
def step_then_thank_you_header_is_shown_in_checkout_complete_page(context):
    thank_you_header = pom.getSauceDemoCheckOutCompletePage().getThankYouHeader()
    assert thank_you_header.is_displayed()
