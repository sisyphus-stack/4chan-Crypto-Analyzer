import json
import requests
from datetime import datetime

def get_access_token():
	with open("access_key.txt", "r") as f:
		access_token = str(f.readline())
	return access_token

def get_datetime():
	#improve parameters
	datetime = input("Please enter yyyy-mm-dd:\n")
	return datetime

def get_url(access_token, datetime, timeframe):
	if(timeframe == 0):
		url = "http://api.coinlayer.com/api/live?" + access_token
		return url
	elif(timeframe == 1):
		url = "http://api.coinlayer.com/api/" + datetime + "?" + access_token
		return url
def get_data(url):
	request = requests.get(url)
	return request.json()

#url = 'http://api.coinlayer.com/api/timeframe?access_key=3a673fdf0140f6398fbe3546c7cf47f1&start_date=2018-04-01&end_date=2018-04-30&symbols=BTC'

"""
http://api.coinlayer.com/timeframe
    ? access_key = YOUR_ACCESS_KEY
    & start_date = 2018-04-01
    & end_date = 2018-04-30
    & symbols = BTC,ETH
"""
access_token = get_access_token()
datetime = get_datetime()
url = get_url(access_token, datetime, 1)
data = get_data(url)
print(access_token)
print(datetime)
print(url)
print(data)

#timestamp = int(json.dumps(data['timestamp']))

#dt_object = datetime.fromtimestamp(timestamp)



#print("dt_object =", dt_object)

#with open("coins.txt", "w") as file1: 
#       file1.write(json.dumps(data['rates']))

