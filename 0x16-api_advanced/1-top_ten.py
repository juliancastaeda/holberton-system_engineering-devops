#!/usr/bin/python3
"""
"""
import requests


def top_ten(subreddit):
    top = requests.get('https://www.reddit.com/r/{}/hot.json'.
                       format(subreddit),
                       headers={"User-Agent": "Julian"},
                       allow_redirects=False)
    info = top.json().get("data", {}).get("children", {})
    if top.status_code != 200:
        return print("None")
    for topten in info[:10]:
        print(topten.get("data", {}).get("title"))
