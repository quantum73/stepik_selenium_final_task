from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        password_1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1_FIELD)
        password_2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2_FIELD)
        email_field.send_keys(email)
        password_1_field.send_keys(password)
        password_2_field.send_keys(password)
        self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.url.endswith(LoginPageLocators.LOGIN_URL.get_attribute("action")), "Incorrect login URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Register form is not presented"
