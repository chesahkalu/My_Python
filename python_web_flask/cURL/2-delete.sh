#!/bin/bash
# Send a DELETE request to a given URL and display the response body.

# -s = Silent mode. Don't show progress meter or error messages.
# X = specifies the request method - DELETE
curl -sX DELETE "$1"
