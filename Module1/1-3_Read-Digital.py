from machine import Pin; import time #time là một thư viện thuộc hệ khác với Pin
#Cài đặt chân GPIO 5 làm input cho nút nhấn
button = Pin(5, Pin.IN, Pin.PULL_UP)

# Đọc trạng thái của nút nhấn
while True:
    if button.value() == 1:  # Nút được nhấn
        print("Button released")
    else:
        print("Button pressed")
    time.sleep(0.5)
