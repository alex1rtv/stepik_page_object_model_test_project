# https://stepik.org/lesson/199980/step/6?unit=174035
# 4.1.6

##def test_guest_can_go_to_login_page(browser):
##    link = "http://selenium1py.pythonanywhere.com/"
##    browser.get(link)
##    login_link = browser.find_element_by_css_selector("#login_link")
##    login_link.click()

## -----------------------------------------------

# 4.1.7
# https://stepik.org/lesson/199980/step/7?unit=174035

##link = "http://selenium1py.pythonanywhere.com/"
##
##def go_to_login_page(browser):
##    login_link = browser.find_element_by_css_selector("#login_link")
##    login_link.click()
##
##def test_guest_can_go_to_login_page(browser): 
##   browser.get(link) 
##   go_to_login_page(browser)
   

# 4.2.4

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

























