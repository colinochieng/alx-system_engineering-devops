#!/usr/bin/python3
"""
Module for recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """

    :param subreddit: subreddit
    :param hot_list: list
    :return: a list containing the titles of all
    hot articles for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'MyApp/1.0 (colinokumu89@gmail.com)'
               }
    limit = 100
    params = {
        'limit': limit,
        "count": count
    }
    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code:
        data = response.json().get('data')
        after = data.get("after")
        count = data.get("dist")
        records = data.get('children')
        for i in records:
            hot_list.append(i.get('data').get('title'))
        if after:
            return recurse(subreddit, hot_list, after=after, count=count)
        return hot_list
    else:
        return None
