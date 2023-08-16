#!/usr/bin/env python3
"""
    Takes a URL and an email address as input, sends a POST request, and displays the response body.
"""

import requests
import sys


def main():
    """
    Sends a POST request with the provided email to the given URL and displays the response body.
    """
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Response body:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")


if __name__ == "__main__":
    main()
