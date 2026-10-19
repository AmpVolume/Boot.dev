# Quote-Generator
import random

quotes = [
    "Be yourself; everyone else is already taken. — Oscar Wilde",
    "In the middle of every difficulty lies opportunity. — Albert Einstein",
    "The best way to predict the future is to invent it. — Alan Kay",
    "Life is what happens when you’re busy making other plans. — John Lennon",
    "Do what you can, with what you have, where you are. — Theodore Roosevelt"
]

def random_quote():
    print(random.choice(quotes))

if __name__ == "__main__":
    random_quote()
