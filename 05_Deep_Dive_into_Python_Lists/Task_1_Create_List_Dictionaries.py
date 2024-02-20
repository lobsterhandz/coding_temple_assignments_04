students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
student_info = [{"name": students[i], "grade": grades[i], "activity": activities[i]} for i in range(len(students))]
print("Students info:", student_info)
