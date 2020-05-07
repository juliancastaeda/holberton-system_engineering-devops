#!/usr/bin/python3
"""Write a function that queries the Reddit API and
   returns the number of subscribers (not active users,
   total subscribers) for a given subreddit. If an invalid
   subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """function that realized get for reddit"""
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'user-agent': 'X-Modhash'}
    url_format = requests.get(url.format(subreddit), headers=headers).json()
    try:
        name = url_format['data']['subscribers']
        return name
    except:
        return 0
