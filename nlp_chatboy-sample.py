import nltk
import random
import string

# Download necessary nltk packages (run this once)
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

# Sample data for the chatbot
responses = {
    "hello": ["Hello there!", "Hi!", "Greetings! How can I help you?"],
    "how are you": ["I'm just a program, but I'm doing well!", "All good here, thanks for asking!"],
    "what is your name": ["I'm Python ChatBot.", "Call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# Lemmatizer to normalize text
lemmatizer = WordNetLemmatizer()

# Function to preprocess user input
def preprocess_input(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Function to find the best response
def get_response(user_input):
    tokens = preprocess_input(user_input)
    
    for key, value in responses.items():
        if key in tokens:
            return random.choice(value)
    return "I'm not sure how to respond to that."

# Main chatbot function
def nlp_chatbot():
    print("Chatbot: Hi! I'm an NLP-powered chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

nlp_chatbot()
