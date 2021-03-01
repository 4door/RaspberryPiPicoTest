from machine import Pin

import time

led = Pin(25, Pin.OUT)

while True:
    time.sleep(1.0) #1秒待機
    led.value(1)

    time.sleep(1.0) #1秒待機
    led.value(0)