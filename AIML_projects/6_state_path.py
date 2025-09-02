# 6. Write a Python program that moves from an initial state (0) to a goal state using +1 steps and prints the path.

def state_path(goal):
    state = 0
    path = []
    while state < goal:
        path.append(state)
        state += 1
    path.append(goal)
    print("Path:", path)
    
state_path(33)