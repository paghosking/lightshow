#!/usr/bin/python
# Python midi to color script for PERFORMANCE INSTRUMENTS
import sys

import pygame
import pygame.midi

import pysimpledmx

import lib
import threading
import Queue
import logging
import time

# settings
VEL_MAX = 127

# config for logging (prints for debugging threads)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def instrument(instrument):
    logging.debug('starting instrument thread for ' + instrument)

    if instrument == 'keyboard':
        while stopQ.empty():
            logging.debug(instrument + 'recieving keyboard midi input... ')
    elif instrument == 'drums':
        while stopQ.empty():
            logging.debug(instrument + 'recieving drums midi input...')
    else:
        logging.debug(instrument + 'ERROR: unknown instrument type')

    logging.debug(instrument + ' thread stopped')

def dmx():
    while True:
        pass

# set up queues
stopQ = Queue.Queue()

keyboard_thread = threading.Thread(name='keybaord', target=instrument, args=('keyboard',))
drums_thread = threading.Thread(name='drums', target=instrument, args=('drums',))

keyboard_thread.start()
drums_thread.start()


try:
    dmx()
except KeyboardInterrupt:
    print "\n\nterminating program..."
finally:
    # stop threads and clean up
    stopQ.put('stop')
    keyboard_thread.join()
    drums_thread.join()
    print "TERMINATED"
