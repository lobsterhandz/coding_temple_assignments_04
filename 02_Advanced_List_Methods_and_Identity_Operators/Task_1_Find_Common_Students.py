submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
common_students = [student for student in submitted if student in attended]
print("Students who submitted and attended:", common_students)
