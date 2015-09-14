#!/usr/bin/python
# test script for GPIO and LCD 16x2 control

import sys
sys.path.insert(0, '/home/pi/lcd_screen_test/')

import lib_lcd

import RPi.GPIO as GPIO
import time

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
# define callback function for GPIO button
def changeMode(void):
    global current_mode
    current_mode += 1
    text = "Mode: %d" % current_mode
    lcdPrint(text, 1)
    lcdPrint("", 2)
    if current_mode > 4:
        current_mode = 0


# a more convenient way of printing text to LCD
def lcdPrint(text, line):
    if line==1:
        lib_lcd.lcd_string(text,lib_lcd.LCD_LINE_1)
    else:
        lib_lcd.lcd_string(text,lib_lcd.LCD_LINE_2)

def main():

    GPIO.add_event_detect(17, GPIO.RISING, callback=changeMode, bouncetime=300)

    lcdPrint("LightHub", 1)
    lcdPrint("Initialized", 2)

    while True:
        pass

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lib_lcd.lcd_byte(0x01, lib_lcd.LCD_CMD)
    lib_lcd.lcd_string("Goodbye!",lib_lcd.LCD_LINE_1)
    GPIO.cleanup()
