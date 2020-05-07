#!/usr/bin/python3
"""rite a function that queries the Reddit API and
   returns the number of subscribers (not active users,
   total subscribers) for a given subreddit. If an invalid
   subreddit is given, the function should return 0.
"""
import requests


def top_ten(subreddit):
    """    """
    top = requests.get('https://www.reddit.com/r/{}/hot.json'.
                       format(subreddit),
                       headers={"User-Agent": "Juliancastaneda"},
                       allow_redirects=False)
    info = top.json().get("data", {}).get("children", {})
    if top.status_code != 200:
        return print("None")
    for topten in info[:10]:
        print(topten.get("data", {}).get("title"))
