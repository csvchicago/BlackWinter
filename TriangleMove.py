from gpiozero import Robot
from time import sleep
blackWinter = Robot(left=(7,8), right=(9,10))

blackWinter.forward()
sleep(1)
blackWinter.stop()

blackWinter.right()
sleep(.55)
blackWinter.stop()

blackWinter.forward()
sleep(2)
blackWinter.stop()

blackWinter.right()
sleep(.55)
blackWinter.stop()

blackWinter.forward()
sleep(2)
blackWinter.stop()

blackWinter.right()
sleep(.55)
blackWinter.stop()

blackWinter.forward()
sleep(1)
blackWinter.stop()
