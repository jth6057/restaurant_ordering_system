# Restaurant Ordering System Report
## Project Overview: 

This project is a restaurant ordering system built using object-oriented programming as its base and includes encapsulation, inheritance, polymorphism, and composition. The system allows for creating menu items, managing orders, applying pricing rules, tracking inventory, and printing receipts. The goal is to include these features in a usable realistic system that is similar to real code in a real inventory management system. To run the program all you need to do is execute main.py which runs a sample scenario that demonstrates all requirements. 

 

## Project structure: 

menu.py - contains menu item classes including MenuItem, FoodItem, DrinkItem, and Combo. 

inventory.py - inventory management classes and functions, manages item stock and prevents ordering out of stock items. 

pricing.py - contains all the logic for pricing including tax calculation, tip calculations, and discount strategies.  

order.py - contains OrderItem and Order classes which manage items in an order and enforces the status of the order. 

cli.py - system interface providing command line style methods for creating order adding items, confirming orders, and printing receipts. 

main.py - sample execution scenario that creates menu items, builds an order, applies discounts, and prints a receipt. 

The project is separated into modules to improve organization and maintainability. Each file has a specific responsibility, which makes the system easier to extend. 

 

## Class Summary:  

MenuItem – base class for generic menu items. 

FoodItem – subclass of menu item representing food items. 

DrinkItem – subclass of MenuItem representing drink items. 

Combo – a menu item composed of multiple items with a percentage discount 	applied. 

Inventory – tracks stock quantities for each menu item. 

OrderItem – represents an item and quantity within an order 

Order – manages order items, applied discounts, and the order status. 

TaxStrategy – calculates tax for food and drink categories 

TipStrategy – calculates the tip based on a percentage of the order total.  

Discount – base class for discount strategies. 

PercentageDiscount – applies a percentage discount to the order total. 

FixedAmountDiscount – subtracts a fixed dollar amount from the order total.



## Class Diagram

MenuItem:
|-- FoodItem
|-- DrinkItem
|__ Combo

Discount:
|-- PercentageDiscount
|__ FixedAmountDiscount

Order:
|__ OrderItem

Order uses:
- TaxStrategy
- TipStrategy
- Discount

Inventory: Manages MenuItem stock

This design separates responsibilities across classes to improve maintainability and flexibility. Inheritance is used for items and discounts, while composition is used for orders and combos.



## Object Oriented Design: 

Encapsulation – Encapsulation is used by keeping internal data private, such as _items and _discounts in the Order class and only being able to modify them through methods like add_item() and apply_discount(). 

Inheritance – Inheritance is used to create specialized classes that inherit attributes and behavior from a base class. FoodItem, DrinkItem, and Combo inherit from MenuItem while PercentageDiscount and FixedAmountDiscount inherit from Discount 

Polymorphism – Polymorphism is shown through overriding methods. The apply() method behaves differently depending on the discount type, and OrderItem.total() works for regular and combo items. 

Composition – Composition is used when classes contain other objects. The Order class contains OrderItem objects, and the Combo class contains multiple MenuItem objects. 

 

## Pricing Formula: 

- Subtotal = sum(item price x quantity) 

- Discounts are applied sequentially in the order they are added and applied before tax 

- Tax is calculated separately for food and drink categories 

- Tip is calculated using – Tip = (subtotal – discounts + tax) x tip rate 

- Total = subtotal – discounts + tax + tip 

 

## Test Plan and Results: 

### Menu and inventory:  

- Items are created correctly 

- Inventory stock is stored and updated properly 

- Prevents ordering when stock is insufficient 

### Order System: 

- Items are added and removed correctly

- Order items are stored and retrieved correctly 

- Subtotal calculation is accurate 

### Discounts: 

- Percentage discounts apply correctly 

- Fixed discounts apply correctly 

- Multiple discounts apply in sequence 

### Tax and Tip: 

- Food and drink are taxed at different rates 

- Combo items correctly split tax by item type 

- Tip is calculated based on final amount 

### Order Status: 

- Valid state transitions work correctly 

- Invalid transitions raise an exception 

 

## Discussion of Results: 

All test cases produced the expected outcomes. Inventory correctly prevented orders when stock was insufficient. Order totals matched manual calculations, confirming the accuracy of subtotal, discount, tax, and tip logic. State transitions behaved as expected, with invalid transitions raising errors. Overall, the system produced consistent and correct results across the tested scenarios. 

 

## Sample Scenario Description: 

The system creates the three items Burger, Fries, Coke and one combo meal with a 10% discount. Stock is assigned to each item. An order is created, and multiple items including the combo are added. A percentage discount and a fixed discount are applied. The order progresses through all statuses from created to paid, and a receipt is generated. 

 

## Discussion of Execution Results: 

The receipt shows correct calculations for subtotal, discounts, tax, tip, and final total. The discount values match the expected percentage and fixed reductions. Tax is applied correctly based on item categories, and the tip is calculated using the final amount. Inventory is reduced after confirming the order, confirming correct system behavior. 

 

## CLI Transcript: 

--- Receipt --- 
 
Items Ordered: 
Burger x2 - $12.00 
Fries x3 - $9.00 
Coke x4 - $8.00 
Burger Combo Meal x1 - $9.90 
 
---------- 
Subtotal: $38.90 
Discount: $5.89 
Tax: $3.02 
Tip: $5.40 
Total: $41.43 

 

## Limitations: 

- The system is not interactive and relies on a predefined scenario 

- Limited error handling for invalid inputs 

- The CLI interface is basic 

- The program doesn't store any data persistently.  

 

## Possible Improvements: 

- Add interactive user input for ordering 

- Improve error handling and validation 

- Create a graphical user interface 

- Expand menu and inventory features 

- Add a persistent data storage feature 

 

## Challenges Faced: 

The biggest challenge I faced was getting all the pricing features to work correctly and produce correct totals. This is because of how the combo meals had to be broken down and the tax calculated for each individual item.  I also struggled with getting the order status feature to work as intended and correctly update. 

## Conclusion: 

This project demonstrates how object-oriented programming can be used to build a structured, flexible, and maintainable system similar to real-world applications. By dividing responsibilities across multiple classes and modules, the system is easier to understand, extend, and reuse. The implementation successfully handles menu management, ordering, pricing, and inventory tracking. 