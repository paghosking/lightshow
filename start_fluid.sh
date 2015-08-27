#! /bin/bash

# This script starts fluidsynth with some appropriate settings for the raspberry pi

fluidsynth -s -i -a alsa -m alsa_seq -o audio.alsa.device=hw:0 -f /home/lightuser/config.txt -z 256 -c 6 -r 48000 -l -p 'fluidsynth port' /usr/share/soundfonts/FluidR3_GM2-2.sf2  &
