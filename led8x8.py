from shiftR import Shifter    # extend by composition

class led():

  pat = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shift = Shifter(data, latch, clock)
 
  def display(r, c):
    Shifter.shiftByte(led.pat[c])  # load the row values
    Shifter.shiftByte(1 << (r-1))   # select the given row
