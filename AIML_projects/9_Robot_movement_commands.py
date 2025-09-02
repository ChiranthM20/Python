# 9. Write a program that takes user input like "move forward" or "turn left" and makes a robot respond accordingly.

def robot_commands():
    while True:
        command = input("Enter command (move forward, turn left, turn right, stop): ").lower()
        if command == "move forward":
            print("Robot: Moving forward...")
        elif command == "turn left":
            print("Robot: Turning left...")
        elif command == "turn right":
            print("Robot: Turning right...")
        elif command == "stop":
            print("Robot: Stopping...")
            break
        else:
            print("Robot: Invalid command.")

robot_commands()