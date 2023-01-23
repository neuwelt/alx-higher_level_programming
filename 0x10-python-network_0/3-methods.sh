#!/bin/bash
# bash script that takes in a URL and displays all HTTP methods that the server will accept
curl -ILs "$1" | grep Allow | cut -d " " -f2-
