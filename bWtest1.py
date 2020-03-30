from gpiozero import Robot
from time import sleep
import sys


#from gpiozero import Buzzer
#bz = Buzzer(14)
#bz.on()

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
b = TonalBuzzer(14)
b.play(Tone("A4"))


blackWinter = Robot(left=(7,8), right=(9,10))

blackWinter.forward()
sleep(2)
blackWinter.stop()
exit()
sys.exit