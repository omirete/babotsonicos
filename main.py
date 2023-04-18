import argparse
from argparse import Namespace
from tweetipy import Tweetipy
from json import load
import random

def parseArgs() -> Namespace:
    parser = argparse.ArgumentParser(
        prog='Twitter bot: @babotsonicos',
        description="Picks a random Babaosnicos' song and tweets a random phrase from it.",
        epilog='For questions, reach out to the developer (GitHub user: /omirete).')

    parser.add_argument('--api_key', required=True)
    parser.add_argument('--api_secret', required=True)
    parser.add_argument('--oauth_key', required=True)
    parser.add_argument('--oauth_secret', required=True)
    parser.add_argument('--text', required=False)

    return parser.parse_args()

def getRandomText() -> str:
    with open('phrases.json', 'r', encoding='utf-8') as f:
        phrases: dict = load(f)
        songs = list(phrases.keys())
        song = random.choice(songs)
        phrase = random.choice(phrases[song])
        return phrase

def postTweet(api_key: str, api_secret: str, oauth_key: str, oauth_secret: str, text: str = None):

    API = Tweetipy(
        oauth_consumer_key=api_key, # TWITTER_API_KEY
        oauth_consumer_secret=api_secret, # TWITTER_API_KEY_SECRET
        oauth_token=oauth_key,
        oauth_token_secret=oauth_secret
    )
    
    phrase = text if text != None else getRandomText()
    API.tweets.write(phrase)

def main():
    args = parseArgs()
    postTweet(**vars(args))

main()
