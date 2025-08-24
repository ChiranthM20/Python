class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.__marks = {} 

    def get_marks(self):
        return self.__marks

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks   

    def calculate_average(self):
        if len(self.__marks) == 0:
            return 0
        total = sum(self.__marks.values())
        average = total / len(self.__marks)
        return average

    def is_passed(self):
        return all(mark >= 35 for mark in self.__marks.values())

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"


class ReportCard:
    def generate(self, student):
        student_marks = student.get_marks()
        print("\n---------------- REPORT CARD ----------------")
        print(f"Name     : {student.name}")
        print(f"Roll No. : {student.roll}")
        print("\n---- Marks ----")
        for subject, marks in student_marks.items():
            print(f"{subject} : {marks}")
        print("----------------")
        print(f"Average : {student.calculate_average():.2f}")
        print(f"Grade   : {student.calculate_grade()}")
        if student.is_passed():
            print("Result  : PASS ")
        else:
            print("Result  : FAIL ")
        print("----------------\n")



name = input("Enter Student Name: ")
roll = input("Enter Roll No: ")
Stu = Student(name, roll)
report = ReportCard()

while True:
    print("========= MENU =========")
    print("1. Add Marks")
    print("2. Show Report Card")
    print("3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        subject = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        Stu.add_marks(subject, marks)

    elif choice == 2:
        report.generate(Stu)

    elif choice == 3:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")
