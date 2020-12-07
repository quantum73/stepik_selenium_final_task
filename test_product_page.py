from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)  # получаем PageObject корзины
    basket_page.should_not_products_in_basket()  # проверяем что в корзине нет ни одной позиции с товаром
    basket_page.should_be_basket_is_empty()  # проверяем что корзина пуста и имеет ссылку "Продолжить покупки"

# @pytest.mark.parametrize(
#     'link',
#     ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#      pytest.param(
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#          marks=pytest.mark.xfail),
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"],
# )
# def test_guest_can_add_product_to_basket(browser, link):
#     product_page = ProductPage(browser, link)
#     # открываем страницу
#     product_page.open()
#     # проверяем, есть ли на странице кнопка добавления в корзину
#     product_page.should_be_add_to_basket_button()
#     # кликаем на кнопку добавления в корзину
#     product_page.add_product_to_basket()
#     # обрабатываем alert и вычисляем результат
#     product_page.solve_quiz_and_get_code()
#     # проверяем появились ли сообщения о добавлении товара к корзину
#     product_page.should_be_success_messages()
#     # проверяем что название товара в сообщении совпадает с названием товара, который действительно был добавлен
#     product_page.should_be_product_name_matches_product_name_in_basket()
#     # проверяем что стоимость корзины совпадает с ценой товара
#     product_page.should_be_product_price_equals_value_of_basket()
