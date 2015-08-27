# Python midi to color script
import sys

import pygame
import pygame.midi

import pysimpledmx

import lib

# mydmx = pysimpledmx.DMXConnection('/dev/cu.usbserial-6AYP9O1D') # mac dmx com port
# mydmx = pysimpledmx.DMXConnection(5)  # windows dmx com port
mydmx = pysimpledmx.DMXConnection('/dev/ttyUSB0')  # linux com port

# settings
screen_height = 200
screen_width = 200
no_of_colors = 12
top_key = 84
bottom_key = 36
key_range = top_key - bottom_key
VEL_MAX = 127

# timing
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


def render_color(color):
    mydmx.setChannel(1, 255)  # set DMX channel 1 to full
    mydmx.setChannel(2, int(color[0] * 255))
    mydmx.setChannel(3, int(color[1] * 255))
    mydmx.setChannel(4, int(color[2] * 255))
    mydmx.render()  # render all of the above changes onto the DMX network


pygame.init()
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE, 32)
# pygame.display.set_caption("MIDI TO DMX")
# screen.fill(pygame.Color("black"))
# pygame.display.flip()
# background rect
background_rect = pygame.Rect(0, 0, screen_width, screen_height)

# initiate midi input
pygame.midi.init()

# midi_in = pygame.midi.Input(pygame.midi.get_default_input_id())
midi_in = pygame.midi.Input(1)

# init MidiColor class
color = lib.MidiColor(no_of_colors)
render_color(color.output_color.rgb)  # turn light off initially

while True:

    # fps = clock.tick(FRAMES_PER_SECOND)

    # for event in pygame.event.get():
        # if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN):
        # if (event.type == pygame.KEYDOWN):
            # midi_in.close()
            # render_color([0, 0, 0])  # turn the lights off on exit
            # sys.exit()

    while midi_in.poll():
        midi_event = midi_in.read(1)
        # print midi_event
        if midi_event[0][0][0] == 144:
            key_id = midi_event[0][0][1]
            note = key_id % no_of_colors
            # print "midi event: " + str(midi_event[0][0]) + " note: " + str(note)
            if midi_event[0][0][2]:
                vel = midi_event[0][0][2]
                color.add_color(note, vel, VEL_MAX)
            else:
                color.rem_color(note)
            # print color.output_color.rgb

    color.update()
    render_color(color.output_color.rgb)
