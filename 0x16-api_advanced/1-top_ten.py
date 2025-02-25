#!/usr/bin/python3
"""A function that queries, prints titles of the first 10 hot posts listed"""
import requests


def top_ten(subreddit):
    """"Prints the titles of the first 10 hot posts"""

    # Deffine the API url
    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=10"

    # custom header
    headers = {"User-Agent": "Mozilla/5.0"}

    # Set get request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # check request status
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post["data"].get("title"))

    # If not a valid subreddit print None.
    else:
        print(None)
