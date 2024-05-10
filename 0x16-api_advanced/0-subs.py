#!/usr/bin/python3
"""
Module contains function 'number_of_subscribers'
Query Reddit API and return number of subscribers.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Query Reddit API and return number of subscribers.
    If invalid subreddit given, return 0;
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"user-agent": "TestAgent1"}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 404:
        return 0

    json = response.json()
    # print(json)
    return json.get('data').get('subscribers')

# number_of_subscribers("kenya")
