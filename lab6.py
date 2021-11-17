import time
import random
from led8x8 import led
import multiprocessing

def lightningbug(data, latch, clock): 
  row = random.randint(0, 7)
  col = random.randint(0, 7)

  leddisp = led(data, latch, clock) 

  while True:
    Rrow = random.randint(-1, 1) 
    Rcol = random.randint(-1, 1)  

    leddisp.display(row, col)
    time.sleep(0.1) 

    if (row + Rrow < 0 or row + Rrow > 7): 
      row = row 
    else:
      row += Rrow 

    if (col + Rcol < 0 or col + Rcol > 7): 
      col = col 
    else:
      col += Rcol 

data, latch, clock = 21, 19, 26 

p = multiprocessing.Process(target=lightningbug, args=(data, latch, clock)) 
p.start() 
