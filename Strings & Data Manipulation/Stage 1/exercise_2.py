"""
Stage 1 - Exercise 2: Nested Structures & Access

You're going to work with:
    A list of dictionaries (e.g., student records)
    A dictionary containing lists (e.g., course rosters)

Try the tasks below:


students = [
    {"name": "Alice", "scores": [85, 90, 82]},
    {"name": "Bob", "scores": [78, 81, 86]},
    {"name": "Charlie", "scores": [92, 88, 95]}
]

course_roster = {
    "Math": ["Alice", "Bob"],
    "Science": ["Alice", "Charlie"],
    "History": ["Bob", "Charlie"]
}


Task 1:
Print each student's name and their average score.
(Hint: use sum() and len())


Task 2:
Print each course and the number of students enrolled.


Task 3:
Print the name of each student along with the courses they are taking.
(Hint: Loop through course_roster and reverse-map names to course lists)


Bonus Task:
Find the student(s) with the highest average score.
"""

students = [
    {"name": "Alice", "scores": [85, 90, 82]},
    {"name": "Bob", "scores": [78, 81, 86]},
    {"name": "Charlie", "scores": [92, 88, 95]},
]

course_roster = {
    "Math": ["Alice", "Bob"],
    "Science": ["Alice", "Charlie"],
    "History": ["Bob", "Charlie", "Tommy"],
}


# Task 1:

for student in students:
    name = student["name"]
    scores = student["scores"]
    average = sum(scores) / len(scores)
    print(f"{name} has an average score of {average:.2f}")

print()


# Task 2:

for key, value in course_roster.items():
    print(f"Course {key} has {len(value)} students enrolled.")

print()


# Task 3:

student_courses = {}

for course, students in course_roster.items():
    for student in students:
        if student not in student_courses:
            student_courses[student] = []
        student_courses[student].append(course)

for student, courses in student_courses.items():
    print(f"{student} is enrolled in: {', '.join(courses)}")

print()


# Bonus task: using heapq

# import heapq
#
# heap = []
#
# for student in students:
#     name = student["name"]
#     scores = student["scores"]
#     average = sum(scores) / len(scores)
#     heapq.heappush(heap, (-average, name))
#
# high_score_student = heapq.heappop(heap)
#
# print(
#     f"Student with the highest score is {high_score_student[1]} with a score of {-high_score_student[0]:.2f}"
# )


# Bonus task: using max

# max_average = 0
# top_student = ""
#
# for student in students:
#     name = student["name"]
#     scores = student["scores"]
#     average = sum(scores) / len(scores)
#     if average > max_average:
#         max_average = average
#         top_student = name
#
# print(
#     f"Student with the highest score is {top_student} with a score of {max_average:.2f}"
# )
