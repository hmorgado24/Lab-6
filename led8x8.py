from shiftregisterclass import Shifter    # extend by composition

class led():

  pat = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def display(row, col):  # display a given number
    Shifter.shiftByte(led.pat[col])
    Shifter.shiftByte(1 << row)
