"""Command-line interface for orders."""

from order import Order
from pricing import TipStrategy
from menu import Combo

class CLI:
    def __init__(self, menu, inventory):

        # Menu and inventory references
        self.menu = menu
        self.inventory = inventory
        self.order = None

    def create_order(self):

        # Start a new order
        self.order = Order()
        print("Order created")

    def add_items(self, item_id, quantity):

        # Get item from the menu
        item = self.menu[item_id]

        # Add it to the order
        self.order.add_item(item, quantity)

    def confirm_order(self):

        # Verify stock availability
        for i in self.order.get_items():

            if self.inventory.get_stock(i.item.item_id) <  i.quantity:
                raise Exception("Out of stock")

        # Deduct from stock
        for i in self.order.get_items():
            self.inventory.lower_stock(i.item.item_id, i.quantity)

        # Change the order state
        self.order.change_status("confirmed")

    def receipt(self, tax, tip_percent):

        subtotal = self.order.subtotal()
        discount = self.order.discount_total()

        # Calculate tax
        tax_amount = tax.calculate_tax(self.order.get_items())

        # Calculate tip
        tip = TipStrategy(tip_percent).calculate_tip(subtotal - discount + tax_amount)

        total = subtotal - discount + tax_amount + tip

        print("\n--- Receipt ---")
        print("\n Items Ordered:")

        for order_item in self.order.get_items():
            item = order_item.item
            quantity = order_item.quantity

            # handle a combos price
            if isinstance(item, Combo):
                price = item.get_price()

            else:
                price = item.price

            item_total = price * quantity
            print(f"{item.name} x{quantity} - ${item_total:.2f}")

        print("\n----------")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Tax: ${tax_amount:.2f}")
        print(f"Tip: ${tip:.2f}")
        print(f"Total: ${total:.2f}")
