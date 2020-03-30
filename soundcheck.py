from gpiozero import Robot
from time import sleep

# Wrong kind of buzzer
#from gpiozero import Buzzer
#bz = Buzzer(14)
#bz.on()

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
b = TonalBuzzer(14)
b.play(Tone("A4"))
sleep(.1)
b.play(Tone("C4"))
sleep(.1)
b.play(Tone("D4"))
sleep(.1)
b.play(Tone("E4"))
sleep(.1)
b.stop()

exit(0)