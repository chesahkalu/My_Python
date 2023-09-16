#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.

# -I = Retrieve only the HTTP headers(Head request)
# grep "Allow" = Search for the line that contains the word "Allow"
# cut -d " " -f 2- = Cut the line at the space character and print the second field and all the following fields.
# cut = Cut out selected portions of each line of a file(in form of columns)
# -d = Use the delimiter character to separate the fields.
# -f = Select only these fields.
# 2- = Print the second field and all the following fields.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
