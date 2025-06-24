"""
Exercise 9: Nested Data Extraction & Summary

You're given a complex data structure representing users and their purchase histories.
Your task is to extract meaningful insights by processing this data.

users = [
    {
        "name": "Alice",
        "purchases": [
            {"item": "Book", "price": 12.99},
            {"item": "Pen", "price": 1.50},
        ],
    },
    {
        "name": "Bob",
        "purchases": [
            {"item": "Notebook", "price": 5.99},
            {"item": "Backpack", "price": 29.99},
            {"item": "Pen", "price": 1.50},
        ],
    },
    {
        "name": "Charlie",
        "purchases": [],
    },
]


Task 1:
Create a dictionary that shows the total amount spent by each user.

Output format:
{
    "Alice": 14.49,
    "Bob": 37.48,
    "Charlie": 0
}


Task 2:
Create a dictionary that shows the total number of times each item was purchased across all users.

Output format:
{
    "Book": 1,
    "Pen": 2,
    "Notebook": 1,
    "Backpack": 1
}


Bonus Task:
Print out each user and list the items they purchased (no prices), comma-separated.
If they didn't purchase anything, say "No purchases".

Example output:
  Alice: Book, Pen
  Bob: Notebook, Backpack, Pen
  Charlie: No purchases
"""

users = [
    {
        "name": "Alice",
        "purchases": [
            {"item": "Book", "price": 12.99},
            {"item": "Pen", "price": 1.50},
        ],
    },
    {
        "name": "Bob",
        "purchases": [
            {"item": "Notebook", "price": 5.99},
            {"item": "Backpack", "price": 29.99},
            {"item": "Pen", "price": 1.50},
        ],
    },
    {
        "name": "Charlie",
        "purchases": [],
    },
]


# Task 1:
spending = {}

for user in users:
    name = user["name"]

    spending[name] = 0

    for purchase in user["purchases"]:
        amount = purchase["price"]

        spending[name] += amount

for user, amount in spending.items():
    print(user, amount)


# Task 2:
sold_items = {}

for user in users:
    for purchase in user["purchases"]:
        item = purchase["item"]

        if item not in sold_items:
            sold_items[item] = 1
        else:
            sold_items[item] += 1

for item, quantity in sold_items.items():
    print(item, quantity)


# Bonus task:
user_purchases = {}

for user in users:
    name = user["name"]

    if name not in user_purchases:
        user_purchases[name] = []

    for purchase in user["purchases"]:
        user_purchases[name].append(purchase["item"])

for user, items in user_purchases.items():
    if not items:
        print(f"{user}: No purchases")
    else:
        print(f"{user}: {", ".join(items)}")
