class GCU:
    def __init__(self, name, course):
        self.name=name
        self.course=course
    def greet(self):
        print(f"Hello {name} you are studying {course}")

A = GCU("Chiranth", "CS")
A.greet()