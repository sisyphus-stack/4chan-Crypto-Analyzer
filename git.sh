#!/bin/sh
touch '/home/dick/Desktop/4chan-Crypto-Analyizer/test.txt'
file='/home/dick/Desktop/4chan-Crypto-Analyizer/test.txt'
your_date='5/20/22'
ls -i "$file"
printf '%s\n' H ",g/^Current date.*/s//${your_date}/" wq | ed -s "$file"
ls -i "$file"
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ add .
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ commit -m "Test"
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ push origin master
