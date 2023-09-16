#!/bin/bash
# Sends a GET request to a given URL and display the response status code.

# -s = Silent mode. Don't show progress meter or error messages.
# -o = Write output to file instead of stdout.
# -/dev/null = Write output to a null device. A special file that discards any data written to it
# -w = Write the specified format to stdout after completion.
# %{http_code} = Variable that displays the HTTP response code.

#This  allows to check the response code of an HTTP request without having to parse the entire response body.

curl -s -o /dev/null -w "%{http_code}" "$1"
