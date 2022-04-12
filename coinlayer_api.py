import json
import requests
from datetime import datetime

url = 'http://api.coinlayer.com/api/timeframe?access_key=3a673fdf0140f6398fbe3546c7cf47f1&start_date=2018-04-01&end_date=2018-04-30&symbols=BTC'

"""
http://api.coinlayer.com/timeframe
    ? access_key = YOUR_ACCESS_KEY
    & start_date = 2018-04-01
    & end_date = 2018-04-30
    & symbols = BTC,ETH
"""
r = requests.get(url)
data = r.json()

print(data)

#timestamp = int(json.dumps(data['timestamp']))

#dt_object = datetime.fromtimestamp(timestamp)



#print("dt_object =", dt_object)

#with open("coins.txt", "w") as file1: 
#       file1.write(json.dumps(data['rates']))

