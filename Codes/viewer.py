'''
Infra Internship Code Challenge

Task 2

This program reads lines of text from the standard input,counts how many times a month appears and displays dates from 0-14th of 2018
'''
import sys
month_count = [0] * 12


def format(date):
    #Displays Malformed Input whenever the input isn't in the format DD/MM/YYYY
    if int(date[:2]) > 0 and int(date[:2]) < 31:
        if int(date[3:5]) > 0 and int(date[3:5]) < 13:
            if (len(date[6:-1]) == 4):
                return 0
    else:
        print 'Malformed Input'


def read(date):
    #increments the month_count for month X whenever it appears
    month = int(date[3:5]) - 1
    month_count[month] = month_count[month] + 1


def count():
    #prints the logged months with the percentage that month appears
    month = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    print "_________________________________________"
    for x in month:
        perc = month_count[month.index(x)] / 10.0
        print x + ': ' + str(perc) + '%'
    print "_________________________________________"


def fourteenth(date):
    #Print lines from 0-14th of 2018
    if int(date[:2]) > 0 and int(date[:2]) < 14:
        if int(date[-3:-1]) == 18:
            print date[:-1]


for date in sys.stdin:
    if date.strip():
        format(date)
        read(date)
        fourteenth(date)

count()
