# 4. Write a program to store and print key characteristics of Artificial Intelligence using a Python dictionary.

def ai_characteristcs():
    ai = {
        "Learning": "AI can learn from data",
        "Reasoning": "AI can make logical decisions",
        "Problem Solving": "AI can solve problems efficiently",
        "Perception": "AI can recognize speech, images, etc."
    }

    print("AI Characteristcs")
    for key,value in ai.items():
        print(f"{key} : {value}")

ai_characteristcs()