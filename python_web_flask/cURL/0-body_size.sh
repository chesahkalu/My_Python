#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.

# -s = Silent mode. Don't show progress meter or error messages.
# | = Pipe the output of the previous command to the next command.4
# wc -c = Print the byte size of the HTTP response header.(character count)
curl -s "$1" | wc -c
