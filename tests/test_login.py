import pytest

from pages.login_page import LoginPage
from utils.test_data import (
    BASE_URL,
    VALID_USERS,
    PASSWORD,
    LOCKED_USER,
    INVALID_USER,
    INVALID_PASSWORD,
    INVALID_LOGIN_ERROR,
    LOCKED_OUT_ERROR
)

@pytest.mark.parametrize("username", VALID_USERS)
def test_valid_login(page, username):
    login_page = LoginPage(page)
    
    login_page.navigate(BASE_URL)
    login_page.login(username, PASSWORD)
    assert login_page.is_inventory_page_loaded()
    assert "inventory.html" in page.url

def test_invalid_login_error_message(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(INVALID_USER, INVALID_PASSWORD)

    assert login_page.is_error_message_visible()
    assert INVALID_LOGIN_ERROR == login_page.get_error_message()

def test_locked_out_user_shows_error_message(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(LOCKED_USER, PASSWORD)
    assert login_page.is_error_message_visible()
    assert login_page.get_error_message() == LOCKED_OUT_ERROR
