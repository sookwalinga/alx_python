#!/usr/bin/env python3
"""
    Takes a URL as input, sends a request, and displays the value of the X-Request-Id header.
"""
import requests
import sys


def get_x_request_id(url):
    """
    Sends a request to the provided URL and retrieves the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id header in the response.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    return x_request_id


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
    else:
        url = sys.argv[1]
        x_request_id = get_x_request_id(url)
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
