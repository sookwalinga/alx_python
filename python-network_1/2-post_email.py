#!/usr/bin/env python3
"""
    Takes a URL and an email address as input, sends a POST request, and displays the response body.
"""

import requests
import sys


def post_email(url, email):
    """
    Sends a POST request with the provided email to the given URL and displays the response body.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
