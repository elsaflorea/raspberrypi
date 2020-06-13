import Adafruit_DHT
import time
import datetime
from rethinkdb import r
from configparser import RawConfigParser

config = RawConfigParser()
config.read('appconfig.ini')

r.connect(config.get('rethinkdb', 'host'), config.get('rethinkdb', 'port')).repl()


sensor = Adafruit_DHT.DHT11

while True:
    log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, 21)

    print(f"temp: {temperature} hum: {humidity} at {log_time}")
    r.db('rpi').table(config.get('rethinkdb', 'temp_hum_table')).insert({
        'room_id': 'bedroom_1',
        'temp': temperature,
        'hum': humidity,
        'date': log_time
    }).run()

    time.sleep(1)
