import nltk
import random
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data (only needs to be done once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm a conversational chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a developer using Python's NLTK library.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am a virtual chatbot, I do not have a physical location.',]
    ],
    [
        r"how is the weather in (.*)?",
        ["I am sorry, I cannot provide real-time weather information.", "Weather information is outside of my capabilities at the moment."]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I don't have health in the traditional sense.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a big fan of programming competitions.",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["I don't have personal preferences for actors, but I can tell you about movies.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Could you please rephrase that?", "I am not sure how to respond to that.", "My apologies, I am still under development and can't answer that."]
    ]
]

def chatbot():
    print("Hi, I'm Chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()