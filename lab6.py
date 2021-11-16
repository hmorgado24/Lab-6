from led8x8 import led
from shiftregisterclass import Shifter
import time
import multiprocessing
import random

def bug(dataPin, latchPin, clockPin): #lighting bug "random walking" function
  row = random.randint(1, 8)
  col = random.randint(0, 7)

  leddisp = led(data, latch, clock) #create an LED display obj that extends 8x8 class

  while True:
    Rrow = random.randint(-1, 1) #change of x by one
    Rcol = random.randint(-1, 1) #change of y by one 

    led.display(row, col) #display initial random position
    time.sleep(0.1) #requested time delay

    if (row + Rrow < 0 or row + Rrow > 7):
      row = row
    else:
      row += Rrow
    
    if (col + Rcol < 0 or col + Rcol  > 7):
      col = col
    else:
      col += Rcol


# def multiA():

#   pat = multiprocessing.Array('i', 8)
#   pat[0], pat[1], pat[2], pat[3], pat[4], pat[5], pat[6], pat[7] = 0b01111111, 0b10111111, 0b11011111, 0b11101111, 0b11110111, 0b11111011, 0b11111101, 0b11111110

# multi = multiprocessing.Process(target=multiA)
# multi.start

data, latch, clock = 21, 19, 26
p = multiprocessing.Process(target=lightningbug, args=(data, latch, clock))
p.start()

# while True:

#   data, latch, clock = 21, 19, 26
#   leddisp = led(data, latch, clock)
  
#   lightningbug(data, latch, clock)