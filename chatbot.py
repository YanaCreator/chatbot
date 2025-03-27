print("Hi! I'm your mini chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello there!")
    elif user_input == "how are you":
        print("Bot: I'm just a bunch of code, but I'm doing great!")
    elif user_input == "what's your name":
        print("Bot: I'm MiniBot!")
    elif user_input == "bye":
        print("Bot: Bye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
