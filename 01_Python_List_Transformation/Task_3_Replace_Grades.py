grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print("Sorted grades:", sorted_grades)

average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)


updated_grades = ["Failed" if grade < 80 else grade for grade in grades]
print("Updated grades:", updated_grades)
