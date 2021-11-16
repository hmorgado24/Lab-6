from shiftregisterclass import Shifter    # extend by composition
import time

class LEDdisplay():

  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

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
    time.sleep(.001)  