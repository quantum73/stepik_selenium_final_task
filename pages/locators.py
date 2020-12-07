from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket')]/span/a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "basket_summary")
    BASKET_CONTINUE_SHOPPING_LINK = (By.XPATH, '//div[@id="content_inner"]/p/a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_URL = LOGIN_FORM
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_PASSWORD_1_FIELD = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_PASSWORD_2_FIELD = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]/p[1]')
    SUCCESS_MSG_WITH_PRODUCT_NAME = (By.XPATH, '//div[@id="messages"]/div[1]//strong')
    SUCCESS_MSG_WITH_PRODUCT_PRICE = (By.XPATH, '//div[@id="messages"]/div[3]//strong')
