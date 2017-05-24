#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Copyright (c) 2017 Shrewsbury Pi
# Base is 
#    git clone https://github.com/adafruit/Adafruit_Python_MCP9808.git
#    git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
# Just to get initialization going
# Author: Matthew Karas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_MCP9808.MCP9808 as MCP9808

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def to_farenheit(c):
    """ Convert a celcius reading to farenheit """
    return ((c * 9.0) / 5.0) + 32.0

PADDING = 2
# Raspberry Pi pin configuration:
RST = 25
# Note the following are only used with SPI:
DC = 24
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
spi_dev=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=spi_dev)

# temp sensor
temp_sensor = MCP9808.MCP9808()
temp_sensor.begin()
# Initialize library.
disp.begin()
disp.clear()
disp.display()

# get values for display
width = disp.width
height = disp.height
top = PADDING
font = ImageFont.truetype('PressStart2P.ttf', 18)


# start drawing
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
while True:
    temp_f = to_farenheit(temp_sensor.readTempC())
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    x = PADDING 
    draw.text((x, x), '{0:0.1F}°F'.format(temp_f), font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(1)
