#!/bin/bash
#  script that sends a request a URL, and displays the size of the body of the response in bytes.
curl -Is "$1" | grep Content-Length | cut -d: -f2
