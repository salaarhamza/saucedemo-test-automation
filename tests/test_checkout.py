from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.test_data import (
    BASE_URL,
    VALID_USERS,
    PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    MISSING_FIRST_NAME_ERROR,
    MISSING_LAST_NAME_ERROR,
    MISSING_POSTAL_CODE_ERROR,
    ORDER_COMPLETE_MESSAGE,
)


def login_and_add_product_to_cart(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()


def test_successful_checkout(page):
    login_and_add_product_to_cart(page)

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.complete_order(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    assert checkout_page.is_checkout_complete()
    assert checkout_page.get_complete_message() == ORDER_COMPLETE_MESSAGE


def test_checkout_without_first_name_shows_error(page):
    login_and_add_product_to_cart(page)

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_information("", LAST_NAME, POSTAL_CODE)
    checkout_page.continue_checkout()

    assert checkout_page.get_error_message() == MISSING_FIRST_NAME_ERROR


def test_checkout_without_last_name_shows_error(page):
    login_and_add_product_to_cart(page)

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_information(FIRST_NAME, "", POSTAL_CODE)
    checkout_page.continue_checkout()

    assert checkout_page.get_error_message() == MISSING_LAST_NAME_ERROR


def test_checkout_without_postal_code_shows_error(page):
    login_and_add_product_to_cart(page)

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_information(FIRST_NAME, LAST_NAME, "")
    checkout_page.continue_checkout()

    assert checkout_page.get_error_message() == MISSING_POSTAL_CODE_ERROR