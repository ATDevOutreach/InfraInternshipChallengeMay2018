#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 

@author: Josephine Nyoike
"""
import random
from datetime import datetime, timedelta
import sys

def date_generator():
    '''generate a random date'''
    begin = datetime(2017, 1, 1, 00, 00, 00)
    end = begin + timedelta(days=365 * 2)
    return begin + (end - begin) * random.random()

for i in range (1000):
    '''print exactly 1000 lines'''
    date = date_generator()
    date2 = date.strftime("%d/%m/%Y")
    sys.stdout.write(date2 + '\n')
   