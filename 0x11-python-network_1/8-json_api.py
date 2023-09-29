#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.:5000/search_user with the letter as a  parameter
"""
import requests
import sys

def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except requests.exceptions.HTTPError as e:
        print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    elif len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        sys.exit("Usage: ./8-json_api.py [letter]")

    search_user(letter)
