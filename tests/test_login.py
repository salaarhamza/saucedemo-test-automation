from pages.login_page import LoginPage
from utils.test_data import BASE_URL, VALID_USER, PASSWORD

def test_valid_login(page):
    login_page = LoginPage(page)
    
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USER, PASSWORD)


    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert login_page.is_inventory_page_loaded()
