"""Menu item classes."""

class MenuItem:
    """Base menu item"""

    def __init__(self, item_id, name, price, category):

        # Basic item information
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def set_availability(self):

        # Toggle availability
        self.available = not self.available

class FoodItem(MenuItem):
    """Food menu item."""

    def __init__(self, item_id, name, price):

        # Food category auto assigned
        super().__init__(item_id, name, price, "food")


class DrinkItem(MenuItem):
    """Drink menu item."""

    def __init__(self, item_id, name, price):

        # Drink category auto assigned
        super().__init__(item_id, name, price, "drink")


class Combo(MenuItem):
    """Combo  composed of multiple items with discounts."""

    def __init__(self, item_id, name, items, discount = 0.1):

        # Combo  price calculated dynamically
        super().__init__(item_id, name, 0, "combo")
        self.items = items
        self.discount = discount

    def get_price(self):

        # Sum component prices and apply combo discount
        total = sum(item.price for item in self.items)
        return total * (1 - self.discount)
