import pytest

from .pages.product_page import ProductPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    # проверяем, есть ли на странице кнопка добавления в корзину
    product_page.should_be_add_to_basket_button()
    # кликаем на кнопку добавления в корзину
    product_page.add_product_to_basket()
    # обрабатываем alert и вычисляем результат
    product_page.solve_quiz_and_get_code()
    # проверяем появились ли сообщения о добавлении товара к корзину
    product_page.should_be_success_messages()
    # проверяем что название товара в сообщении совпадает с названием товара, который действительно был добавлен
    product_page.should_be_product_name_matches_product_name_in_basket()
    # проверяем что стоимость корзины совпадает с ценой товара
    product_page.should_be_product_price_equals_value_of_basket()
