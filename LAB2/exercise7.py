""" 
Using the student records above, display each student’s
the student with the highest mark.
name and marks. Count the students who passed (marks ≥ 50), calculate the class average, and identify
"""
students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

passed = 0
highest = students[0]

for student in students:
    print("Name:", student["name"], "Marks:", student["marks"])

    if student["marks"] >= 50:
        passed += 1

    if student["marks"] > highest["marks"]:
        highest = student

print("Number of passed students:", passed)
print("Student with highest mark:", highest["name"])
print("Highest mark:", highest["marks"])