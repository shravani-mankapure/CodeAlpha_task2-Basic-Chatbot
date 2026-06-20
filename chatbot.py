def get_response(user_input):
    
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "howdy"]:
        return "Hi there! 👋 How can I help you today?"

    # Asking how the bot is
    elif user_input in ["how are you", "how are you?", "how r u", "how do you do"]:
        return "I'm doing great, thanks for asking! 😊 What about you?"

    # User is doing well
    elif user_input in ["i'm fine", "i am fine", "good", "i'm good", "fine"]:
        return "That's wonderful to hear! 🎉"

    # User is not well
    elif user_input in ["not good", "bad", "not well", "sad", "i'm sad"]:
        return "Oh no! I'm sorry to hear that. I hope you feel better soon! 💙"

    # Bot's name
    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "I'm sitara 🤖, your simple AI assistant! Its nice to meet you!!"

    # What can the bot do
    elif user_input in ["what can you do", "help", "help me"]:
        return (
            "I can chat with you! Try saying:\n"
            "  • hello / hi / hey\n"
            "  • how are you\n"
            "  • what is your name\n"
            "  • Tell me a Joke\n"
            "  • bye"
        )

    # Telling Joke
    elif user_input in ["tell me a joke", "joke", "say something funny"]:
        return "Why don't scientists trust atoms? Because they make up everything! 😄"

    #exiting
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit", "tata"]:
        return "Goodbye! Have a wonderful day! 👋"

    # Time / date (bonus)
    elif user_input in ["what time is it", "what's the time"]:
        return ("I don't have a clock, but your device does! ⏰")

    # Unknown input
    else:
        return "Sorry, I didn't quite understand that. Type 'help' to see what I can do!"


def run_chatbot():
    """
    Main loop that keeps the chatbot running until the user says bye/quit.
    """
    print("=" * 45)
    print("     Welcome to Sitara ChatBot 🤖")
    print("  Type 'help' to see What commands i have.")
    print("     Type 'bye' or 'quit' to exit.")
    print("=" * 45)
    print()

    # List of exit keywords to stop the loop
    exit_keywords = ["bye", "goodbye", "see you", "exit", "quit", "tata"]

    while True:
        # Get input from user
        user_input = input("You: ")

        # Skip empty input
        if not user_input.strip():
            print("ChatBot: Please type something!\n")
            continue

        # Get and print the response
        response = get_response(user_input)
        print(f"ChatBot: {response}\n")

        # Exit condition
        if user_input.lower().strip() in exit_keywords:
            break


# Entry point
if __name__ == "__main__":
    run_chatbot()
