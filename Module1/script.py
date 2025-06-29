from machine import Pin
import time

# Set up GPIO 13 for the LED
led = Pin(13, Pin.OUT)

print("running script.py")
# Blink the LED 5 times
for i in range(5):
#while True:
    led.on()  # Turn the LED on
    time.sleep(0.5)  # Wait 0.5 seconds
    led.off()  # Turn the LED off
    time.sleep(0.5)  # Wait 0.5 seconds

