#!/bin/sh
echo "this is a new line" >> /home/dick/Desktop/4chan-Crypto-Analyizer/test.txt
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ add .
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ commit -m "Test"
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ push origin master
