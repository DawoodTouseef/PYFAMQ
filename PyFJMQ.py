import random 
from DATA.quotes import quotes
from DATA.facts import facts
from DATA.jokes import jokes
from DATA.motivations import motivations

def get_quote():
    return random.choice(quotes)

def get_jokes():
    return random.choice(jokes)

def get_facts():
    return random.choice(facts)

def get_motivation():
    return random.choice(motivations)
