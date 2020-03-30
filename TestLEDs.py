from gpiozero import LED
from time import sleep

ledred = LED(17)
ledgreen = LED(27)
#ledblue = LED(22)

ledred.on()
sleep(1)
ledred.off()

ledgreen.on()
sleep(1)
ledgreen.off()

#ledblue.on()
#sleep(1)
#ledblue.off()

print("Done")