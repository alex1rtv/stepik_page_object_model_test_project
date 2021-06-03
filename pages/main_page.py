# https://stepik.org/lesson/238819/step/3?unit=211271

from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
