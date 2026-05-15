from datetime import datetime
import random


# =========================
# LOGIN SYSTEM
# =========================

def login():

    print("===== AI CHATBOT LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234":
        print("\nLogin Successful!\n")
        return True

    else:
        print("\nInvalid Username or Password")
        return False


# =========================
# SAVE CHAT HISTORY
# =========================

def save_chat(user, bot_reply):

    with open("chat_history.txt", "a") as file:
        file.write(f"User: {user}\n")
        file.write(f"Bot: {bot_reply}\n")
        file.write("-" * 30 + "\n")


# =========================
# CHATBOT LOGIC
# =========================

def get_response(user_input):

    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey"]
    bye_words = ["bye", "exit", "quit"]

    if user_input in greetings:
        return random.choice(["Hi!", "Hello!", "Hey there!"])

    elif "how are you" in user_input:
        return "I am fine. Thanks for asking!"

    elif "your name" in user_input:
        return "I am an AI Chatbot."

    elif "python" in user_input:
        return "Python is a programming language."

    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence."

    elif "cybersecurity" in user_input:
        return "Cybersecurity protects systems from attacks."

    elif "what is machine learning" in user_input:
        return "Machine Learning is a branch of AI that learns from data."

    elif "what is data science" in user_input:
        return "Data Science is the study of data to extract insights."

    elif "help" in user_input:
        return "Ask me about Python, AI, cybersecurity, date, time."

    elif "date" in user_input:
        return str(datetime.now().date())

    elif "time" in user_input:
        return str(datetime.now().strftime("%H:%M:%S"))

    elif user_input in bye_words:
        return "Goodbye! Have a nice day."

    elif user_input == "":
        return "Please type something."

    else:
        return "Sorry, I don't understand."


# =========================
# MAIN CHAT LOOP
# =========================

def chatbot():

    print("===== WELCOME TO AI CHATBOT =====")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You: ")
        response = get_response(user)

        print("Bot:", response)

        save_chat(user, response)

        if user.lower() in ["bye", "exit", "quit"]:
            break


# =========================
# MAIN PROGRAM
# =========================

if __name__ == "__main__":

    if login():
        chatbot()

    else:
        print("Access Denied.")