from shiftR import Shifter    # extend by composition

class led():

  pat = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shiftR = Shifter(data, latch, clock)
 
  def display(self, r, c):
    self.shiftR.shiftByte(led.pat[c])  # load the row values
    self.shiftR.shiftByte(1 << (r-1))   # select the given row
