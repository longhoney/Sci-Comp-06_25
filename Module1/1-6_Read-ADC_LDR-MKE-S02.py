from machine import ADC, Pin
import time #time là một thư viện thuộc hệ khác với ADC và Pin

# Cài đặt chân GPIO 34 làm input cho cảm biến ánh sáng (analog)
light_sensor = ADC(Pin(34))
light_sensor.atten(ADC.ATTN_11DB)  # Tăng độ phân giải đến 0-3.3V

# Đọc giá trị cảm biến ánh sáng
while True:
    light_value = light_sensor.read()  # Đọc giá trị ADC (0-4095)
    # Chuyển đổi giá trị ADC thành Volt
    voltage = (light_value * 3.3) / 4095  # Tương ứng với điện áp 0-3.3V
    
    print("Light Sensor Value:", light_value)
    #print("Voltage:", voltage, "V") #"Ẩn" dòng này để sử dụng Plotter của Thonny
    time.sleep(0.3)
