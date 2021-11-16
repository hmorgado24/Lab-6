from shiftregisterclass import Shifter    # extend by composition

class led():

  pat = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(self, row, col):  # display a given number
    self.shifter.shiftByte(led.pat[col])
    self.shifter.shiftByte(1 << row)
