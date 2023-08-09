#!/usr/bin/python3
"""Find the value of the X-Request-Id in response"""

import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id header from the response of the given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id header, or a message if the header is not found.
    """
    try:
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            return x_request_id
        else:
            return "X-Request-Id header not found in the response."
    except requests.exceptions.RequestException as e:
        return "Error making the request: {}".format(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <url>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = fetch_x_request_id(url)
    print(x_request_id)
