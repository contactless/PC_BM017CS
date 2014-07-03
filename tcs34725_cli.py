#!/usr/bin/python

# example driver for BM017 and TCS34725

import time
import smbus
from Adafruit_I2C import Adafruit_I2C
from PC_BM017CS import BM017

import argparse
if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='TCS34725 CLI')

    parser.add_argument('--int-time', dest='integration_time', type=float,
                     help='Integration time in ms. Must be between 2.4ms and 614.4ms. Default is 614.4ms', default=614.4)
    parser.add_argument('--gain', dest='gain', type=int,
                     help='Gain. Can be 1, 4, 16 or 60. Default is 60x.', default=60)

    parser.add_argument('--samples', dest='samples', type=int,
                     help='Number of measureemnts to make. Default is indefinite')

    args = parser.parse_args()

    if not (2.4 <= args.integration_time  <= 614.4):
        parser.print_usage()
        raise RuntimeError("integration time must be between  2.4ms and 614.4ms")

    int_quanta = args.integration_time / 2.4
    if int(int_quanta) != int_quanta:
        parser.print_usage()
        raise RuntimeError("integration time must be in multiply of 2.4ms")

    if args.gain not in (1,4,16,60):
        parser.print_usage()
        raise RuntimeError("Gain must be 1, 4, 16 or 60.")

    reg_gain = { 1: 0x00, 4: 0x01, 16: 0x02, 60: 0x03} [args.gain]
    reg_int_time = 256 - int(int_quanta)


    bm017 = BM017(False)
    bm017.readStatus()
    bm017.isBM017There()
    bm017.getColors()
    bm017.readStatus()
    bm017.disableDevice()


    bm017.setIntegrationTimeAndGain(reg_int_time, reg_gain)

    counter = 0
    while 1:
        bm017.getColors()
        time.sleep(args.integration_time * 1E-3)

        print "C: %s, R: %s, G: %s, B: %s" % (bm017.clear_color, bm017.red_color, bm017.green_color, bm017.blue_color)

        counter += 1
        if args.samples and (counter >= args.samples):
            break


