a = lambda a,b,c,d: a+b-c*d
print(a(2,4,7,9))



student_marks = [
    {"name":"Chiranth", "marks":80 },
    {"name":"Alice", "marks":85},
    {"name":"Bob", "marks":90}
]

student_marks.sort(key = lambda x: x["marks"], reverse = True)
print(student_marks)