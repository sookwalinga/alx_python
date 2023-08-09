#!/usr/bin/env python3
"""
    Takes GitHub credentials (username and personal access token) as input,
    uses Basic Authentication to access GitHub API, and displays user id.
"""

import requests
import sys


def get_user_id(username, token):
    """
    Uses Basic Authentication to fetch user id from GitHub API and displays it.
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    get_user_id(username, token)
