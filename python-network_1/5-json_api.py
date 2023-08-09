#!/usr/bin/env python3
"""
    Takes a letter as input, sends a POST request, and displays id and name or error message.
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request with the provided letter to the URL and displays id and name or error message.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    search_user(letter)
