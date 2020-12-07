from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "In basket one or more products"

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTINUE_SHOPPING_LINK), "Basket is not empty"
