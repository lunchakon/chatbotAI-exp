import nltk
import random
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# ... previous code ...

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ["""I'm doing well, thanks!""", """I'm fine, how about you?"""]),
    (r'what is your name', ['My name is ChatBot.', "I'm ChatBot, nice to meet you!"]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye bye!']),
    (r'(.*) your name(.*)', ["I'm ChatBot.", "You can call me ChatBot."]),
    (r'(.*) (weather|temperature) (.*)', ["I'm sorry, I don't have real-time weather information."]),
    (r'(.*)', ["I'm not sure how to respond to that.", "Can you please rephrase that?", "I don't understand."])
]


chatbot = Chat(patterns, reflections)

def chat():
    print("Hello! I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()