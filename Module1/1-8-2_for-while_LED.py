from machine import Pin, PWM
import time

# Cài đặt chân GPIO 13 làm output cho LED với PWM
led = PWM(Pin(13), freq=5000)

# Hiệu ứng tăng và giảm độ sáng đèn LED
    #trái tim thổn thức 0.01
while True:
    # Tăng độ sáng
    for duty in range(0, 1023, 10):
        led.duty(duty)
        time.sleep(0.015)
    # Giảm độ sáng
    for duty in range(1023, 0, -10):
        led.duty(duty)
        time.sleep(0.015)
