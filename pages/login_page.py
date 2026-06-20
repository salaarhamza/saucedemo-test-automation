class LoginPage:
    def __init__(self, page):
        self.page = page
    
    def navigate(self, url):
        self.page.goto(url)
    
    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def is_inventory_page_loaded(self):
        return self.page.locator(".inventory_list").is_visible()

