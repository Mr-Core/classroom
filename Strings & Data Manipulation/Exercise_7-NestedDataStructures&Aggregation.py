"""
Exercise 3: Nested Data Structures & Aggregation

Scenario: Orders & Inventory

You're working with an order tracking system for an online shop. Each order includes a list of items purchased by a user, along with quantity.
Your Data:

orders = [
    {"user": "Alice", "items": [{"product": "Book", "quantity": 2}, {"product": "Pen", "quantity": 5}]},
    {"user": "Bob", "items": [{"product": "Book", "quantity": 1}]},
    {"user": "Charlie", "items": [{"product": "Pen", "quantity": 2}, {"product": "Notebook", "quantity": 3}]},
    {"user": "Daisy", "items": [{"product": "Book", "quantity": 1}, {"product": "Pen", "quantity": 2}]},
]


Task 1:
Create a dictionary product_totals that shows the total quantity sold for each product.

Example output:
{
    "Book": 4,
    "Pen": 9,
    "Notebook": 3
}


Task 2:
Create a dictionary user_totals that shows the total number of items purchased per user.

Example output:
{
    "Alice": 7,
    "Bob": 1,
    "Charlie": 5,
    "Daisy": 3
}


Task 3:
Print a list of users who bought more than 5 items in total.


Bonus Task:
Print a sorted list of products by most sold quantity, descending.

Each line should look like:
Book: 4 units
"""

orders = [
    {
        "user": "Alice",
        "items": [
            {"product": "Book", "quantity": 2},
            {"product": "Pen", "quantity": 5},
        ],
    },
    {"user": "Bob", "items": [{"product": "Book", "quantity": 1}]},
    {
        "user": "Charlie",
        "items": [
            {"product": "Pen", "quantity": 2},
            {"product": "Notebook", "quantity": 3},
        ],
    },
    {
        "user": "Daisy",
        "items": [
            {"product": "Book", "quantity": 1},
            {"product": "Pen", "quantity": 2},
        ],
    },
]


# Task 1:
product_totals = {}

for order in orders:
    for item in order["items"]:
        product = item["product"]
        quantity = item["quantity"]

        if product not in product_totals:
            product_totals[product] = 0

        product_totals[product] += quantity

for key, value in product_totals.items():
    print(f"{key}: {value}")


# Task 2:
user_totals = {}

for order in orders:
    user = order["user"]
    no_orders = 0

    for item in order["items"]:
        no_orders += item["quantity"]

    user_totals[user] = no_orders

for key, value in user_totals.items():
    print(f"{key}: {value}")


# Task 3:
for user, total_items in user_totals.items():
    if total_items >= 5:
        print(f"{user}: {total_items}")


# Bonus task:
# sorted_product_totals = dict(
#     sorted(product_totals.items(), key=lambda item: item[1], reverse=True)
# )
#
# for key, value in sorted_product_totals.items():
#     print(f"{key}: {value} units")

sorted_products = sorted(product_totals.items(), key=lambda item: item[1], reverse=True)

for product, qty in sorted_products:
    print(f"{product}: {qty} units")
