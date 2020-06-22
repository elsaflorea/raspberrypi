from configparser import RawConfigParser
from rethinkdb import r
import RPi.GPIO as GPIO
import mariadb
import time
import datetime

config = RawConfigParser()
config.read('appconfig.ini')

mdb_connection = mariadb.connect(
    user=config.get('mariadb', 'user'),
    password=config.get('mariadb', 'password'),
    database=config.get('mariadb', 'database'),
    host=config.get('mariadb', 'host'),
)
mdb_cursor = mdb_connection.cursor()

r.connect(config.get('rethinkdb', 'host'), config.get('rethinkdb', 'port')).repl()

GPIO.setmode(GPIO.BCM)

MOTION_SENSOR_PIN = 4
BUZZ_PIN = 26
LED_RED_PIN = 12
LED_YELLOW_PIN = 16
LED_GREEN_PIN = 20

GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
GPIO.setup(BUZZ_PIN, GPIO.OUT)  # BUzzer
GPIO.setup(LED_RED_PIN, GPIO.OUT)  # RED LED
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)  # GREEN LED
GPIO.setup(LED_YELLOW_PIN, GPIO.OUT)  # YELLOW LED

GPIO.output(LED_YELLOW_PIN, GPIO.HIGH)
GPIO.output(LED_RED_PIN, GPIO.LOW)
GPIO.output(LED_GREEN_PIN, GPIO.LOW)


try:
    time.sleep(2)
    while True:
        if GPIO.input(MOTION_SENSOR_PIN):

            log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            r.db('rpi').table(config.get('rethinkdb', 'motion_table')).insert({
                'room_id': 'bedroom_1',
                'date': log_time
            }).run()
            
            # mdb_cursor = mdb_connection.cursor()
            mdb_cursor.execute("SELECT value as state_value FROM location_stats WHERE name = 'state' ")

            # print content
            row = mdb_cursor.fetchone()
            print(row[0])

            if row[0] == 1:
                GPIO.output(LED_RED_PIN, GPIO.HIGH)
                GPIO.output(BUZZ_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_GREEN_PIN, GPIO.HIGH)

            time.sleep(2)  # to avoid multiple detection

        GPIO.output(LED_RED_PIN, GPIO.LOW)
        GPIO.output(LED_GREEN_PIN, GPIO.LOW)
        GPIO.output(BUZZ_PIN, GPIO.LOW)
        time.sleep(0.1)  # loop delay, should be less than detection delay
except:
    GPIO.cleanup()
