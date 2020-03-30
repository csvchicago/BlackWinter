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

sensorleft = DistanceSensor(echo=24, trigger=23, max_distance=3)
sensorright = DistanceSensor(echo=6, trigger=5, max_distance=3)

while True:
    print(f'DistanceLeft: {sensorleft.distance * 100:.2f}    DistanceRight: {sensorright.distance * 100:.2f}')
    sleep(1.0)

exit(0)