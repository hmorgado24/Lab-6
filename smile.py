import time
from led8x8 import LEDdisplay
from shiftregisterclass import Shifter

data, latch, clock = 21, 19, 26
leddisp = Shifter(data, latch, clock)

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]

while True:
  for n in range(len(pattern)):

    leddisp.shiftByte(pattern[n])
    time.sleep(.6)