import json
import requests

url = 'http://api.coinlayer.com/api/live?access_key=3a673fdf0140f6398fbe3546c7cf47f1'

r = requests.get(url)
data = r.json()