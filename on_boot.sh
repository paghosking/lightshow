#! /bin/bash

# this script should be set to run automatically on boot.

# initialize the gpio pins - turn them off to start with
# the GPIO pins are connected to 3 status LEDs
# at the time of writing this the LEDs didn't really serve a useful purpose - but they do look pretty
/home/pi/wiringPi/gpio/gpio -g mode 2 out
/home/pi/wiringPi/gpio/gpio -g mode 3 out
/home/pi/wiringPi/gpio/gpio -g mode 4 out
/home/pi/wiringPi/gpio/gpio -g write 2 0
/home/pi/wiringPi/gpio/gpio -g write 3 0
/home/pi/wiringPi/gpio/gpio -g write 4 0


# start fluidsynth using the start_fluid.sh script
sh /home/pi/start_fluid.sh &

# turn one the first status LED on to indicate that fluidsynth has been started
/home/pi/wiringPi/gpio/gpio -g write 2 1

# wait for fluid synth to start up. This is necessary ensure the fluidsynth audio port has been created.
sleep 15

# route keyboard midi input to fluidsynth
aconnect 20:0 128:0

# turn on the second status LED
/home/pi/wiringPi/gpio/gpio -g write 3 1

# explicitly set audio output to the raspberry pi onboard Jack. 
# by default, audio will come out of the HDMI driver if it is plugged in.
sudo amixer cset numid=3 1

# start the python script that converts midi to DMX output
python /home/pi/python_scripts/midi_2_dmx.py &

# turn on the last status LED to indicate that the system is fully operational
/home/pi/wiringPi/gpio/gpio -g write 4 1
