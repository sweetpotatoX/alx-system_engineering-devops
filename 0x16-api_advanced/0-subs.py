#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            # If the 'subscribers' key is not found in the JSON response
            print("Error: 'subscribers' key not found in JSON response.")
            return None
    elif response.status_code == 404:
        # If the subreddit does not exist
        print("Error: Subreddit '{}' does not exist.".format(subreddit))
        return None
    else:
        # If the request fails for any other reason
        print("Error: Request failed with status code {}".format(response.status_code))
        return None
