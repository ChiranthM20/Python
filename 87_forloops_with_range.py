# adding marks to student using index values

students = ["A", "B", "C"]
marks = [10,20,30]
student_marks = {}

for i in range(len(students)):  # we can also use range(3)
    student_marks[students[i]] = marks[i]
print(student_marks)

