# Day 60: rule-based chatbot

responses = {
    "hello": "Hi there! How can I help?",
    "how are you": "I'm just code, but I'm doing great!",
    "bye": "Goodbye! Have a great day."
}

print("Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print(f"Chatbot: {responses['bye']}")
        break
    print(f"Chatbot: {responses.get(user_input, 'Sorry, I did not understand that.')}")