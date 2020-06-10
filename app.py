from configparser import ConfigParser
import RPi.GPIO as GPIO
import mariadb
import time

config = ConfigParser()
config.read('appconfig.ini')

mdb_connection = mariadb.connect(
    user=config.get('mariadb', 'user'),
    password=config.get('mariadb', 'password'),
    database=config.get('mariadb', 'database'),
    host=config.get('mariadb', 'host'),
)
mdb_cursor = mdb_connection.cursor()

GPIO.setmode(GPIO.BCM)

MOTION_SENSOR_PIN = 4
LED_RED_PIN = 12
LED_GREEN_PIN = 12
LED_YELLOW_PIN = 12

GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_RED_PIN, GPIO.OUT)  # RED LED
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)  # GREEN LED
GPIO.setup(LED_YELLOW_PIN, GPIO.OUT)  # YELLOW LED

GPIO.output(LED_YELLOW_PIN, GPIO.HIGH)

try:
    time.sleep(2)
    while True:
        if GPIO.input(MOTION_SENSOR_PIN):
            mdb_cursor.execute("SELECT * FROM location_stats WHERE name = 'state' ")

            # print content
            row = mdb_cursor.fetchone()

            if row['value'] == 1:
                GPIO.output(LED_RED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_GREEN_PIN, GPIO.HIGH)

            time.sleep(2)  # to avoid multiple detection

            GPIO.output(LED_RED_PIN, GPIO.LOW)
            GPIO.output(LED_GREEN_PIN, GPIO.LOW)
        time.sleep(0.1)  # loop delay, should be less than detection delay
except:
    GPIO.cleanup()
