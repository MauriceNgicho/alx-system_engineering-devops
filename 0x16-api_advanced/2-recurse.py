#!/usr/bin/python3
"""A function that queries API, returns a list of all hot articles"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API to get all hot article titles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}  # Using pagination

    response = requests.get(
                url, headers=headers,
                params=params, allow_redirects=False

            )

    if response.status_code != 200:
        return None  # Return None if subreddit is invalid

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post["data"].get("title"))

    after = data.get("after")
    if after:
        # Recursive call with pagination
        return recurse(subreddit, hot_list, after)

    return hot_list
