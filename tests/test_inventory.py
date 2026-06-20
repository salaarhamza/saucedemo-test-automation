from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD


def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)


def test_inventory_page_loads_after_login(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    assert inventory_page.is_loaded()


def test_inventory_contains_six_products(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    assert inventory_page.get_product_count() == 6


def test_all_products_have_names(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    product_names = inventory_page.get_product_names()

    assert len(product_names) == 6
    assert all(name.strip() for name in product_names)


def test_all_products_have_prices(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    product_prices = inventory_page.get_product_prices()

    assert len(product_prices) == 6
    assert all(price > 0 for price in product_prices)


def test_sort_products_by_name_a_to_z(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.sort_by_name_a_to_z()
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)


def test_sort_products_by_price_low_to_high(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.sort_by_price_low_to_high()
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices)