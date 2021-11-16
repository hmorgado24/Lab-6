import time
from led8x8 import LEDdisplay

data, latch, clock = 21, 19, 26
leddisp = LEDdisplay(data, latch, clock)

while True:
  for n in range(8):
    LEDdisplay.display(n)
    time.sleep(.001)