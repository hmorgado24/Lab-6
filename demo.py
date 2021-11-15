import time
import RPi.GPIO as gpio
from led8x8 import LEDdisplay

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 21, 26, 19

# Pick a number sequence
sequence = [8, 6, 7, 5, 3, 0, 9]

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

while True:
  for n in range(len(sequence)):
    theLEDdisplay.setNumber(sequence[n])
    time.sleep(0.4)

gpio.cleanup()