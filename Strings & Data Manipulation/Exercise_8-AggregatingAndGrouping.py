"""
Exercise 4: Aggregating and Grouping

Scenario:

You're working with data from an online course platform.
Each student can be enrolled in multiple courses, and
each course can have a score if it's completed.

students = [
    {"name": "Alice", "courses": [{"title": "Math", "score": 95}, {"title": "English", "score": 88}]},
    {"name": "Bob", "courses": [{"title": "Math", "score": 72}]},
    {"name": "Charlie", "courses": [{"title": "History", "score": 91}, {"title": "Math", "score": 85}]},
    {"name": "Daisy", "courses": [{"title": "English", "score": 79}, {"title": "History", "score": 83}]},
]


Task 1:
Create a dictionary showing average score per course.

Example output:
{
  "Math": 84.0,
  "English": 83.5,
  "History": 87.0
}


Task 2:
Create a dictionary showing students who took each course.

Example output:
{
  "Math": ["Alice", "Bob", "Charlie"],
  "English": ["Alice", "Daisy"],
  "History": ["Charlie", "Daisy"]
}


Task 3:
Identify and print the top scorer per course.

Example output:
Math: Alice (95)
English: Alice (88)
History: Charlie (91)


Bonus Task:
Print a readable summary of each student in the following format:

Alice:
  - Math: 95
  - English: 88

Bob:
  - Math: 72

...
"""

students = [
    {
        "name": "Alice",
        "courses": [{"title": "Math", "score": 95}, {"title": "English", "score": 88}],
    },
    {"name": "Bob", "courses": [{"title": "Math", "score": 72}]},
    {
        "name": "Charlie",
        "courses": [{"title": "History", "score": 91}, {"title": "Math", "score": 85}],
    },
    {
        "name": "Daisy",
        "courses": [
            {"title": "English", "score": 79},
            {"title": "History", "score": 83},
        ],
    },
]


# Task 1:
course_avg_score = {}

for student in students:
    for course in student["courses"]:
        title = course["title"]
        score = course["score"]

        if title not in course_avg_score:
            course_avg_score[title] = []

        course_avg_score[title].append(score)

for course, score in course_avg_score.items():
    avg_score = sum(score) / len(score)

    course_avg_score[course] = avg_score

print(course_avg_score)


# Task 2:
students_in_courses = {}

for student in students:
    name = student["name"]
    course = ""

    for courses in student["courses"]:
        course = courses["title"]

        if course not in students_in_courses:
            students_in_courses[course] = []

        students_in_courses[course].append(name)

print(students_in_courses)


# Task 3:
top_student_per_course = {}

for student in students:
    name = student["name"]

    for course in student["courses"]:
        title = course["title"]
        score = course["score"]

        if (
            title not in top_student_per_course
            or top_student_per_course[title][1] < score
        ):
            top_student_per_course[title] = (name, score)

print(top_student_per_course)

# Bonus task:
student_summary = {}

for student in students:
    name = student["name"]
    course = ""
    score = 0
