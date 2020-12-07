import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def can_add_product_to_basket(self):
        # проверяем, есть ли на странице кнопка добавления в корзину
        self.should_be_add_to_basket_button()
        # кликаем на кнопку добавления в корзину
        self.add_product_to_basket()
        # проверяем появились ли сообщения о добавлении товара к корзину
        self.should_be_success_messages()
        # проверяем что название товара в сообщении совпадает с названием товара, который действительно был добавлен
        self.should_be_product_name_matches_product_name_in_basket()
        # проверяем что стоимость корзины совпадает с ценой товара
        self.should_be_product_price_equals_value_of_basket()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_success_messages(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MSG_WITH_PRODUCT_NAME), "No success messages with product name"
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MSG_WITH_PRODUCT_PRICE), "No success messages with product price"

    def should_be_product_price_equals_value_of_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
        price_in_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_WITH_PRODUCT_PRICE).text.strip()
        assert product_price == price_in_message, "Product price corresponds to the value of the basket"

    def should_be_product_name_matches_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        message_with_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_WITH_PRODUCT_NAME).text.strip()
        assert product_name == message_with_price, "Product name matches the product name that was added to the basket"
        print("--- Product add to basket! ---")

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
