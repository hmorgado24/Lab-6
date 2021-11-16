from shiftregisterclass import Shifter    # extend by composition
import time

class LEDdisplay():

  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.Shifter = Shifter(data, latch, clock)
 
  def display(self, row, col):  # display a given number
    self.Shifter.shiftByte(LEDdisplay.pattern[col])
    self.Shifter.shiftByte(LEDdisplay.pattern(1 << row))
  
data, latch, clock = 21, 19, 26
pins = LEDdisplay(data, latch, clock)

while True:
  for n in range(8):
    pins.display(n, n)
    time.sleep(.001)