#!/bin/bash
# Get the response body for a given URL for 200 status code responses.

# -s = Silent mode. Don't show progress meter or error messages.
# -L = Follow redirects in URL
curl -sL "$1"
