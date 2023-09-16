#!/bin/bash
# Bash scripts that sends a POST request to a given URL.

# -s = Silent mode. Don't show progress meter or error messages.
# -X = specifies the request method - POST instead of the default GET request.
# -d = specifies HTTP POST data
# This data can be used by the server to process the request and generate a response

curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

