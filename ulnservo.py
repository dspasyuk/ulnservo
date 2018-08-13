# License: GPL
# GNU GENERAL PUBLIC LICENSE
# Copyright (C) Denis Spasyuk
import machine
import time
d1 = machine.Pin(5, machine.Pin.OUT)  # D1 # IO5
d2 = machine.Pin(4, machine.Pin.OUT)  # D2 # IO4
d3 = machine.Pin(0, machine.Pin.OUT)  # D3 # IO0
d4 = machine.Pin(14, machine.Pin.OUT) # D5 # IO14

cw = [[1, 0, 0, 1],
      [1, 0, 0, 0],
      [1, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 1],
      [0, 0, 0, 1]]

ccw = [[0, 0, 0, 1],
      [0, 0, 1, 1],
      [0, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 1]]

def stop():
    d1.off()
    d2.off()
    d3.off()
    d4.off()

def servo(angle, direction):
   stop()
   count = 1
   rotation = int(angle*512/360)
   t = 0.0015
   if direction == "cw":
        while count < rotation:
            for run in cw:
                 if run[0] == 1:
                     d1.on()
                 else:
                     d1.off()
                 if run[1] == 1:
                     d2.on()
                 else:
                     d2.off()
                 if run[2] == 1:
                     d3.on()
                 else:
                     d3.off()
                 if run[3] ==1:
                     d4.on()
                 else:
                     d4.off()
                 time.sleep(t)
            count = count +1
   if direction == "ccw":
        while count < rotation:
             for run in ccw:
                 if run[0] == 0:
                     d1.off()
                 else:
                     d1.on()
                 if run[1] == 0:
                     d2.off()
                 else:
                     d2.on()
                 if run[2] == 0:
                     d3.off()
                 else:
                     d3.on()
                 if run[3] == 0:
                     d4.off()
                 else:
                     d4.on()
                 time.sleep(t)
                 count = count +1
   if count == rotation:
       stop()
