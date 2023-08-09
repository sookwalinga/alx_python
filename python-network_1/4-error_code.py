#!/usr/bin/env python3
"""
    Takes a URL as input, sends a request, and displays the response body or error code.
"""

import requests
import sys


def fetch_and_display(url):
    """
    Fetches the provided URL, displays the response body or error code.
    """
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display(url)
