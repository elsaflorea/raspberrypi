# import Adafruit_DHT
import datetime
from rethinkdb import r
from configparser import RawConfigParser

config = RawConfigParser()
config.read('appconfig.ini')

r.connect(config.get('rethinkdb', 'host'), config.get('rethinkdb', 'port')).repl()
# r.db('rpi').table_create('temp_hum_log').run()


# sensor = Adafruit_DHT.DHT11
# humidity, temperature = Adafruit_DHT.read_retry(sensor, 21)
humidity = 1
temperature = 20

log_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

r.db('rpi').table(config.get('rethinkdb', 'temp_hum_table')).insert({
    'room_id': 'bedroom_1',
    'temp': temperature,
    'hum': humidity,
    'date': log_time
}).run()
