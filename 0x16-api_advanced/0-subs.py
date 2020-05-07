#!/usr/bin/python3
"""hi
   hello
   and
   user
"""
import requests


def number_of_subscribers(subreddit):
    """
    """
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'user-agent': 'X-Modhash'}
    url_format = requests.get(url.format(subreddit), headers=headers).json()
    try:
        name = url_format['data']['subscribers']
        return name
    except:
        return 0
