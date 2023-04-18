from tweetipy import Tweetipy
from json import load
import random
from os import getenv

with open('phrases.json', 'r', encoding='utf-8') as f:
    phrases: dict = load(f)

def getRandomText() -> str:
    songs = list(phrases.keys())
    song = random.choice(songs)
    phrase = random.choice(phrases[song])
    return phrase


API = Tweetipy(
    getenv("TWITTER_API_KEY"),
    getenv("TWITTER_API_KEY_SECRET")
)

phrase = getRandomText()
API.tweets.write(phrase)
