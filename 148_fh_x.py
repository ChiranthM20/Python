file = None

try:
    file = open("student.txt", "x")
    file.write("Hello")
except Exception as e:
    print(f"Error: {e}")
finally:
    if file:
        file.close()