#!/usr/bin/python3
"""
    This module returns the the top 10 postd of a  reddit
"""


import requests


def top_ten(subreddit):
    """
        This function gets the top 10 posts

        args:
            subreddit (str): the reddit to get the top 10 posts from
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit Scrapper"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            for post in data["data"]["children"]:
                title = post["data"]["title"]
                print(title)

        except KeyError:
            print(None)
    else:
        print(None)
