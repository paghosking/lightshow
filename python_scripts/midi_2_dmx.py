#!/usr/bin/python
# Python midi to color script
import sys
sys.path.insert(0, '/home/pi/lightshow/python_scripts/')

import pygame
import pygame.midi

import pysimpledmx

import RPi.GPIO as GPIO
import time

import lib
import lib_lcd

# set up GPIO pins
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(lib_lcd.LCD_E, GPIO.OUT)  # E
GPIO.setup(lib_lcd.LCD_RS, GPIO.OUT) # RS
GPIO.setup(lib_lcd.LCD_D4, GPIO.OUT) # DB4
GPIO.setup(lib_lcd.LCD_D5, GPIO.OUT) # DB5
GPIO.setup(lib_lcd.LCD_D6, GPIO.OUT) # DB6
GPIO.setup(lib_lcd.LCD_D7, GPIO.OUT) # DB7
# push button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Initialise display
lib_lcd.lcd_init()

current_mode = 0
# define a callback function for button GPIO pin
def changeMode(void):
    global current_mode
    current_mode += 1
    global color
    color.change_mode(current_mode)
    text = "Mode: %d" % current_mode
    lcdPrint(text, 1)
    if current_mode == 1:
        lcdPrint("Color Scores", 2)
    elif current_mode == 2:
        lcdPrint("Rainbow", 2)
    elif current_mode == 3:
        lcdPrint("Reds", 2)
    elif current_mode == 4:
        lcdPrint("Greens", 2)
    elif current_mode == 5:
        lcdPrint("Blues", 2)
    elif current_mode > 5:
        current_mode = 0
        lcdPrint("Resonant Colors", 2)

# a more convenient function for printing text to LCD
def lcdPrint(text, line):
    if line==1:
        lib_lcd.lcd_string(text,lib_lcd.LCD_LINE_1)
    else:
        lib_lcd.lcd_string(text,lib_lcd.LCD_LINE_2)


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

# create an instance of the color handling class
color = lib.MidiColor(no_of_colors)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


def render_color(color):
    mydmx.setChannel(1, 255)  # set DMX channel 1 to full
    mydmx.setChannel(2, int(color[0] * 255))
    mydmx.setChannel(3, int(color[1] * 255))
    mydmx.setChannel(4, int(color[2] * 255))
    mydmx.render()  # render all of the above changes onto the DMX network

def main():

    # need access to the color class instance
    global color

    GPIO.add_event_detect(17, GPIO.RISING, callback=changeMode, bouncetime=300)

    lcdPrint("LightHub", 1)
    lcdPrint("Initialized", 2)

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
# if no light output is observed, try changing the midi_in port. Use aconnect -i shell command to list midi ports
    midi_in = pygame.midi.Input(2)

    # turn off DMX light initially
    render_color(color.output_color.rgb)

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


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print "\n\nprogram terminated\n"
    finally:
        mydmx.close()
        lib_lcd.lcd_byte(0x01, lib_lcd.LCD_CMD)
        lib_lcd.lcd_string("Goodbye!",lib_lcd.LCD_LINE_1)
        GPIO.cleanup()




