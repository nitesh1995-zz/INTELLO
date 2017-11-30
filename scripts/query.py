#!/usr/bin/python
import random
import string
import sys
import time
import os
import shelve
import os.path

query = string.join(sys.argv[1:])
fileDir = os.path.dirname(os.path.realpath('__file__'))
queryLogFile = os.path.join(fileDir, 'logs/query.log')
target = open(queryLogFile, "a")
target.write("\n")
now = time.strftime("%c")
    ## date and time representation
target.write("Current date & time " + now)
target.write("\n")
target.write(query)
target.flush()
target.close()
response = "YOUR QUERY HAS BEEN RECORDED. I WILL INFORM MY BOTMASTER KONAG ABOUT THE EVENT."
print response
