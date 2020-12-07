from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()  # открываем страницу
    product_page.should_be_add_to_basket_button()  # проверяем, есть ли на странице кнопка добавления в корзину
    product_page.add_product_to_basket()  # кликаем на кнопку добавления в корзину
    product_page.solve_quiz_and_get_code()  # обрабатываем alert и вычисляем результат
