'''
Infra Internship Code Challenge

Task 1

This script writes 1000 lines of text to standard output. Each line of text is a date in the form dd/MM/YYYY
'''
import random
import sys


def randomize():
    day = str(random.randint(1, 30))
    month = str(random.randint(1, 12))
    year = random.randint(17, 18)
    return day.zfill(2) + '/' + month.zfill(2) + '/20' + str(year) + '\n'


def output():
    for x in range(0, 1000):
        print randomize()


output()
