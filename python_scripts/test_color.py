#!/usr/bin/python
# script for testing dmx light colors

import sys
import pysimpledmx
import chroma
import time

def render_color(color):
    mydmx.setChannel(1, 255)  # set DMX channel 1 to full
    mydmx.setChannel(2, int(color[0] * 255))
    mydmx.setChannel(3, int(color[1] * 255))
    mydmx.setChannel(4, int(color[2] * 255))
    mydmx.render()  # render all of the above changes onto the DMX network

mydmx = pysimpledmx.DMXConnection('/dev/ttyUSB0')  # linux com port

color = chroma.Color('#000000')
render_color(color.rgb)
color = chroma.Color('#000000')
render_color(color.rgb)
print color.rgb
# time.sleep(2)

# close dmx connection
mydmx.close()
