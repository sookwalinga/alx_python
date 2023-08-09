#!/usr/bin/env python3
"""
Module to send a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
"""

import requests
import sys


def search_user(letter):
    """
    Send a POST request to http://0.0.0.0:5000/search_user with the provided letter as a parameter.

    Args:
        letter (str): The letter to be used as the 'q' parameter in the request.
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        try:
            json_response = response.json()
            if json_response:
                user_id = json_response.get('id')
                user_name = json_response.get('name')
                print("[{}] {}".format(user_id, user_name))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <letter>".format(sys.argv[0]))
        sys.exit(1)

    letter = sys.argv[1]
    search_user(letter)
