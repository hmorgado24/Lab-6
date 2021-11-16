from shiftregisterclass import Shifter    # extend by composition
import time

class LEDdisplay():

  pattern = [0b01111111, 0b10111111, 0b11011111, 0b11101111, 0b11110111, 0b11111011, 0b11111101, 0b11111110]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, row, col):  # display a given number
    self.shifter.shiftByte(LEDdisplay.pattern[col])
    self.shifter.shiftByte(1 << row)
  
data, latch, clock = 21, 19, 26
pins = LEDdisplay(data, latch, clock)

while True:
  for n in range(8):
    pins.display(n, n)
    time.sleep(.01)  