from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]/p[1]')
    SUCCESS_MSG_WITH_PRODUCT_NAME = (By.XPATH, '//div[@id="messages"]/div[1]')
    SUCCESS_MSG_WITH_PRODUCT_PRICE = (By.XPATH, '//div[@id="messages"]/div[3]')
