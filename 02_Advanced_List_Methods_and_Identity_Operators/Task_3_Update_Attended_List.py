submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
common_students = [student for student in submitted if student in attended]
print("Students who submitted and attended:", common_students)

are_identical = sorted(submitted) == sorted(attended)
print("Are the lists identical:", are_identical)

attended = [student for student in attended if student in submitted]
print("Updated attended list:", attended)
