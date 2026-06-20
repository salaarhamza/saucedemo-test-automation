from utils.test_data import BASE_URL, VALID_USER, PASSWORD

def test_valid_login(page):
    page.goto(BASE_URL)
    
    page.fill("#user-name", VALID_USER)
    page.fill("#password", PASSWORD)
    page.click("#login-button")

    assert page.url == "https://www.saucedemo.com/inventory.html"
    assert page.locator(".inventory_list").is_visible()
