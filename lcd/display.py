import lcddriver
import time
import Adafruit_DHT

# Load the driver and set it to "output"
# If you use something from the driver library use the "output." prefix first
display = lcddriver.lcd()

sensor = Adafruit_DHT.DHT11

# Main body of code
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, 21)
<<<<<<< HEAD
        print("Writing to output")
=======
        print(f"Writing to display temp: {temperature}, hum: {humidity}")
>>>>>>> 9bd875c3ef13dee3c29dc5e42c6fdc234b04c6f8
        display.lcd_display_string("Casa inteligenta!", 1) # Write line of text to first line of output
        display.lcd_display_string(f"Temperatura: {temperature}", 2) # Write line of text to second line of output
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_display_string(f"Umiditate: {humidity}", 2)  # Refresh the first line of output with a different message
        time.sleep(2)                                     # Give time for the message to be read                                  # Give time for the message to be read

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
