#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(res.content.decode()))
    print('\t- content:', res.content.decode())
