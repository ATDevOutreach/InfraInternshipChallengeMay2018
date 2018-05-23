#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 

@author: Josephine Nyoike
"""
import datetime
import sys
def check_date_format(date):
    '''check that the date provided is in the correct format, else throw an error'''
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Malformed output")
def count_months(months):
    '''count the months used in a line and print their percentages'''
    unique_months = []
    for month in months:
        if month not in unique_months:
            unique_months.append(month)
    for month1 in unique_months:
        c = months.count(month1)
        percentage = c/len(months) * 100
        string_percentage = month1 + ': '+ str(percentage) + '%'
        print(string_percentage)
def main():
    
    lines = sys.stdin.readlines()
    months = []
    for date in lines:
        check_date_format(date)
        if date.year == 2018 and date.day in range(0, 15):
            print(date)
        month_name = date.strftime("%B")
        months.append(month_name)
    
    months.sort()
    count_months(months)
main()