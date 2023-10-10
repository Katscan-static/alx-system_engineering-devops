#!/usr/bin/python3
"""
    this Module returns the number of subscribers for a particular reddit post
"""


import requests


def number_of_subscribers(reddit):
    """
        this function returns the number of subscribers

        args:

            reddit (str): a reddit post

            Returns (int): returns number of susbscribers
    """

    url = f"https://www.reddit.com/r/{reddit}/about.json"
    headers = {"User-Agent": "My Reddit Scrapper"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            number_of_subs = data["data"]["subscribers"]
            return number_of_subs
        except KeyError:
            return 0

    else:
        return 0
