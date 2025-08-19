att =int(input("enter your attendence percentage :"))
is_teacher_friend = input("True or False :").strip().lower()=="true"

# and

if att>75:
    print("You can write the Exam")
elif att<75 and is_teacher_friend==True:
    print("You can attend the Exam")
else:
    print("You cannot attend the Exam")
