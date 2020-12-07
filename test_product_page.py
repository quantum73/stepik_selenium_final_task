import time
from uuid import uuid4

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.test_for_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        email = str(time.time()) + "@fakemail.org"
        password = str(uuid4())

        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.should_be_login_link()
        product_page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_register_form()
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.can_add_product_to_basket()


@pytest.mark.test_for_guest
class TestGuestAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.can_add_product_to_basket()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_products_in_basket()  # проверяем что в корзине нет ни одной позиции с товаром
        basket_page.should_be_basket_is_empty()  # проверяем что корзина пуста и имеет ссылку "Продолжить покупки"

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
