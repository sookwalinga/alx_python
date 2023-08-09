#!/usr/bin/env python3
"""
    Fetches https://alu-intranet.hbtn.io/status
"""

import requests


def fetch_and_display_status():
    """
    Fetches https://alu-intranet.hbtn.io/status and displays response body.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_and_display_status()
