#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.

# -s = Silent mode. Don't show progress meter or error messages.
# -H = Specify header content type to be application/json.
# -d = Specify HTTP POST data to post.
# cat "$2" = Read the contents of the JSON file.

curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
