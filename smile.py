import time
from led8x8 import LEDdisplay

data, latch, clock = 21, 19, 26
pins = LEDdisplay(data, latch, clock)

while True:
  for n in range(8):
    pins.display(n)
    time.sleep(.001)