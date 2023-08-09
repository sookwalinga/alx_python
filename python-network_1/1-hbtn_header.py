#!/usr/bin/env python3
"""
Module to send a request to a URL and display the value of the variable X-Request-Id
in the response header.
"""

import requests
import sys


def get_x_request_id(url):
    """
    Send a request to the specified URL and display the value of the variable X-Request-Id
    in the response header.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
