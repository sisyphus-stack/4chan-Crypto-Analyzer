/biz/ --> Crypto Analyzer
=========================
A project designed to analyse the activity of /biz/ and see the frequency of certain coins correlates to fluctuations of those coins in a given timeframe.

My hypothesis is that the more a cryptocurrency is mentioned on a certain day, the higher the change will be in price of that coin (either higher or lower).

I am using Bibliotheca Anonoma's **complete Python Wrapper for the 4chan API.** (See documentation below) in order to scrape from biz forums.

For the Crypto API I am using coinlayer (https://coinlayer.com/) as they had a free API that I could use.

My hope is that once I determine whether my hypothesis is correct or not, I can generalize this program to work with other platform API's (eg Reddit, Twitter). Using data from different sights can hopefully give some insights on possible movements in the crypto sphere.


4chan Python Library
====================
The Bibliotheca Anonoma's **complete Python Wrapper for the 4chan API.**
Uses requests, respects if-modified-since headers on updating threads.
Caches thread objects. Fun stuff.

An absolute must if you want to interface with or scrape from 4chan,
using a Python script.

`Hosted Documentation <http://basc-py4chan.readthedocs.org/en/latest/index.html>`_

`Github Repository <https://github.com/bibanon/BASC-py4chan>`_

You can install this library `straight from
PyPi <https://pypi.python.org/pypi/BASC-py4chan>`_ with::

    pip install basc-py4chan
    
    
CoinLayer
=========
https://coinlayer.com/


                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                        Version 2, December 2004

     Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

     Everyone is permitted to copy and distribute verbatim or modified
     copies of this license document, and changing it is allowed as long
     as the name is changed.

                DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
       TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

      0. You just DO WHAT THE FUCK YOU WANT TO.
