from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD


def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)


def test_add_product_to_cart_updates_badge(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_badge_count() == "1"


def test_added_product_is_visible_in_cart(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(page)

    assert cart_page.get_cart_item_count() == 1
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"
    assert cart_page.get_cart_item_price() == "$29.99"


def test_remove_product_from_cart(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.remove_backpack_from_cart()

    assert cart_page.is_cart_empty()