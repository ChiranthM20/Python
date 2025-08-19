att = int(input("Enter your attendance percentage: "))
is_teacher_friend = input("Is the teacher your friend? (True/False): ").strip().lower()=="true"

if att >= 75:
    print("You can write the Exam")
elif att < 75 and is_teacher_friend:
    print("You can attend the Exam")
else:
    print("You cannot attend the Exam")
