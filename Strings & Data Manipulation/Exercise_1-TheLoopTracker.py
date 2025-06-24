"""
Exercise 5 - The Loop Tracker

Objective:
Practice looping through lists, tuples, and dictionaries while accessing both keys and values.


Task:
You are given the following three data structures:

names = ["Alice", "Bob", "Charlie"]
scores = (85, 92, 78)
gradebook = {
    "Alice": "B",
    "Bob": "A",
    "Charlie": "C"
}


Write a script that does the following:

    Loops through the names list and prints:
        Name: Alice

    Loops through the scores tuple using enumerate and prints:
        Student #1 scored 85

    Loops through the gradebook dictionary and prints:
        Bob received grade A


Bonus (Optional):
    Add a new student and grade to the gradebook dictionary.
    Print all students who received a grade lower than "B".
"""

names = ["Alice", "Bob", "Charlie"]
scores = (85, 92, 78)
gradebook = {"Alice": "B", "Bob": "A", "Charlie": "C"}

# Task 1:
for name in names:
    print(f"Name: {name}")


# Task 2:
for index, value in enumerate(scores):
    print(f"Student #{index+1} scored {value}")


# Task 3:
for key, value in gradebook.items():
    print(f"{key} received grade {value}")


# Bonus task 1:
gradebook["Tommy"] = "F"


# Bonus task 2:
print("Students with grade lower than B: ", end="")
for key, value in gradebook.items():
    if value in ["C", "D", "F"]:  # if value == "C" or value == "D" or value == "F":
        print(f"{key}, ", end="")
