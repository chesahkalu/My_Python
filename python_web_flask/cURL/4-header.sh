#!/bin/bash
# Send a GET request to a given URL with a header variable.

# -s = Silent mode. Don't show progress meter or error messages.
# -H = Pass custom header(s) to server. Can be used for Authentication.
# X-School-User-Id = The header variable.
curl -sH "X-School-User-Id: 98" "$1"
