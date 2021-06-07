from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time
import pytest

# 4.3.3
# https://stepik.org/lesson/201964/step/3?discussion=1095640&next=&reply=3886667&thread=solutions&unit=176022

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    #"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

##links = [
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
##    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
##]



@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


@pytest.mark.parametrize("product", links)
def test_should_be_message_product_is_added_to_basket(browser, product):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_product_name_in_message()


@pytest.mark.parametrize("product", links)
def test_should_be_message_with_basket_price(browser, product):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_total_price_in_message()


# 4.3.6
@pytest.mark.parametrize("product", links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product):
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_not_present_success_message()


@pytest.mark.parametrize("product", links)
def test_guest_cant_see_success_message(browser, product):
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.is_not_present_success_message()


@pytest.mark.parametrize("product", links)
def test_message_disappeared_after_adding_product_to_basket(browser, product):
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_disappeared_success_message()

















    
    

