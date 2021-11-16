from led8x8 import led

import time
import multiprocessing
import random


def lightningbug(data, latch, clock):

  row = random.randint(0,7)
  col = random.randint(0,7)

  while True:
    Rrow = random.randint(-1, 1)
    Rcol = random.randint(-1, 1)

    led.display(row, col)

    if (row + Rrow < 0 or row + Rrow > 7):
      row = row
    else:
      row += Rrow
    
    if (col + Rcol < 0 or col + Rcol  > 7):
      col = col
    else:
      col += Rcol
    
    time.sleep(.01)

def multiA():

  pat = multiprocessing.Array('i', 8)
  pat[0], pat[1], pat[2], pat[3], pat[4], pat[5], pat[6], pat[7] = 0b01111111, 0b10111111, 0b11011111, 0b11101111, 0b11110111, 0b11111011, 0b11111101, 0b11111110

multi = multiprocessing.Process(target=multiA)
multi.start

while True:

  data, latch, clock = 21, 19, 26
  leddisp = led(led.data, led.latch, led.clock)
  
  lightningbug(data, latch, clock)
