#!/usr/bin/env python

from datetime import datetime
import logging
import random
import sys

def gen_dates():

    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)

    for i in range(1, 1000):
        try:
            randdate = datetime.strptime('{}/{}/{}'.format(random.randint(1,30), random.randint(1, 12), random.randint(2017, 2018)), '%d/%m/%Y').strftime("%d/%m/%Y")
        except ValueError:
            pass
        sys.stdout.write(randdate+"\n")
gen_dates()
