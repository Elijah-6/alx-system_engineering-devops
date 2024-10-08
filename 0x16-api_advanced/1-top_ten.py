#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    sub = res.json()
    hot_posts = sub['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        hot_posts.pop(0)
        for post in hot_posts:
            print(post['data']['title'])
