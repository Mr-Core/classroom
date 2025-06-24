"""
Exercise 7: Data Structure Manipulation (Intermediate)


Task 1: Reverse a dictionary (values to keys)
Given a dictionary where names are keys and favorite colors are values:

favorites = {
    "Alice": "Blue",
    "Bob": "Red",
    "Charlie": "Blue",
    "Daisy": "Green",
}

Create a new dictionary where colors are keys, and the value is a list of names that chose that color.


Task 2: Filter a list of dictionaries
Given a list of dictionaries representing books:

books = [
    {"title": "Book A", "rating": 4.7},
    {"title": "Book B", "rating": 3.9},
    {"title": "Book C", "rating": 4.2},
]

Create a new list that contains only books with a rating of 4.0 or higher.


Task 3: Flatten a nested list
Given:

nested = [[1, 2], [3, 4, 5], [6]]

Flatten this list to a single list: [1, 2, 3, 4, 5, 6].


Bonus Task: Group students by average score range
Given a list of students like before:

students = [
    {"name": "Alice", "scores": [90, 92, 85]},
    {"name": "Bob", "scores": [70, 65, 68]},
    {"name": "Charlie", "scores": [88, 91, 94]},
    {"name": "Daisy", "scores": [50, 60, 55]},
]

Group them into a dictionary where keys are score bands:
    "A" for avg ≥ 90
    "B" for avg ≥ 80
    "C" for avg ≥ 70
    "D" for avg ≥ 60
    "F" for avg < 60

"""

# Task 1:
favorites = {
    "Alice": "Blue",
    "Bob": "Red",
    "Charlie": "Blue",
    "Daisy": "Green",
}

favorites_revers = {}

for key, value in favorites.items():
    if value not in favorites_revers:
        favorites_revers[value] = []
    favorites_revers[value].append(key)

for color, person in favorites_revers.items():
    print(f"{color} chose: {', '.join(person)}")

print()

# Task 2:
books = [
    {"title": "Book A", "rating": 4.7},
    {"title": "Book B", "rating": 3.9},
    {"title": "Book C", "rating": 4.2},
]

high_books = []

for book in books:
    if book["rating"] >= 4.0:
        high_books.append(book["title"])

print(high_books)

print()

# Task 3:
nested = [[1, 2], [3, 4, 5], [6]]
flattened = []

for value in nested:
    if len(value) > 1:
        for i in range(len(value)):
            flattened.append(value[i])
    else:
        flattened.append(value[0])

print(flattened)

print()

# Bonus task:
students = [
    {"name": "Alice", "scores": [90, 92, 85]},
    {"name": "Bob", "scores": [70, 65, 68]},
    {"name": "Charlie", "scores": [88, 91, 94]},
    {"name": "Daisy", "scores": [50, 60, 55]},
]

student_scores = {}

for student in students:
    name = student["name"]
    score = student["scores"]
    average_score = sum(score) / len(score)
    if average_score >= 90:
        if "A" not in student_scores:
            student_scores["A"] = []
        student_scores["A"].append(name)

    elif average_score >= 80:
        if "B" not in student_scores:
            student_scores["B"] = []
        student_scores["B"].append(name)

    elif average_score >= 70:
        if "C" not in student_scores:
            student_scores["C"] = []
        student_scores["C"].append(name)

    elif average_score >= 60:
        if "D" not in student_scores:
            student_scores["D"] = []
        student_scores["D"].append(name)

    elif average_score < 60:
        if "F" not in student_scores:
            student_scores["F"] = []
        student_scores["F"].append(name)
    else:
        print("Unknown score")

for score, student in student_scores.items():
    print(f"Grade {score} achieved: {", ".join(student)}")

print()

print("Sorted print:")
for score in sorted(student_scores.keys()):
    print(f"Grade {score} achieved: {", ".join(student_scores[score])}")
