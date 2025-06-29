from machine import ADC, Pin, PWM
import time

# Cài đặt chân GPIO 34 cho cảm biến ánh sáng (analog)
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)  # Phạm vi đọc giá trị từ 0 đến 3.3V

# Cài đặt chân GPIO 13 cho LED với PWM
led = PWM(Pin(13), freq=5000)

def led_control():
    light_value = light_sensor.read()  # Đọc giá trị cảm biến ánh sáng trong khoảng từ 0 - 40
    led_brightness = int(light_value / 4)  # Chia cho 4 để giá trị trong khoảng 0-1023
    led.duty(led_brightness)  # Điều chỉnh độ sáng đèn LED
    time.sleep(0.1)  # Thêm độ trễ nhỏ để tránh làm quá tải CPU

# Gọi hàm để bắt đầu điều khiển độ sáng đèn LED
while True:
    led_control()

