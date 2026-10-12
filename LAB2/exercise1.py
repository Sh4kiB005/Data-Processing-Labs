"""
Create a list containing the marks of five courses. Display the total,
average, highest mark, and lowest mark. Count the number of passed courses, using 50 as the pass mark.

"""
marks = [85, 72, 45, 90, 60]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0
for mark in marks:
    if mark >= 50:
        passed += 1

print("Total marks:", total)
print("Average marks:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Passed courses:", passed)
