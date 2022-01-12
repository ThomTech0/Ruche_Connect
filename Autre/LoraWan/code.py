# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import busio
import digitalio
import board
from adafruit_tinylora.adafruit_tinylora import TTN, TinyLoRa

# Board LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Create library object using our bus SPI port for radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)


# RFM9x Breakout Pinouts
cs = digitalio.DigitalInOut(board.D6)
irq = digitalio.DigitalInOut(board.D5)
rst = digitalio.DigitalInOut(board.D9)

# TTN Device Address, 4 Bytes, MSB
devaddr = bytearray([0x26, 0x0B, 0x16, 0x32])

# TTN Network Key, 16 Bytes, MSB
nwkey = bytearray(
    [
        0x37,
        0x7C,
        0xE1,
        0x81,
        0x27,
        0x4D,
        0xAA,
        0x18,
        0xBB,
        0x34,
        0x2A,
        0x59,
        0x0B,
        0x8E,
        0xEF,
        0x57,
    ]
)

# TTN Application Key, 16 Bytess, MSB
app = bytearray(
    [
        0x32,
        0x13,
        0xF4,
        0x56,
        0x19,
        0xF5,
        0xE1,
        0x77,
        0xB4,
        0x6B,
        0xF7,
        0x74,
        0x82,
        0xEF,
        0x30,
        0xDD,
    ]
)

ttn_config = TTN(devaddr, nwkey, app, country="EU")

lora = TinyLoRa(spi, cs, irq, rst, ttn_config)

# Data Packet to send to TTN
data = bytearray(4)

while True:
    temp_val = 5
    humid_val = 6
    print("Temperature: %0.2f C" % temp_val)
    print("relative humidity: %0.1f %%" % humid_val)

    # Encode float as int
    temp_val = int(temp_val * 100)
    humid_val = int(humid_val * 100)

    # Encode payload as bytes
    data[0] = (temp_val >> 8) & 0xFF
    data[1] = temp_val & 0xFF
    data[2] = (humid_val >> 8) & 0xFF
    data[3] = humid_val & 0xFF

    # Send data packet
    print("Sending packet...")
    lora.send_data(data, len(data), lora.frame_counter)
    print("Packet Sent!")
    led.value = True
    lora.frame_counter += 1
    time.sleep(2)
    led.value = False

