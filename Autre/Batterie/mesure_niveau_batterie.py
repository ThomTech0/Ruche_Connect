#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:50:42 2022

@author: Anaelle
"""

import board
from analogio import AnalogIn

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2


battery_voltage = get_voltage(vbat_voltage)
print("VBat voltage: {:.2f}".format(battery_voltage))