#!/bin/bash
# Script that takes in a url, sends a POST request to the passed URL and display the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1
