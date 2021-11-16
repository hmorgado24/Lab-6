from shiftregisterclass import Shifter    # extend by composition

class led():

  pat = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, r, c):
    self.shifter.shiftByte(led.pat[c])  # load the row values
    self.shifter.shiftByte(1 << (r-1))   # select the given row
