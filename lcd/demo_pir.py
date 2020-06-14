import sys

sys.path.append('../lcd/')

from gpiozero import LED
from gpiozero import MotionSensor
import lcddriver

display = lcddriver.lcd()
red_led = LED(20)
pir = MotionSensor(27)

try:
    while True:
        pir.wait_for_active()
        red_led.blink(5)
        # # Write line of text to first line of output
        display.lcd_display_string("Motion detected", 1)
        pir.wait_for_inactive()
        display.lcd_clear()
        red_led.off()

except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
    red_led.off()