"""
Exercise 10: Nested Data with Filtering & Aggregation

products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 30},
            {"name": "Smartphone", "price": 800, "stock": 0},
            {"name": "Headphones", "price": 150, "stock": 15},
        ],
    },
    {
        "category": "Books",
        "items": [
            {"name": "Python Programming", "price": 45, "stock": 12},
            {"name": "AI for Beginners", "price": 60, "stock": 7},
        ],
    },
    {
        "category": "Clothing",
        "items": [
            {"name": "T-Shirt", "price": 20, "stock": 50},
            {"name": "Jeans", "price": 40, "stock": 5},
            {"name": "Jacket", "price": 120, "stock": 0},
        ],
    },
]


Task 1:
Print all items that are currently in stock (stock > 0), with their category and price.

Output format:
Electronics - Laptop ($1200)
Electronics - Headphones ($150)
...


Task 2:
Create a dictionary category_totals showing the total stock per category (sum of stock of all items in that category).

Example output:
{'Electronics': 45, 'Books': 19, 'Clothing': 55}


Task 3:
Identify and print the most expensive item in the entire dataset, along with its category.

Output format:
Most expensive item: Laptop ($1200) in Electronics


Bonus Task:
Create a flat list of all out-of-stock items, with their names only, sorted alphabetically.

Output example:
['Jacket', 'Smartphone']
"""

products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 30},
            {"name": "Smartphone", "price": 800, "stock": 0},
            {"name": "Headphones", "price": 150, "stock": 15},
        ],
    },
    {
        "category": "Books",
        "items": [
            {"name": "Python Programming", "price": 45, "stock": 12},
            {"name": "AI for Beginners", "price": 60, "stock": 7},
        ],
    },
    {
        "category": "Clothing",
        "items": [
            {"name": "T-Shirt", "price": 20, "stock": 50},
            {"name": "Jeans", "price": 40, "stock": 5},
            {"name": "Jacket", "price": 120, "stock": 0},
        ],
    },
]


# Task 1:
for product in products:
    category = product["category"]

    for item in product["items"]:
        name = item["name"]
        price = item["price"]
        stock = item["stock"]

        if stock > 0:
            print(f"{category} - {name} (${price})")


# Task 2:
category_totals = {}

for product in products:
    category = product["category"]
    stock = 0

    for item in product["items"]:
        stock += item["stock"]

    category_totals[category] = stock


# Task 3:
category = ""
name = ""
price = 0

for product in products:
    for item in product["items"]:
        if price < item["price"]:
            category = product["category"]
            name = item["name"]
            price = item["price"]

print(f"Most expensive item: {name} (${price}) in {category}")


# Bonus task:
out_of_stock = []

for product in products:
    for item in product["items"]:
        if item["stock"] == 0:
            out_of_stock.append(item["name"])

print(sorted(out_of_stock))
