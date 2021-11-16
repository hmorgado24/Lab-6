from shiftR import Shifter    # extend by composition

class led():

  pat = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shift = Shifter(data, latch, clock)
 
  def display(self, r, c):
    self.shift.shiftByte(led.pat[c])  # load the row values
    self.shift.shiftByte(1 << (r-1))   # select the given row
