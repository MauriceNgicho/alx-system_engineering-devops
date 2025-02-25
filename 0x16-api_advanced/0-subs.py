#!/usr/bin/python3
"""A function that gets the total number of subscribers"""
import requests


def number_of_subscribers(subreddit):

    # Deffine the API url
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # custom header
    headers = {"User-Agent": "MauriceRedditScraper/1.0 (by u/MauriceNgicho)"}

    # Set get request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # check request status
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]

    # If not a valid subreddit
    return 0
