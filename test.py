import Adafruit_DHT
import sys
sensor = Adafruit_DHT.DHT11
pin = 3

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("humidity: ", humidity)
    print("temperature: ", temperature)
