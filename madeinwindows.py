from gpiozero import Robot
from time import sleep

blackWinter = Robot(left=(7,8), right=(9,10))

blackWinter.forward()
sleep(2)
blackWinter.stop()
