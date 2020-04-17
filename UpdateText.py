'''
from guizero import App, Text
from time import sleep

app = App("Hello world")
text = Text(app, text="1")
while True:
    text.value = int(text.value) + 1
    sleep(1)
    app.display()
'''
from guizero import App, Text
from gpiozero import Robot
from gpiozero.tools import zip_values
import sys
TwoBlackWinter = Robot(left=(7, 8), right=(9, 10))

# Action you would like to perform
def counter():
    formatit = float(text.value)
    formatit = formatit + .05
    #formatit = f"{formatit:.2f}"
    formatit = "%.2f" % formatit
    text.value = formatit
    #print(f"x is now-->{text.value:.2f}")
    if float(text.value) > 1.00:
        TwoBlackWinter.forward(0)
        TwoBlackWinter.stop
        sys.exit(0)
    TwoBlackWinter.right(float(text.value))

app = App("BW - Rotation Speed Test")
text = Text(app, text=".00", size=110)
text.repeat(3000, counter)  # Schedule call to counter() every 1000ms
app.display()
