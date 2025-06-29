from machine import Pin; import time #time là một thư viện thuộc hệ khác với Pin

#Cài đặt chân GPIO 13 làm output cho LED
led = Pin(13, Pin.OUT)

# Cài đặt chân GPIO 5 làm input cho nút nhấn
button = Pin(5, Pin.IN, Pin.PULL_UP)


while True:
		# Kiểm tra điều kiện: nút được nhấn
    if button.value() == 1:  # Nút không được nhấn
        led.off()  # nếu đúng, bật đèn LED
    else:
        led.on()  # nếu sai, tắt đèn LED
		#time.sleep(0.5) //phần mềm báo lỗi indent (thụt đầu dòng)
    time.sleep(0.5)