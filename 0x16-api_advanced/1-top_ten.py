#!/usr/bin/python3
"""
Request from reddit API
"""
import requests


def top_ten(subreddit):
    """
    :param subreddit:  Reddit API
    :return: the first 10 hot posts listed for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'MyApp/1.0 (colinokumu89@gmail.com)'
               }
    response = requests.get(url=url, headers=headers)

    if response.status_code:
        data = response.json()
        for i in range(0, 10):
            records = data.get('data').get('children')[i]
            print(records.get('data').get('title'))
    else:
        print(None, response.status_code)
        print(response.json())
