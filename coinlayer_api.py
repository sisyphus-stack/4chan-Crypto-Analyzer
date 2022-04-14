import json
import requests
from datetime import datetime

#Pulls access_key from access_key.txt file
def get_access_key():
	with open("access_key.txt", "r") as f:
		access_key = str(f.readline())
	return access_key

#Appends access key to url
def get_url(access_key):
	url = 'http://api.coinlayer.com/live?access_key=' + access_key
	return url

#Requests data from api using supplied URL
def get_data(url):
	request = requests.get(url)
	return request.json()

def main():
	access_key = get_access_key()
	url = get_url(access_key)
	
	#receive error when supplying appended url
	data = get_data(url)
	print(data)
	
	#however, API call works when I hardcode url
	data = get_data('http://api.coinlayer.com/live?access_key=3a673fdf0140f6398fbe3546c7cf47f1')
	print(data)
main()
