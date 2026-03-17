"""Inventory management."""

class Inventory:

    def __init__(self):
        self.stock = {}

    def set_stock(self, item_id, amount):

        # Set or update stock level
        self.stock[item_id] = amount

    def get_stock(self, item_id):

        # Return stock amount, 0 if no items
        return self.stock.get(item_id, 0)

    def lower_stock(self, item_id, quantity):

        # Prevent negative stock
        if self.get_stock(item_id) < quantity:
            raise Exception("Not enough stock")

        # Decrease stock  after order confirmation
        self.stock[item_id] -= quantity

    def display_stock(self):

        # Display  current inventory
        print("---Current Stock---")

        for item_id, quantity in self.stock.items():
            print(f"{item_id}: {quantity}")
