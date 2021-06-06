# 4.2.7
# https://stepik.org/lesson/238819/step/7?unit=211271

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    MESSAGE_ADDING_SUCCESS = (By.CSS_SELECTOR, "#messages strong")
    
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong") 
    
