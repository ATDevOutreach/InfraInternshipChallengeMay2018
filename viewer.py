#!/usr/bin/env python

import sys
from dateutil.parser import *
from datetime import datetime
import calendar

def check(string):
    try:
        #parses the line to date format
        DATE = parse(string)
        #checks the month the line is in
        countmonth(DATE)
        return True
    except ValueError:
        print ("Malformed input")
        return False


def countmonth(date):
    monthnum = int(date.month)
    #adds number of lines in the month
    MONTHS[monthnum] = MONTHS[monthnum] + 1.0


def view():
    print("Correct logs: %d"%CORRECTINPUT)
    for i, num in enumerate(MONTHS):
        if i != 0:
            print("%s: %.2f%%"%(calendar.month_name[i], num*100/CORRECTINPUT)) 


#reads line from stdin(logger.py output)
MONTHS = [0] * 13
CORRECTINPUT = 0.0
for line in sys.stdin:
    line.rstrip(" ")
    #checks if line is in date format
    #counts the correctly date formatted lines
    if check(line) == True:
        CORRECTINPUT += 1
#output results
view()

    
