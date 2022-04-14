#!/bin/sh
clear
git init
git add .
git commit -m "fixed API call error (forgot to strip newline from access_key.txt file)"
git push -u origin master
