#!/usr/bin/python3
"""Function to query the number of subscribers for a given subreddit"""


import requests


def number_of_subscribers(subreddit):
    """queries the subreddit provided as argument and return subscriber No"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced: :v1.0.0 (by /u/absaGH)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
        results = response.json().get("data")
        return results.get("subscribers")
