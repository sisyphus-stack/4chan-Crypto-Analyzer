# credits to Anarov for improved example.py
from __future__ import print_function 
import basc_py4chan
import urllib, json, os, datetime
from unidecode import unidecode
import time
from urllib.request import Request, urlopen


def main():
    # grab the first thread on the board by checking first page
    board = basc_py4chan.Board('lit')
    all_thread_ids = board.get_all_thread_ids()
    BIT_counter = 0
    """for i in range(0, len(all_thread_ids)):
        thread_id = all_thread_ids[i]
        current_thread = board.get_thread(thread_id)
        #print(current_thread)
        topic = current_thread.topic
        #print('Topic Repr', topic)
        print('Postnumber', topic.post_number)
        #print('Timestamp',  topic.timestamp)
        #print('Datetime',   repr(topic.datetime))
        #print('Subject',    topic.subject)
        #print('Comment',    topic.text_comment)
        #print('Replies',    current_thread.replies)
        for j in range(0, len(current_thread.replies)):
            #print('Reply: ', current_thread.replies[j].text_comment)
            #print(current_thread.replies[0].text_comment.find("catalog"))
            if(current_thread.replies[j].text_comment.find("bitcoin") != -1):
                #print(current_thread.replies[j].text_comment + '\n\n\n')                
                BIT_counter += 1
            if(current_thread.replies[j].text_comment.find("BIT") != -1):
                BIT_counter += 1
                #print(current_thread.replies[j].text_comment + '\n\n\n') 
        #print(len(current_thread.replies))
        print(i)"""
    # thread information
   
    # topic information
    #print("#Bitcoin = ", BIT_counter)
    
    url = "https://a.4cdn.org/lit/archive.json"
    response = urlopen(url)
    threads = json.loads(response.read())
    #for i in range(0, len(threads)):    
    print(threads[1473])
    current_thread = board.get_thread(threads[1473])
    topic = current_thread.topic
    print("\n\n topic ", topic)
    #print('Topic Repr', topic)
    print('Postnumber', topic.post_number)
    print('Timestamp',  topic.timestamp)
    print('Datetime',   repr(topic.datetime))
    print('Subject',    topic.subject)
    print('Comment',    topic.text_comment)
    #print('Replies',    current_thread.replies)
    for j in range(0, len(current_thread.replies)):
            print('Reply: ', current_thread.replies[j].text_comment)
            #print(current_thread.replies[0].text_comment.find("catalog"))
            if(current_thread.replies[j].text_comment.find("bitcoin") != -1):
                print(current_thread.replies[j].text_comment + '\n\n\n')                
                BIT_counter += 1
            if(current_thread.replies[j].text_comment.find("BIT") != -1):
                BIT_counter += 1
                print(current_thread.replies[j].text_comment + '\n\n\n') 
    #print(len(threads))
    
   
if __name__ == '__main__':
    main()
