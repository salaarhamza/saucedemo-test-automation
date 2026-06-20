class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.inventory_container = ".inventory_list"
        self.inventory_items = ".inventory_item"
        self.product_names = ".inventory_item_name"
        self.product_prices = ".inventory_item_price"
        self.sort_dropdown = "[data-test='product-sort-container']"

    def is_inventory_page_loaded(self):
        return self.page.is_visible(self.inventory_container)

    def get_product_names(self):
        return self.page.locator(self.product_names).all_text_contents()
        
    def is_loaded(self):
        return self.page.locator(self.inventory_container).is_visible()

    def get_product_count(self):
        return self.page.locator(self.inventory_items).count()

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def get_product_prices(self):
        price_texts = self.page.locator(self.product_prices).all_inner_texts()
        return [float(price.replace("$", "")) for price in price_texts]

    def sort_by_name_a_to_z(self):
        self.page.select_option(self.sort_dropdown, "az")

    def sort_by_name_z_to_a(self):
        self.page.select_option(self.sort_dropdown, "za")

    def sort_by_price_low_to_high(self):
        self.page.select_option(self.sort_dropdown, "lohi")

    def sort_by_price_high_to_low(self):
        self.page.select_option(self.sort_dropdown, "hilo")
        
    
    #### Cart interactions ####
    def add_backpack_to_cart(self):
        self.page.click("[data-test='add-to-cart-sauce-labs-backpack']")

    def remove_backpack_from_cart(self):
        self.page.click("[data-test='remove-sauce-labs-backpack']")

    def open_cart(self):
        self.page.click(".shopping_cart_link")

    def get_cart_badge_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()
