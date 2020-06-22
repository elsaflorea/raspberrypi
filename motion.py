from configparser import RawConfigParser
import datetime
from rethinkdb import r
import RPi.GPIO as GPIO
import time

config = RawConfigParser()
config.read('appconfig.ini')

GPIO.setmode(GPIO.BCM)

MOTION_SENSOR_PIN = 4
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

r.connect(config.get('rethinkdb', 'host'), config.get('rethinkdb', 'port')).repl()

mdb_connection = mariadb.connect(
    user=config.get('mariadb', 'user'),
    password=config.get('mariadb', 'password'),
    database=config.get('mariadb', 'database'),
    host=config.get('mariadb', 'host'),
)
mdb_cursor = mdb_connection.cursor()

try:
    time.sleep(2)
    while True:
        if GPIO.input(MOTION_SENSOR_PIN):
            mdb_cursor = mdb_connection.cursor()
            mdb_cursor.execute("SELECT value as state_value FROM location_stats WHERE name = 'state' ")

            # print content
            row = mdb_cursor.fetchone()

            print(row)

            log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            r.db(config.get('rethinkdb', 'database')).table(config.get('rethinkdb', 'motion_table')).insert({
                'room_id': 'room_0',
                'date': log_time
            }).run()

            time.sleep(1) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay
except:
    GPIO.cleanup()
