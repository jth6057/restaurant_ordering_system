"""Order and order items."""

class OrderItem:
    """Represents a single menu item in an order and its quantity."""

    def __init__(self, item, quantity):

        # Store the item and its quantity
        self.item = item
        self.quantity = quantity

    def total(self):

        # Default item price
        price = self.item.price

        # Use combo pricing if available
        if hasattr(self.item, "get_price"):
            price = self.item.get_price()

        return price * self.quantity

class Order:
    """Represents an order containing items, discounts, and status cycle."""

    # Valid order states and transitions
    transitions = {"created": "confirmed",
                   "confirmed": "preparing",
                   "preparing": "ready",
                   "ready": "served",
                   "served": "paid"}

    def __init__(self):

        # List of OrderItem objects
        self._items = []
        self.status = "created"
        self._discounts = []

    def add_item(self, item, quantity):

        # Add item to an order
        self._items.append(OrderItem(item, quantity))

    def remove_item(self, item_id):

        # Remove items by its id
        self._items = [i for i in self._items if i.item.item_id != item_id]

    def subtotal(self):

        # Sum item totals
        return sum([i.total() for i in self._items])

    def apply_discount(self, discount):

        # Apply the discount strategy
        self._discounts.append(discount)

    def discount_total(self):
        total = self.subtotal()

        # Apply the discounts in order
        for discount in self._discounts:
            total = discount.apply(total)

        return self.subtotal() - total

    def change_status(self, new_status):

        # Enforce the valid order states and transitions
        if Order.transitions.get(self.status) != new_status:
            raise Exception(f"Invalid status change: {self.status}")

        self.status = new_status

    def view_items(self):

        # Print items in order
        for i in self._items:
            print(i.item.name, ":", i.quantity)

    def get_items(self):
        return self._items

    def get_discounts(self):
        return self._discounts
