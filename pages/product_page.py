# https://stepik.org/lesson/201964/step/2?next=&unit=176022

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        basket_button.click()
        self.solve_quiz_and_get_code()
        

    def check_product_name_in_message(self):        
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDING_SUCCESS), \
               "No message of adding to basket on page"

        message_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDING_SUCCESS).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert product_name == message_basket, "Wrong product name in message"


    def check_total_price_in_message(self):        
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), \
               "No  message of total price on page"

        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        total_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert total_price == message_price, "Wrong total price in message"


    def is_not_present_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDING_SUCCESS), \
               "Success message is present on product page, but should not be"


    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDING_SUCCESS), \
               "Success message did not disappeared on product page"
        




        
        
        
