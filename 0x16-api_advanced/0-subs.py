#!/usr/bin/python3
"""
Module for API Operation
"""
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """
    headers = {'User-Agent': 'MyApp/1.0 (colinokumu89@gmail.com)'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
