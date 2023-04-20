# @babotsonicos 🎵🤖

This is the code used to run the [@babotsonicos](https://twitter.com/babotsonicos) bot account in Twitter.

The [`phrases.json`](https://github.com/omirete/babotsonicos/blob/master/phrases.json) file contains a list of songs (w/ lyrics) from [Babasonicos](https://www.babasonicos.com/) (an argentinian music group).

## 🤖 What does the bot do?
It tweets a random lyric phrase from the Babasonicos band every three hours.

## 🤔 What does this code do?
The magic happens in the `main.py` script, and it just does three steps:
1. It picks a random song from `phrases.json`.
2. It picks a random phrase from the chosen song.
3. It tweets the chosen phrase from the [@babotsonicos](https://twitter.com/babotsonicos) twitter account.

## 👀 How does it run? And the server?
This bot requires no traditional server because it just relies on GitHub actions.

You can find a workflow in this repository that triggers every three hours and runs the `main.py` script (see [`/.github/workflows/manual.yml`](https://github.com/omirete/babotsonicos/blob/master/.github/workflows/manual.yml)).

There is really not more to it than that.

## ❗ Disclaimer
### TL;DR
I am not the owner of the bot account in Twitter. I just developed it for the owner because it was a fun project. 🥳

### The longer story
The bot was originally created using a website that enabled non-programmers to build their own Twitter bots. Thus, @babotsonicos existed and had been running fine for two years before me.

At some point, the website that was running it stopped working (likely due to changes in the API pricing) and consequently the bot stopped working as well.

When I saw the owner of the bot [tweeting about it](https://twitter.com/babotsonicos/status/1647646057919139843), I approached and [offered to help](https://twitter.com/babotsonicos/status/1648437484836237318), because it seemed fun and I also wanted to give my own Twitter library for Python ([Tweetipy](https://github.com/omirete/tweetipy)) a test drive in a "real world" use case. 🤩
