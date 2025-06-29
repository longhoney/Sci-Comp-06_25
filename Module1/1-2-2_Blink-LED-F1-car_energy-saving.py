from machine import Pin
import time

# Khởi tạo LED ở chân GPIO 2 (thay đổi nếu cần)
led = Pin(13, Pin.OUT)

while True:
    # Nháy 1: Sáng ngắn
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.2)

    # Nháy 2: Sáng ngắn
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.6)
