# credits to Anarov for improved example.py
from __future__ import print_function 
import basc_py4chan
import urllib, json, os, datetime
from unidecode import unidecode
import time
from urllib.request import Request, urlopen


def main():
    board = basc_py4chan.Board('biz')
    #all_thread_ids = board.get_all_thread_ids()
    BIT_counter = 0
    
    #find way to make case for archive. 
    #It seems that I'm able to get the threads from archive, but when I pull info from 
    #standard basc_py4chan.Board('biz') I only pull threads from catalog.
    url = "https://a.4cdn.org/biz/archive.json"
    response = urlopen(url)
    threads = json.loads(response.read())
    for i in range(0, len(threads)):    
        print(i)    
        print("Timestamp: ", threads[i])
        current_thread = board.get_thread(threads[i])      
        print(current_thread.topic.timestamp) 
        for j in range(0, len(current_thread.replies)):
            if(current_thread.replies[j].text_comment.find("bitcoin") != -1):
                print(current_thread.replies[j].text_comment + '\n\n\n')                
                BIT_counter += 1
            if(current_thread.replies[j].text_comment.find("BIT") != -1):
                BIT_counter += 1
                print(current_thread.replies[j].text_comment + '\n\n\n') 

    print(len(threads))
    
   
if __name__ == '__main__':
    main()
