"""
users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 19, "active": False},
    {"name": "Charlie", "age": 25, "active": True},
    {"name": "Daisy", "age": 17, "active": False},
    {"name": "Eve", "age": 35, "active": True},
]


Task 1 — Filter Active Users (List of Names)
Create a list of names for users who are marked as "active": True.

Example output:
['Alice', 'Charlie', 'Eve']

Do this first with a for loop, then with a list comprehension.


Task 2 — Create Dictionary of Adult Users (age >= 21)
Create a dictionary where the keys are user names, and the values are their ages, but only include users who are 21 or older.

Example output:
{'Alice': 30, 'Charlie': 25, 'Eve': 35}

Again, do this with a loop, then with a dict comprehension.


Task 3 — Tag Users with Age Group
Create a new list of dictionaries. For each user, add a new field "group":
"adult" if age >= 21
"minor" if age < 21

Example:
{'name': 'Daisy', 'age': 17, 'active': False, 'group': 'minor'}

Stick to a regular for loop for this one — comprehensions with nested logic can get hairy, and we'll warm up to that in the bonus.


Bonus Task — Double Up!

Using a list comprehension, generate a list of strings:
Each string should say:
    "{name} is an adult" or "{name} is a minor" depending on their age.

Example:
['Alice is an adult', 'Bob is a minor', 'Charlie is an adult', ...]
"""

users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 19, "active": False},
    {"name": "Charlie", "age": 25, "active": True},
    {"name": "Daisy", "age": 17, "active": False},
    {"name": "Eve", "age": 35, "active": True},
]


# Task 1:
active_users_loop = []
active_users_compreh = []

for user in users:
    if user["active"] == True:
        active_users_loop.append(user["name"])

active_users_compreh = [user["name"] for user in users if user["active"] == True]


# Task 2:
adult_users_loop = {}
adult_users_compreh = {}

for user in users:
    if user["age"] >= 21:
        adult_users_loop[user["name"]] = user["age"]

adult_users_compreh = {user["name"]: user["age"] for user in users if user["age"] >= 21}


# Task 3:
user_tag_age_loop = []
user_tag_age_compreh = []

for user in users:
    temp = {}
    temp["name"] = user["name"]
    temp["age"] = user["age"]
    temp["active"] = user["active"]

    if user["age"] >= 21:
        temp["group"] = "adult"
    else:
        temp["group"] = "minor"

    user_tag_age_loop.append(temp)

for user in users:
    temp = user.copy()
    temp["group"] = "adult" if user["age"] >= 21 else "minor"
    user_tag_age_compreh.append(temp)


# Bonus task:
user_groups_loop = []
user_groups_compreh = []

for user in user_tag_age_loop:
    name = user["name"]
    group = user["group"]

    user_groups_loop.append(f"{name} is an {group}")


user_groups_compreh = [
    f"{user['name']} is an {'adult' if user['group'] == 'adult' else 'a minor'}"
    for user in user_groups_loop
]
