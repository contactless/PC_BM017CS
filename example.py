#!/usr/bin/python

# example driver for BM017 and TCS34725

import time
import smbus
from Adafruit_I2C import Adafruit_I2C
from PC_BM017CS import BM017


bm017 = BM017(True)

bm017.debug = False

bm017.readStatus()

bm017.isBM017There()

bm017.getColors()
bm017.readStatus()

bm017.disableDevice()
bm017.setIntegrationTimeAndGain(0x00, 0x03)

while 1:
    bm017.getColors()

    print "C: %s, R: %s, G: %s, B: %s\n" % (bm017.clear_color, bm017.red_color, bm017.green_color, bm017.blue_color)
