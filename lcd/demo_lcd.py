# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and output use
import lcddriver
import time

# Load the driver and set it to "output"
# If you use something from the driver library use the "output." prefix first
display = lcddriver.lcd()

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to output")
        display.lcd_display_string("Greetings Human!", 1) # Write line of text to first line of output
        display.lcd_display_string("Demo Pi Guy code", 2) # Write line of text to second line of output
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_display_string("I am a output!", 1)  # Refresh the first line of output with a different message
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_clear()                               # Clear the output of any data
        time.sleep(2)                                     # Give time for the message to be read

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
