#TestCompassTurnNorth

from gpiozero import Robot
from gpiozero.tools import zip_values
from time import sleep
import py_qmc5883l

sensor = py_qmc5883l.QMC5883L()
sensor.calibration = [[1.0124554030038653, -0.02946998375102533, -561.7134736702388],
                      [-0.02946998375102533, 1.0697271651520381, 1255.7392354217145],
                      [0.0, 0.0, 1.0]]
m = sensor.get_magnet()
print(m)

TwoBlackWinter = Robot(left=(7, 8), right=(9, 10))
# Marc suggested:
# direction = sense.get_orientation()['yaw'] to get the angle.

n = sensor.get_bearing()
n = n + 90
if n > 360:
    n = n - 360
print(f"Initial compass reading = {n}")


def rotate_to_direction(new_direction):
    n = int(sensor.get_bearing())
    n = n + 90
    if n > 360:
        n = n - 360
    print(n)
    current_direction = n
    print(f" Current={current_direction} headingto={new_direction}")
    if current_direction == new_direction:
        return
    if current_direction > new_direction:
        diff = new_direction - current_direction + 360
    else:
        diff = new_direction - current_direction
    if diff < 180:  # rotate right is more efficient
        TwoBlackWinter.right(0.4)
    else:
        TwoBlackWinter.left(0.4)
    while n != new_direction:
        n = int(sensor.get_bearing())
        n = n + 90
        if n > 360:
            n = n - 360
        print(f"curr={n} head2={new_direction}")
        continue
    return


rotate_to_direction(180)
'''
for i in range(4):
    rotate_to_direction(i * 90)
    TwoBlackWinter.forward(0.6)
    sleep(0.8)
    n = int(sensor.get_bearing())
    n = n + 90
    if n > 360:
        n = n - 360
    print(f"At end of turn compass heading is: {n}")
'''


TwoBlackWinter.stop()

#print("setting full speed ahead straight 3 secs")
#blackWinter.value = (1.0, 1.0)
#blackWinter.forward()
#sleep(1)

#print("3 sec turning left")
#blackWinter.value = (0.1, 1.0)
## blackWinter.forward()
#sleep(11.5)
#blackWinter.stop()

