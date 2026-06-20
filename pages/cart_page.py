class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_item = ".cart_item"
        self.cart_item_name = ".inventory_item_name"
        self.cart_item_price = ".inventory_item_price"
        self.remove_backpack_button = "[data-test='remove-sauce-labs-backpack']"

    def get_cart_item_count(self):
        return self.page.locator(self.cart_item).count()

    def get_cart_item_name(self):
        return self.page.locator(self.cart_item_name).inner_text()

    def get_cart_item_price(self):
        return self.page.locator(self.cart_item_price).inner_text()

    def remove_backpack_from_cart(self):
        self.page.click(self.remove_backpack_button)

    def is_cart_empty(self):
        return self.page.locator(self.cart_item).count() == 0