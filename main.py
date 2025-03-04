from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(16))

while True:
    try:
        sleep(1)
        # The DHT11 returns at most one measurement every 1s
        sensor.measure()
        # Retrieves measurements from the sensor
        print(f"Temperature : {sensor.temperature():.1f}")
        print(f"Humidity    : {sensor.humidity():.1f}")
        # Transmits the temperature to the computer console
    except OSError as e:
        print('Failed reception')
        # If esp does not receive the measurements from the sensor