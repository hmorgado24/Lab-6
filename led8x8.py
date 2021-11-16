from shiftregisterclass import Shifter    # extend by composition

class LEDdisplay():

  rows = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.Shifter = Shifter(data, latch, clock)
 
  def display(self, num):  # display a given number
    self.Shifter.shiftByte(LEDdisplay.rows[num])
    self.Shifter.shiftByte(LEDdisplay.pattern[num])