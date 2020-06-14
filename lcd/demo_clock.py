# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and output use
import lcddriver
import time
import datetime

# Load the driver and set it to "output"
# If you use something from the driver library use the "output." prefix first
display = lcddriver.lcd()

try:
    print("Writing to output")
    display.lcd_display_string("No time to waste", 1) # Write line of text to first line of output
    while True:
        display.lcd_display_string(str(datetime.datetime.now().time()), 2) # Write just the time to the output
        # Program then loops with no delay (Can be added with a time.sleep)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()