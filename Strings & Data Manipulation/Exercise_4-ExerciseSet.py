"""
Stage 3 - Exercise Set


Task 1: Group Words by Their First Letter

words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]

Create a dictionary where each key is the first letter of words, and the value is a list of all words starting with that letter.

Expected Output (order may vary):
{
  'a': ['apple', 'apricot', 'avocado'],
  'b': ['banana', 'blueberry'],
  'c': ['cherry']
}


Task 2: Filter and Rename Keys

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 25},
    {"name": "Daisy", "age": 17}
]

Filter out people under 21
Create a new list of dictionaries, each with keys "first_name" and "years_old" instead of "name" and "age".

Expected Output:
[
    {"first_name": "Alice", "years_old": 30},
    {"first_name": "Charlie", "years_old": 25}
]


Task 3: Count All Word Occurrences

sentences = [
    "the quick brown fox",
    "jumps over the lazy dog",
    "the fox is quick and brown"
]

Count how many times each word appears across all sentences.
Output as a dictionary.

Expected Output:
{
    'the': 3,
    'quick': 2,
    'brown': 2,
    'fox': 2,
    'jumps': 1,
    'over': 1,
    'lazy': 1,
    'dog': 1,
    'is': 1,
    'and': 1
}


Bonus Task: Top Performer per Department

departments = {
    "Engineering": [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 72}
    ],
    "Marketing": [
        {"name": "Charlie", "score": 95},
        {"name": "Daisy", "score": 85}
    ],
    "Design": [
        {"name": "Eve", "score": 91},
        {"name": "Frank", "score": 87}
    ]
}

For each department, print the name of the top-scoring person and their score.

Expected Output:
Engineering: Alice (88)
Marketing: Charlie (95)
Design: Eve (91)
"""

# Task 1:
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]

sort_by_letter = {}

for word in words:
    first_letter = word[0]
    if first_letter not in sort_by_letter:
        sort_by_letter[first_letter] = []
    sort_by_letter[first_letter].append(word)

for letter, word in sort_by_letter.items():
    print(f"'{letter}': {word}")

print()

# Task 2:
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 25},
    {"name": "Daisy", "age": 17},
]

filtered_data = []

for employee in data:
    if employee["age"] >= 21:
        filtered_data.append(
            {"first_name": employee["name"], "years_old": employee["age"]}
        )

for employee in filtered_data:
    print(employee)

print()

# Task 3:
sentences = [
    "the quick brown fox",
    "jumps over the lazy dog",
    "the fox is quick and brown",
]

seen_words = {}

for sentance in sentences:
    words = sentance.split()
    for word in words:
        if word not in seen_words:
            seen_words[word] = 0
        seen_words[word] += 1

for word, count in seen_words.items():
    print(f"'{word}': {count}")

print()

# Bonus task:
departments = {
    "Engineering": [{"name": "Alice", "score": 88}, {"name": "Bob", "score": 72}],
    "Marketing": [{"name": "Charlie", "score": 95}, {"name": "Daisy", "score": 85}],
    "Design": [{"name": "Eve", "score": 91}, {"name": "Frank", "score": 87}],
}

for department, employees in departments.items():
    name = ""
    score = 0
    for employee in employees:
        if employee["score"] > score:
            name = employee["name"]
            score = employee["score"]
    print(f"{department}: {name} ({score})")
