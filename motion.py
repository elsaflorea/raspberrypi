from configparser import ConfigParser
import datetime
from rethinkdb import r
import RPi.GPIO as GPIO
import time

config = ConfigParser()
config.read('appconfig.ini')

GPIO.setmode(GPIO.BCM)

MOTION_SENSOR_PIN = 4
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


try:
    time.sleep(2)
    while True:
        if GPIO.input(MOTION_SENSOR_PIN):

            r.db(config.get('rethinkdb', 'database')).table(config.get('rethinkdb', 'motion_table')).insert({
                'room_id': 'room_0',
                'date': log_time
            }).run()

            time.sleep(1) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay
except:
    GPIO.cleanup()



