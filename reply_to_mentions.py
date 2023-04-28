import argparse
import os
from typing import Union
from tweetipy import Tweetipy
from tweetipy.helpers import QueryBuilder
from helpers.get_random_text import getRandomText
from time import sleep
from datetime import datetime
from dotenv import load_dotenv

def parseArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Twitter bot: @babotsonicos',
        description="Picks a random Babaosnicos' song and tweets a random phrase from it.",
        epilog='For questions, reach out to the developer (GitHub user: /omirete).')

    parser.add_argument("-d", '--debug', required=False, action="store_true")

    return parser.parse_args()

def log_error(text: str):
    now = datetime.now().isoformat()
    log_exists = os.path.exists('error_log')
    with open('error_log', "a" if log_exists else "w", encoding='utf-8') as log:
        log.write(f"{now}:\t{text}\n")

def log(text: str):
    now = datetime.now().isoformat()
    log_exists = os.path.exists('log')
    with open('log', "a" if log_exists else "w", encoding='utf-8') as log:
        log.write(f"{now}:\t{text}\n")

def read_last_id() -> Union[str, None]:
    try:
        with open('last_id', 'r', encoding='utf-8') as f:
            return f.read().strip().strip('\n')
    except FileNotFoundError:
        return None

def write_last_id(id: str):
    if id != None and id != "":
        with open('last_id', 'w', encoding='utf-8') as f:
            f.write(id)

def main():

    args = parseArgs()
    debug: bool = args.debug

    api_key_me = os.getenv("API_KEY_ME")
    api_secret_me = os.getenv("API_SECRET_ME")
    oauth_key_me = os.getenv("OAUTH_KEY_ME")
    oauth_secret_me = os.getenv("OAUTH_SECRET_ME")
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    oauth_key = os.getenv("OAUTH_KEY")
    oauth_secret = os.getenv("OAUTH_SECRET")
    API_ME = Tweetipy(api_key_me, api_secret_me, oauth_key_me, oauth_secret_me)
    API = Tweetipy(api_key, api_secret, oauth_key, oauth_secret)

    q = QueryBuilder()

    id_of_last_tweet_replied_to = read_last_id()

    tweets = API_ME.tweets.search(
        q.with_exact_string('@babotsonicos')
        & q.NOT.from_user('babotsonicos')
        & q.has.mentions,
        since_id=id_of_last_tweet_replied_to,
        sort_order='recency',
        max_results=100
    )
    # Sort retrieved tweets from oldest to newest
    tweets.sort(key=lambda t: t.id) # Works in-place and returns None.

    # Only work on the first 20 tweets, to avoid getting throttled by Twitter.
    # If there are more than 20, they will be answered in the next run of the
    # script.
    for i in range(10):
        t = tweets[i]
        if debug:
            print(t)
        try:
            phrase = getRandomText()
            # Let's try to be good web citizens and wait at least three minutes
            # between each call to the API so we don't hit too hard on Twitter's
            # servers. This is also helpful if we want to avoid being banned. 😅
            API.tweets.write(phrase, in_reply_to_tweet_id=t.id)
            id_of_last_tweet_replied_to = t.id
            sleep(60*3)
        except Exception as e:
            # Log error
            log_error(str(e))
            break
        log(f'Wrote reply to tweet id: {t.id}')

    write_last_id(id_of_last_tweet_replied_to)

if __name__ == "__main__":
    load_dotenv()
    main()
