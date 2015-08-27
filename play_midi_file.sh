#!/bin/bash

# a simple script to play a midi file. That is all. 
# It takes an argument which is the path to the midi file.

fluidsynth -a alsa -m alsa_seq -l -i /usr/share/soundfonts/FluidR3_GM2-2.sf2 $1
