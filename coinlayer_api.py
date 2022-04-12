import json
import requests
from datetime import datetime

url = 'http://api.coinlayer.com/api/live?access_key=3a673fdf0140f6398fbe3546c7cf47f1'

r = requests.get(url)
data = r.json()

timestamp = int(json.dumps(data['timestamp']))

dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)

with open("coins.txt", "w") as file1: 
       file1.write(json.dumps(data['rates']))

