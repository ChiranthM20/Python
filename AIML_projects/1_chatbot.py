# 1. Write a Python program to simulate a basic AI chatbot that replies to user greetings and weather-related questions.

def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ").strip().lower()
        if not user:   # If user just presses enter
            print("Chatbot: Please type something...")
            continue
        if user in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        elif "weather" in user:
            print("Chatbot: The weather is sunny today!")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don’t understand that.")

chatbot()
