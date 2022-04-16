import json
import requests
from datetime import datetime

#Pulls access_key from access_key.txt file
def get_access_key():
	with open("access_key.txt", "r") as f:
		access_key = f.readline().rstrip('\n')
	return access_key

#Appends access key to url
def get_url(access_key):
	url = 'http://api.coinlayer.com/live?access_key=' + access_key
	return str(url)

def get_coin():
    case = input("Enter the coin you would like to analyze: ")  
    return case  

#Requests data from api using supplied URL
def get_data(url):
	request = requests.get(url)
	return request.json()

def get_dates():
    dates = {"day" : "", "month" : "", "year" : ""}   
    dates["day"] = input("Enter day: ")
    dates["month"] = input("Enter month: ")
    dates["year"] = input("Enter year: ")
    return dates
    
def live_analysis(coin):
	print("LIVE ANALYSIS: ")
	data = get_data(get_url(get_access_key()))
	print(data['rates'][coin])
	return 0;

def analysis_from_date():
	return 0;
	
def analysis_time_range():
	return 0;
	
def main():
	case = 0;
	while(case != 'q'):
		
		case = input("Options\nLive analysis [1]\nAnalysis from date [2]\nAnalysis of Time Range[3]\nExit [q]\n")
		
		print(type(case))
		
		if(int(case) == 1):
			live_analysis(get_coin())
			print()	
		
		elif(int(case) == 2):
			dates = get_dates()
			print(dates)
		
		else: print("Invalid option!")
main()
