"""Pricing: tax, tips, and discounts."""

class TaxStrategy:
    """Calculates tax based on item category."""

    def __init__(self, food_tax_rate, drink_tax_rate):

        # Store tax rates by category
        self.food_tax_rate = food_tax_rate
        self.drink_tax_rate = drink_tax_rate

    def calculate_tax(self, ordered_items):

        total = 0

        # Loop through ordered items
        for ordered_item in ordered_items:

            item = ordered_item.item
            quantity = ordered_item.quantity

            # Calculate tax for combo items
            if hasattr(item, "items"):

                combo_price = item.get_price()
                # Split into each item in a combo then apply the tax rates to each item based on that

                for sub_item in item.items:

                    portion = sub_item.price / sum(sub_item.price for sub_item in item.items)
                    portion_price = combo_price * portion * quantity

                    if sub_item.category == "food":
                        total += self.food_tax_rate * portion_price

                    elif sub_item.category == "drink":
                        total += self.drink_tax_rate * portion_price
            else:
                # Regular food and drink tax
                if item.category == "food":
                    total += item.price * quantity * self.food_tax_rate

                elif item.category == "drink":
                    total += item.price * quantity * self.drink_tax_rate

        return total

class TipStrategy:
    """Calculates tips based on a percentage."""

    def __init__(self, percent):

        # Tip percent
        self.percent = percent

    def calculate_tip(self, amount):

        # Tip based on final amount
        return amount * self.percent

class Discount:
    """Base class for discount strategies."""

    # Base discount
    def apply(self, amount):
        return amount

class PercentageDiscount(Discount):
    """Discount is applied based on a percentage from a total."""

    def __init__(self, percent):

        # Percentage discount
        self.percent = percent

    def apply(self, amount):
        return amount * (1 - self.percent)

class FixedAmountDiscount(Discount):
    """Discount is applied on a fixed amount from a total."""

    def __init__(self, amount):

        # Fixed dollar discount
        self.amount = amount

    def apply(self, amount):

        # Stop negative totals
        return max(0, amount - self.amount)
