#!/usr/bin/env python3
"""
    Takes a URL as input, sends a request, and displays the value of the X-Request-Id header.
"""

import requests
import sys


def fetch_and_display_request_id(url):
    """
    Fetches the provided URL, displays the value of X-Request-Id header in response.
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    if request_id:
        print(request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display_request_id(url)
