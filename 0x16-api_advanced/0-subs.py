#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    sub = res.json()
    if 'data' not in sub:
        return 0
    if 'subscribers' not in sub.get('data'):
        return 0
    return res.json()['data']['subscribers']
