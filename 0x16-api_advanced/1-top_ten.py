#!/usr/bin/python3
"""
Module contains function 'number_of_subscribers'
Query Reddit API and print first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Query Reddit API and print first 10 hot posts titles.
    If invalid subreddit given, print None;
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {"user-agent": "TestAgent1"}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    json = response.json()

    # print(json)
    posts = json.get("data").get("children")

    for post in posts:
        print(post.get('data').get("title"))
