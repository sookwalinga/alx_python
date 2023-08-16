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

#!/usr/bin/python3

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)
x_request_id = response.headers.get('X-Request-Id', None)

if x_request_id:
    print(x_request_id)
else:
    print("X-Request-Id header not found in the response.")
