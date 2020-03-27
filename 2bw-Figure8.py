from gpiozero import Robot
from gpiozero.tools import zip_values
from time import sleep
blackWinter = Robot(left=(7,8), right=(9,10))

blackWinter.stop()
print("setting full speed ahead straight 3 secs")
blackWinter.value = (1.0,1.0)
blackWinter.forward()
sleep(1)

#  print("pausing 3 secs")
  # blackWinter.stop()
# sleep(3)

print("3 sec turning left")
blackWinter.value = (0.1,1.0)
#blackWinter.forward()
sleep(11.5)
blackWinter.stop()

print("setting full speed ahead straight 3 secs")
blackWinter.value = (1.0,1.0)
blackWinter.forward()
sleep(4)

# print("pausing 3 secs")
# sleep(3)
# blackWinter.stop()

print("3 sec turning right")
blackWinter.value = (1.0,0.1)
sleep(11)
blackWinter.stop()
blackWinter.forward()
sleep(2)


print("done")
