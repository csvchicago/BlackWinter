from gpiozero import Robot
from time import sleep


#from gpiozero import Buzzer
#bz = Buzzer(14)
#bz.on()

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
b = TonalBuzzer(14)
b.play(Tone("A4"))
exit

blackWinter = Robot(left=(7,8), right=(9,10))

blackWinter.forward()
sleep(2)
blackWinter.stop()

sleep(2)

blackWinter.backward()
sleep(2)
blackWinter.stop()

sleep(2)

blackWinter.right(1.0)
sleep(1)
blackWinter.stop()

sleep(2)

blackWinter.left(1.0)
sleep(1)
blackWinter.stop()

sleep(2)

blackWinter.forward()
sleep(2)
blackWinter.stop()