#!/bin/sh
your_date='your desired date'
sed -i "s/^Current date.*/Current date ${your_date}/" /home/dick/Desktop/4chan-Crypto-Analyizer/test.txt
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ add .
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ commit -m "Test"
git -C /home/dick/Desktop/4chan-Crypto-Analyizer/ push origin master
