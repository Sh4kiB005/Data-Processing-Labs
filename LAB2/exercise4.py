def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


marks = [85, 75, 65, 80, 70]

grade = calculate_grade(marks)
print("Grade:", grade)