#!/usr/bin/python3
"""
    this module get all the hot subreddits
"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    A recursive function that returns a list of titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The subreddit name.
        hot_list (list, optional): A list of titles (used in recursion).
        after (str, optional): The "after" parameter for pagination.

    Returns:
        list or None: A list of titles or None if no results are found.
    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    if after:
        url += f"&after={after}"

    headers = {"User-Agent": "My Reddit Scraper"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            for post in data["data"]["children"]:
                title = post["data"]["title"]
                hot_list.append(title)

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

        except KeyError:
            return None

    else:
        return None
