import argparse
from tweetipy import Tweetipy
from helpers.get_random_text import getRandomText

def parseArgs() -> argparse.Namespace:
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

def postTweet(api_key: str, api_secret: str, oauth_key: str, oauth_secret: str, text: str = None):

    API = Tweetipy(
        oauth_consumer_key=api_key, # TWITTER_API_KEY
        oauth_consumer_secret=api_secret, # TWITTER_API_KEY_SECRET
        oauth_token=oauth_key,
        oauth_token_secret=oauth_secret
    )
    
    phrase = text if (text != None and text != "") else getRandomText()
    API.tweets.write(phrase)

def main():
    args = parseArgs()
    postTweet(**vars(args))

if __name__ == "__main__":
    main()
