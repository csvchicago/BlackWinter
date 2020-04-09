from gpiozero import DistanceSensor
from time import sleep

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
b = TonalBuzzer(14)
b.play(Tone("A4"))
sleep(.1)
b.play(Tone("C4"))
sleep(.1)
b.stop()

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)


# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
sensorleft = DistanceSensor(echo=24, trigger=23, max_distance=3)
sensorright = DistanceSensor(echo=6, trigger=5, max_distance=3)
cmd = "hostname -I | cut -d\' \' -f1"

IP = subprocess.check_output(cmd, shell = True )
IP = IP.decode('UTF-8')

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load

    draw.text((x, top),       "Two Black Winter 1.0", font=font, fill=255)
    draw.text((x, top+8),     "IP: " + str(IP),  font=font, fill=255)
  #  draw.text((x, top+20),    str(CPU), font=font, fill=255)
  #  draw.text((x, top+30),    str(MemUsage),  font=font, fill=255)
#    Disk = print(f'DistanceLeft: {sensorleft.distance * 100:.2f}    DistanceRight: {sensorright.distance * 100:.2f}')
    Disk = f'Lft:{sensorleft.distance * 100:.2f} Rt: {sensorright.distance * 100:.2f}'
    draw.text((x, top+38),    str(Disk),  font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.display()
    sleep(1.0)







while True:
    print(f'DistanceLeft: {sensorleft.distance * 100:.2f}    DistanceRight: {sensorright.distance * 100:.2f}')
    sleep(1.0)

exit(0)