#! /bin/bash

# this script should be set to run automatically on boot.
# easiest way to do this is to add it to /etc/rc.local before the 'exit 0' line

# start fluidsynth using the start_fluid.sh script
sh /home/pi/lightshow/start_fluid.sh &

# wait for fluid synth to start up. This is necessary ensure the fluidsynth audio port has been created.
sleep 15

# set PCM volume to max
amixer -c 0 set PCM playback 100% unmute

# route keyboard midi input to fluidsynth
aconnect 20:0 128:0

# explicitly set audio output to the raspberry pi onboard Jack. 
# by default, audio will come out of the HDMI driver if it is plugged in.
sudo amixer cset numid=3 1

# start the python script that converts midi to DMX output
python /home/pi/lightshow/python_scripts/midi_2_dmx.py &
