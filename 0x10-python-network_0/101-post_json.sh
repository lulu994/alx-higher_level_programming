#!/bin/bash
# Script that sends a requests to a URL argument, displays onyl the status code of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
