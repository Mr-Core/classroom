"""
Exercise 2: Data Cleanup & Normalization

Your Data (already inconsistent and messy):

users = [
    {"name": " Alice ", "age": "30", "email": "ALICE@Email.com"},
    {"name": "bob", "age": 22, "email": "bob@email.com "},
    {"name": "CHARLIE", "age": "N/A", "email": "charlie@email.com"},
    {"name": "Daisy ", "age": 27, "email": "DAISY@email.COM"},
]


Task 1:
Clean up the name and email fields:
    Remove leading/trailing whitespace.
    Capitalize names properly (first letter uppercase).
    Lowercase the email address completely.


Task 2:
Convert the "age" field to an int.
If the age is not a valid number, set it to None.


Task 3:
Create a new cleaned list called cleaned_users that holds the cleaned user data.


Bonus Task:
Sort the cleaned_users list by age (ascending), skipping those with None as age (don't include them in the sorted list).
Print out cleaned_users in a readable format — one user per line.
"""

users = [
    {"name": " Alice ", "age": "30", "email": "ALICE@Email.com"},
    {"name": "bob", "age": 22, "email": "bob@email.com "},
    {"name": "CHARLIE", "age": "N/A", "email": "charlie@email.com"},
    {"name": "Daisy ", "age": 27, "email": "DAISY@email.COM"},
]


# Task 1:
for user in users:
    user["name"] = user["name"].strip().capitalize()
    user["email"] = user["email"].lower()


# Task 2:
for user in users:
    try:
        user["age"] = int(user["age"])
    except:
        user["age"] = None


# Task 3:
cleaned_users = []

for user in users:
    name = user["name"].strip().capitalize()

    email = user["email"].lower()

    age = 0
    try:
        age = int(user["age"])
    except:
        age = None

    new_user = {"name": name, "age": age, "email": email}

    cleaned_users.append(new_user)


# Bonus task:
sorted_users = sorted(
    [user for user in cleaned_users if user["age"] is not None], key=lambda x: x["age"]
)
