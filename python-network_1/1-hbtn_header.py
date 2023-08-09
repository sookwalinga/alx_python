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
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
