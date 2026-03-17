"""Sample execution."""

from menu import FoodItem, DrinkItem, Combo
from inventory import Inventory
from pricing import TaxStrategy, PercentageDiscount, FixedAmountDiscount
from cli import CLI

# Create the menu items
burger = FoodItem(1, 'Burger', 6)
fries = FoodItem(2, 'Fries', 3)
coca_cola = DrinkItem(3, 'Coke', 2)

# Create a combo item
combo_meal = Combo(4, 'Burger Combo Meal', [burger, fries, coca_cola], 0.1)

# Build menu dictionary
menu = {
    1: burger,
    2: fries,
    3: coca_cola,
    4: combo_meal
}

# Initialize inventory
inventory = Inventory()
inventory.set_stock(1, 100)
inventory.set_stock(2, 50)
inventory.set_stock(3, 30)
inventory.set_stock(4, 10)

# Create CLI interface
cli = CLI(menu, inventory)
cli.create_order()

# Add items to order
cli.add_items(1, 2)
cli.add_items(2, 3)
cli.add_items(3, 4)
cli.add_items(4, 1)

# apply discounts
cli.order.apply_discount(PercentageDiscount(0.10))
cli.order.apply_discount(FixedAmountDiscount(2))

# confirm order
cli.confirm_order()

# status progression over time
cli.order.change_status('preparing')
cli.order.change_status('ready')
cli.order.change_status('served')
cli.order.change_status('paid')

# Define tax rates
tax = TaxStrategy(0.07, 0.10)

# Print the receipt
cli.receipt(tax, 0.15)
