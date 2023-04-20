import random
from json import load

def getRandomText() -> str:
    with open('phrases.json', 'r', encoding='utf-8') as f:
        phrases: dict = load(f)
        songs = list(phrases.keys())
        song = random.choice(songs)
        phrase = random.choice(phrases[song])
        return phrase
