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

import chroma

# settings
VEL_MAX = 127

# config for logging (prints for debugging threads)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def instrument(instrument, midi_port):
    logging.debug('starting instrument thread for ' + instrument)
    # open midi port
    midi_in = pygame.midi.Input(midi_port)

    if instrument == 'keyboard':

        # only valid id's should be processed
        valid_ids = [144, 128]

        while stopQ.empty():
            while midi_in.poll():
                midi_event = midi_in.read(1)
                # logging.debug(midi_event)
                if midi_event[0][0][0] in valid_ids:
                    key_id = midi_event[0][0][1]
                    if midi_event[0][0][2]:
                        vel = midi_event[0][0][2]
                        keyboardQ.put([key_id, vel])
                    else:
                        keyboardQ.put([key_id, 0])


    elif instrument == 'drums':

        while stopQ.empty():
            while midi_in.poll():
                midi_event = midi_in.read(1)
                # if midi_event[0][0][0] != 248:
                logging.debug(midi_event)

    else:
        while midi_in.poll():
            logging.debug(instrument + 'ERROR: unknown instrument type')

    midi_in.close()
    logging.debug(instrument + ' thread stopped')


def render_color(color, channel):
    mydmx.setChannel(1, 255)
    mydmx.setChannel(channel, int(color[0] * 255))
    mydmx.setChannel(channel + 1, int(color[1] * 255))
    mydmx.setChannel(channel + 2, int(color[2] * 255))

def dmx():

    global mydmx

    # set up frame limit
    clock = pygame.time.Clock()

    # initialize color class instances
    keyboard_color = lib.MidiColor(12)
    keyboard_color.change_mode(5)

    while True:
        fps = clock.tick(60) # frame limit
        while not (keyboardQ.empty() and drumsQ.empty()):
            if not keyboardQ.empty():
                midi_data =  keyboardQ.get()
                midi_data[0] %= 12
                if midi_data[1]:
                    keyboard_color.add_color(midi_data[0], midi_data[1], VEL_MAX)
                else:
                    keyboard_color.rem_color(midi_data[0])
            if not drumsQ.empty():
                print drumsQ.get()
        keyboard_color.update()
        # print keyboard_color.output_color
        render_color(keyboard_color.output_color.rgb, 2)
        mydmx.render()


# mydmx = pysimpledmx.DMXConnection('/dev/cu.usbserial-6AYP9O1D') # mac dmx com port
# mydmx = pysimpledmx.DMXConnection(5)  # windows dmx com port
mydmx = pysimpledmx.DMXConnection('/dev/ttyUSB0')  # linux com port

# pygame midi initialization
pygame.init()
pygame.midi.init()

# set up queues
stopQ = Queue.Queue()
keyboardQ = Queue.Queue()
drumsQ  = Queue.Queue()

keyboard_thread = threading.Thread(name='keybaord', target=instrument, args=('keyboard', 3))
drums_thread = threading.Thread(name='drums', target=instrument, args=('drums', 5))

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
    mydmx.close()
    print "TERMINATED"
