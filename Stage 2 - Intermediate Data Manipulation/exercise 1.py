"""
Exercise 1: Grouping and Summarizing

You're given a list of transactions. Each transaction is a dictionary with "user", "amount", and "type".

transactions = [
    {"user": "Alice", "amount": 50, "type": "deposit"},
    {"user": "Bob", "amount": 20, "type": "withdrawal"},
    {"user": "Alice", "amount": 30, "type": "withdrawal"},
    {"user": "Daisy", "amount": 100, "type": "deposit"},
    {"user": "Bob", "amount": 70, "type": "deposit"},
    {"user": "Daisy", "amount": 20, "type": "withdrawal"},
]


Task 1:
Create a dictionary that stores the total deposited amount for each user.

Output should look like:
{"Alice": 50, "Daisy": 100, "Bob": 70}


Task 2:
Create a dictionary that shows the net balance (deposit - withdrawal) per user.

Output should look like:
{"Alice": 20, "Bob": 50, "Daisy": 80}


Task 3:
List all users who made more than one transaction, regardless of type.

Output should be:
["Alice", "Bob", "Daisy"]

Note: This one's sneaky — you'll want a dictionary or collections.Counter!


Bonus Task:
Print a summary like:

Alice: 2 transactions, net balance 20
Bob: 2 transactions, net balance 50
Daisy: 2 transactions, net balance 80

"""

transactions = [
    {"user": "Alice", "amount": 50, "type": "deposit"},
    {"user": "Bob", "amount": 20, "type": "withdrawal"},
    {"user": "Alice", "amount": 30, "type": "withdrawal"},
    {"user": "Daisy", "amount": 100, "type": "deposit"},
    {"user": "Bob", "amount": 70, "type": "deposit"},
    {"user": "Daisy", "amount": 20, "type": "withdrawal"},
    {"user": "Josh", "amount": 10, "type": "deposit"},
]


# Task 1:
total_deposit_amount = {}

for transaction in transactions:
    if transaction["type"] == "deposit":
        user = transaction["user"]

        if user not in total_deposit_amount:
            total_deposit_amount[user] = 0

        total_deposit_amount[user] += transaction["amount"]

print(total_deposit_amount)

print()


# Task 2:
net_balances = {}

for transaction in transactions:
    if transaction["user"] not in net_balances:
        net_balances[transaction["user"]] = 0

    if transaction["type"] == "deposit":
        net_balances[transaction["user"]] += transaction["amount"]
    elif transaction["type"] == "withdrawal":
        net_balances[transaction["user"]] -= transaction["amount"]

print(net_balances)

print()


# Task 3:
counter_dict = {}
multiple_transaction_users = []

for transation in transactions:
    if transation["user"] not in counter_dict:
        counter_dict[transation["user"]] = 0

    counter_dict[transation["user"]] += 1

for user, no_transaction in counter_dict.items():
    if no_transaction >= 2:
        multiple_transaction_users.append(user)

print(multiple_transaction_users)

print()


# Bonus Task:
for user, count in counter_dict.items():
    print(f"{user}: {count} transactions, net balance {net_balances[user]}")
