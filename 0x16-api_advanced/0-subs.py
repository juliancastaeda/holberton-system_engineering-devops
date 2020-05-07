#!/usr/bin/python3
"""

"""
import json
import requests


def number_of_subscribers(subreddit):
    subscribers = requests.get('https://www.reddit.com/r/{}/about.json'.
                               format(subreddit),
                               headers={"User-Agent": "X-Modhash"},
                               allow_redirects=False)
    if subscribers.status_code != 200:
        return 0
    return subscribers.json().get("data").get("subscribers")
